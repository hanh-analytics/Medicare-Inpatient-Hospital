import pandas as pd
import plotly.express as px
import dash
import numpy as np
from dash import dcc, html
# Load Excel file
file_path = "/Users/DELL/Desktop/Projects/CMS Program Statistics - Medicare Inpatient Hospital/2021/CPS MDCR INPT 2021.xlsx"
extra_file = "/Users/DELL/Desktop/Projects/CMS Program Statistics - Medicare Inpatient Hospital/2021/CPS MDCR INPT 2020.xlsx"

def create_hospital_payment_comparison(file_path, chart_title="Hospital Program Payment Comparison"):  
     # Read the data from the sheet containing relevant columns
    df = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 4", header=3, usecols=["Type of Hospital", "Total Program Payments"], dtype=str)

    # Rename columns for clarity (do this *before* dropping NAs if possible)
    df.columns = ["Type of Hospital" ,"Total Program Payments"]

    # Convert numeric columns to proper data types (removing dots for thousands separators)
    df["Total Program Payments"] = pd.to_numeric(df["Total Program Payments"].str.replace('.', '', regex=False), errors='coerce')
    
    # Drop rows with missing values in key columns (after renaming and converting)
    df = df.dropna(subset=["Total Program Payments"])

    # Apply a log transformation to the 'Total Program Payments' to better visualize smaller values
    df["Log Program Payments"] = np.log1p(df["Total Program Payments"])  # log1p is used to handle 0 values
    
    # Plot the bar chart with the transformed values
    fig = px.bar(df, x="Type of Hospital", y="Log Program Payments", 
                 title=chart_title, 
                 labels={"Type of Hospital": "Type of Hospital", "Log Program Payments": "Log of Program Payments ($)"},
                 color_discrete_sequence=['rgb(57, 105, 172)'])  # Set the color
    
    return fig


def create_hospital_impact_bubble_chart(file_path, chart_title="Impact of Hospital Size and Affiliation on Costs"):
    # Read the data from the sheet
    df = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 4", header=3)

    # Remove any non-numeric characters (e.g., commas, dots) from the columns before converting to numeric
    df["Total Program Payments"] = pd.to_numeric(df["Total Program Payments"].replace({',': '', '.': ''}, regex=True), errors='coerce')
    df["Hospital Size"] = pd.to_numeric(df["Total Persons With Utilization"].replace({',': '', '.': ''}, regex=True), errors='coerce')

    # Drop rows with missing values in any key columns
    df = df.dropna(subset=["Total Program Payments", "Hospital Size", "Type of Hospital"])  # Keep original column name for now

    # Rename the column *after* dropping NAs to avoid potential issues
    df.rename(columns={"Type of Hospital": "Type of Hospital"}, inplace=True)

    # Create the bubble chart
    min_size = 8  # Set your minimum size
    scale_factor = 2 # Adjust scaling factor as needed
    max_size = 40
    fig = px.scatter(df, x="Type of Hospital", y="Total Program Payments", size=np.maximum(min_size, np.log(df["Hospital Size"] + 1) * scale_factor),
                 size_max = max_size,
                     title=chart_title, 
                     labels={"Type of Hospital": "Type of Hospital",  # Updated label here
                             "Total Program Payments": "Program Payments ($)", 
                             "Hospital Size": "Hospital Size (Persons With Utilization)"},
                     color="Type of Hospital", # To color bubbles by affiliation
                     hover_name="Type of Hospital", hover_data=["Type of Hospital", "Total Program Payments"],
                     color_discrete_sequence=px.colors.qualitative.Set3)
    
    return fig

def create_policy_impact_chart(file_path, extra_file, chart_title="Observable Impacts of Policy Changes Over Time"):
    # Load main dataset
    df_1 = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 1", header=4)
    df_1 = df_1.dropna(axis=1, how="all")

    df_1.columns = ["Type of Entitlement and Calendar Year", "Total Original Medicare Part A Enrollees", 
                    "Total Persons With Utilization", "Total Discharges"] + [f"Unnamed_{i}" for i in range(len(df_1.columns)-4)]

    df_1 = df_1.dropna(how="all")

    # Extract the relevant section
    all_beneficiaries_index = df_1[df_1["Type of Entitlement and Calendar Year"] == "All Beneficiaries"].index

    if not all_beneficiaries_index.empty:
        start_index = all_beneficiaries_index[0] + 1
        df_1_all_beneficiaries = df_1.iloc[start_index:start_index + 6]

        df_1_all_beneficiaries["Year"] = pd.to_numeric(df_1_all_beneficiaries["Type of Entitlement and Calendar Year"], errors='coerce')
        df_1_all_beneficiaries.dropna(subset=["Year", "Total Discharges"], inplace=True)
        df_1_all_beneficiaries["Year"] = df_1_all_beneficiaries["Year"].astype(int)

        # Load extra dataset containing 2015
        df_extra = pd.read_excel(extra_file, sheet_name="MDCR INPT HOSP 1", header=4)
        df_extra = df_extra.dropna(axis=1, how="all")

        df_extra.columns = ["Type of Entitlement and Calendar Year", "Total Original Medicare Part A Enrollees", 
                            "Total Persons With Utilization", "Total Discharges"] + [f"Unnamed_{i}" for i in range(len(df_extra.columns)-4)]

        df_extra = df_extra.dropna(how="all")

        extra_beneficiaries_index = df_extra[df_extra["Type of Entitlement and Calendar Year"] == "All Beneficiaries"].index

        if not extra_beneficiaries_index.empty:
            extra_start_index = extra_beneficiaries_index[0] + 1
            df_extra_all_beneficiaries = df_extra.iloc[extra_start_index:extra_start_index + 1]  # Only get 2015

            df_extra_all_beneficiaries["Year"] = pd.to_numeric(df_extra_all_beneficiaries["Type of Entitlement and Calendar Year"], errors='coerce')
            df_extra_all_beneficiaries.dropna(subset=["Year", "Total Discharges"], inplace=True)
            df_extra_all_beneficiaries["Year"] = df_extra_all_beneficiaries["Year"].astype(int)

            # Concatenate both datasets
            df_final = pd.concat([df_1_all_beneficiaries, df_extra_all_beneficiaries])

            # Sort by Year
            df_final = df_final.sort_values(by="Year")

            # Create the line chart using "Total Discharges" instead of "Total Persons With Utilization"
            fig = px.line(df_final, 
                          x="Year", 
                          y="Total Discharges",  # Switch to Discharges
                          markers=True,  
                          title=chart_title,
                          labels={"Year": "Year", "Total Discharges": "Discharges"})  # Rename label

            fig.update_traces(line=dict(color="rgb(57, 105, 172)"))

            # Policy changes to annotate
            policy_years = {
                2015: "Medicare Access and CHIP Reauthorization Act",
                2020: "COVID-19 Impact"
            }

            # Add policy change annotations
            for year, policy in policy_years.items():
                fig.add_vline(x=year, line_dash="dash", line_color="red")
                fig.add_annotation(
                    x=year, 
                    y=df_final["Total Discharges"].max(),
                    text=policy, 
                    showarrow=True, 
                    arrowhead=2,
                    font=dict(color="red", size=12),
                    yshift=10
                )

            return fig
        else:
            print("Error: 'All Beneficiaries' not found in extra dataset!")
            return None
    else:
        print("Error: 'All Beneficiaries' not found in main dataset!")
        return None

# Example usage with custom titles:
fig1_2021 = create_hospital_payment_comparison(file_path, chart_title="Hospital Program Payment Comparison")  # Renamed to fig1_2021
fig2_2021 = create_hospital_impact_bubble_chart(file_path, chart_title="Impact of Hospital Size and Affiliation on Costs") # Renamed to fig2_2021
fig3_2021 = create_policy_impact_chart(file_path,extra_file, chart_title="Observable Impacts of Policy Changes Over Time") # Renamed to fig3_2021


# Initialize the Dash app
app = dash.Dash(__name__)

# Set the font for both dashboard title and graph titles to "Open Sans"
font_family = "Open Sans, sans-serif"

# Define the layout of the Dash app
app.layout = html.Div([
    html.H1("Performance and Policy Implications Analysis",
     style={                
                'textAlign': 'center',
                'padding': '20px', 
                'color': 'rgb(57, 105, 172)', 
                'font-family': font_family  # Set font family here
            }),
    dcc.Graph(figure=fig1_2021, config={'displayModeBar': False}),
    dcc.Graph(figure=fig2_2021, config={'displayModeBar': False}),
    dcc.Graph(figure=fig3_2021, config={'displayModeBar': False})
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)





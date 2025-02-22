import pandas as pd
import plotly.express as px
import us
import dash
from dash import dcc, html
import streamlit as st

def create_admissions_line_chart(file_path, chart_title="Trend in Hospital Admissions Over the Years"):
    """Creates and returns a line chart of hospital admissions over time."""

    df_1 = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 1", header=4)
    df_1 = df_1.dropna(axis=1, how="all")

    df_1.columns = ["Type of Entitlement and Calendar Year", "Total Original Medicare Part A Enrollees", 
                    "Total Persons With Utilization"] + [f"Unnamed_{i}" for i in range(len(df_1.columns)-3)]

    df_1 = df_1.dropna(how="all")

    all_beneficiaries_index = df_1[df_1["Type of Entitlement and Calendar Year"] == "All Beneficiaries"].index

    if not all_beneficiaries_index.empty:
        start_index = all_beneficiaries_index[0] + 1
        df_1_all_beneficiaries = df_1.iloc[start_index:start_index + 6]

        df_1_all_beneficiaries["Year"] = pd.to_numeric(df_1_all_beneficiaries["Type of Entitlement and Calendar Year"], errors='coerce')

        df_1_all_beneficiaries.dropna(subset=["Year", "Total Persons With Utilization"], inplace=True)

        df_1_all_beneficiaries["Year"] = df_1_all_beneficiaries["Year"].astype(int)

        fig1 = px.line(df_1_all_beneficiaries, 
                      x="Year", 
                      y="Total Persons With Utilization", 
                      markers=True,  
                      title=chart_title,
                      labels={"Year": "Year", "Total Persons With Utilization": "Number of Admissions"})
        fig1.update_traces(line=dict(color="rgb(57, 105, 172)"))
        return fig1
    else:
        print("Error: 'All Beneficiaries' not found in dataset!")
        return None


def create_utilization_choropleth_map(file_path, map_title="Geographical Utilization Rates Across States"):
    """Creates and returns a choropleth map of utilization rates."""

    df_3 = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 3", header=3)

    df_3.rename(columns={"Area of Residence": "State", "Total Persons With Utilization": "Utilization Rate"}, inplace=True)

    df_3["Utilization Rate"] = df_3["Utilization Rate"].astype(str).str.replace(",", "", regex=False)
    df_3["Utilization Rate"] = pd.to_numeric(df_3["Utilization Rate"], errors="coerce")

    df_3["State"] = df_3["State"].str.strip()

    def get_state_abbrev(state_name):
        if isinstance(state_name, str):
            try:
                state = us.states.lookup(state_name)
                return state.abbr if state else None
            except Exception as e:
                print(f"Error looking up state: {state_name}. Error: {e}")
                return None
        return None

    df_3["State Abbrev"] = df_3["State"].apply(get_state_abbrev)

    exclude_values = [
        "BLANK", "All Areas", "United States", "NOTES:", "SOURCE:", "Territories, Possessions, and Other",
        "Puerto Rico", "Virgin Islands", "American Samoa", "Guam", "Northern Mariana Islands", "Foreign Countries", "Unknown",
        None
    ]

    df_3.dropna(subset=["State Abbrev", "Utilization Rate"], inplace=True)
    df_3 = df_3.loc[~df_3["State Abbrev"].isin(exclude_values)]

    fig2 = px.choropleth(df_3,
                        locations="State Abbrev",
                        locationmode="USA-states",
                        color="Utilization Rate",
                        hover_data=["Utilization Rate", "State"],
                        color_continuous_scale="Blues",
                        scope="usa",
                        title=map_title)
    return fig2


def create_normalized_stacked_bar_chart(file_path, chart_title="Medicare Utilization by Demographic Categories (100% Stacked)"):
    """Creates and returns a 100% stacked bar chart of normalized utilization data."""
    df2 = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 2", header=4, usecols=[0, 1, 2], dtype=str)

    # Rename columns
    df2.columns = ["Demographic Group", "Total Enrollees", "Total With Utilization"]

    # Convert numeric columns (removing dots which might be thousand separators)
    df2["Total Enrollees"] = pd.to_numeric(df2["Total Enrollees"].str.replace('.', '', regex=False), errors='coerce')
    df2["Total With Utilization"] = pd.to_numeric(df2["Total With Utilization"].str.replace('.', '', regex=False), errors='coerce')

    # Drop rows with missing values in key columns
    df2 = df2.dropna(subset=["Total Enrollees", "Total With Utilization"])

    # Function to classify demographic groups into broader categories
    def categorize_group(group):
        if "Years" in group or "Under" in group or "Over" in group:
            return "Age"
        elif group in ["Male", "Female"]:
            return "Sex"
        elif group in ["Non-Hispanic White", "Black (or African-American)", "Asian/Pacific Islander", 
                       "Hispanic", "American Indian/Alaska Native", "Other"]:
            return "Race"
        elif "MME" in group or "Non-MME" in group:
            return "Medicare-Medicaid Enrollment (MME) Status"
        return None  # Exclude irrelevant rows

    # Apply categorization function
    df2["Subcategory"] = df2["Demographic Group"].apply(categorize_group)

    # Filter to keep only the relevant categories
    df2 = df2[df2["Subcategory"].notna()]

    # Calculate the utilization rate
    df2["Utilization Rate (%)"] = (df2["Total With Utilization"] / df2["Total Enrollees"]) * 100

    # **Normalize each demographic category to sum to 100%**
    df2["Normalized Utilization (%)"] = df2.groupby("Subcategory")["Utilization Rate (%)"].transform(lambda x: (x / x.sum()) * 100)

    # Stacked Bar Chart for Normalized Data
    fig3 = px.bar(df2, 
                 x="Subcategory",  # Main categories (Age, Sex, Race, MME Status)
                 y="Normalized Utilization (%)",  # Normalized to sum to 100%
                 color="Demographic Group",  # Stacking by demographic subcategories
                 title=chart_title,
                 labels={"Normalized Utilization (%)": "Utilization Rate (%)", "Subcategory": "Demographic Category"},
                 barmode="stack",
                      color_discrete_sequence=[
                 "rgb(57, 105, 172)",  # Deep blue
                 "rgb(0, 158, 115)",   # Vibrant teal-green
                 "rgb(244, 165, 35)",  # Bright orange
                 "rgb(214, 89, 99)",   # Soft red
                 "rgb(133, 190, 95)",  # Muted green
                 "rgb(255, 128, 52)"   # Warm orange
             ]
)
# Adjust layout to fix title, legend, and positioning
    fig3.update_layout(
        legend=dict(
            orientation="v",  # Vertical layout
            yanchor="top",  # Position the top of the legend at the top of the chart
            y=1,  # Position the legend at the top of the chart
            xanchor="left",  # Position the left of the legend at the right side
            x=1.05,  # Move the legend to the right of the chart
            itemsizing='constant',  # Keeps the legend items uniform in size
            traceorder='normal'  # Keeps the trace order as is
    ),
        margin=dict(t=100, b=50, l=50, r=100)  # Add margin to the right for the legend
)

    return fig3


def create_hospital_type_bar_chart(file_path, chart_title="Utilization Rates by Hospital Type"):
    """Creates and returns a bar chart comparing utilization rates by hospital type."""

    df_hosp = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 4", header=3, usecols=[0, 1, 2], dtype=str)

    # Rename columns for clarity (adjust names based on actual data)
    df_hosp.columns = ["Hospital Type", "Total Enrollees", "Total Persons With Utilization"]

    # Convert numeric columns, handling errors
    df_hosp["Total Enrollees"] = pd.to_numeric(df_hosp["Total Enrollees"].str.replace('.', '', regex=False), errors='coerce')
    df_hosp["Total Persons With Utilization"] = pd.to_numeric(df_hosp["Total Persons With Utilization"].str.replace('.', '', regex=False), errors='coerce')

    # Drop rows with missing values
    df_hosp = df_hosp.dropna(subset=["Total Enrollees", "Total Persons With Utilization"])

    # Calculate utilization percentage
    df_hosp["Utilization Rate (%)"] = (df_hosp["Total Enrollees"] / df_hosp["Total Persons With Utilization"]) * 100

    # Create a bar chart with a colorblind-friendly palette
    fig4 = px.bar(df_hosp,
                 x="Hospital Type",
                 y="Utilization Rate (%)",
                 title=chart_title,
                 labels={"Utilization Rate (%)": "Utilization Percentage"},
                 color="Hospital Type",  # Color by Hospital Type
                 color_discrete_sequence=["rgb(57, 105, 172)"])  # Colorblind-friendly palette
    # Hide the legend to reduce extra space
    fig4.update_layout(showlegend=False)
    return fig4


def create_payment_line_chart(file_path, chart_title="Trend in Program Payments Over the Years"):
    """Creates and returns a line chart of program payments over time."""

    df_1 = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 1", header=3)
    df_1 = df_1.dropna(axis=1, how="all")
    print(df_1.head(10))

    # 1. Identify the "All Beneficiaries" row and get the subsequent rows
    all_beneficiaries_index = df_1[df_1["Type of Entitlement and Calendar Year"] == "All Beneficiaries"].index

    if not all_beneficiaries_index.empty:
        start_index = all_beneficiaries_index[0] + 1
        df_1_all_beneficiaries = df_1.iloc[start_index:start_index + 6].copy()

        # 2. Extract Year as numeric values
        df_1_all_beneficiaries["Year"] = pd.to_numeric(df_1_all_beneficiaries["Type of Entitlement and Calendar Year"], errors='coerce')

        # 3. Drop rows with missing Year or Total Program Payments
        df_1_all_beneficiaries.dropna(subset=["Year", "Total Program Payments"], inplace=True)

        # 4. Convert Year to integer for proper x-axis handling
        df_1_all_beneficiaries["Year"] = df_1_all_beneficiaries["Year"].astype(int)

        # 5. Identify the Program Payments column and clean it
        program_payments_column = next((col for col in df_1.columns if "Total Program Payments" in col), None)

        if program_payments_column:
            df_1_all_beneficiaries[program_payments_column] = pd.to_numeric(df_1_all_beneficiaries[program_payments_column], errors='coerce')

            # 6. Create the line chart
            fig5 = px.line(df_1_all_beneficiaries,
                          x="Year",
                          y=program_payments_column,
                          markers=True,
                          title=chart_title,
                          labels={"Year": "Year", program_payments_column: "Total Program Payments ($)"})
            fig5.update_traces(line=dict(color="rgb(57, 105, 172)"))
            return fig5
        else:
            print("Error: 'Program Payments' column not found.")
            return None
    else:
        print("Error: 'All Beneficiaries' data not found.")
        return None


# Main part of your script:
file_path = "https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/raw/main/database/CPS%20MDCR%20INPT%202021.xlsx"

# Example usage with custom titles:
fig1_2021 = create_admissions_line_chart(file_path, chart_title="Trend in Hospital Admissions Over the Years")  # Renamed to fig1_2021
fig2_2021 = create_utilization_choropleth_map(file_path, map_title="Geographical Utilization Rates Across States") # Renamed to fig2_2021
fig3_2021 = create_normalized_stacked_bar_chart(file_path, chart_title="Medicare Utilization by Demographic Categories)") # Renamed to fig3_2021
fig4_2021 = create_hospital_type_bar_chart(file_path, chart_title="Utilization Rates by Hospital Type") 
fig5_2021 = create_payment_line_chart(file_path, chart_title="Trend in Program Payments Over the Years")

# Define a function to return the layout
def layout():
    font_family = "Open Sans, sans-serif"

    return html.Div([
        html.H1("Utilization and Access Analysis",
            style={                
                'textAlign': 'center',
                'padding': '20px', 
                'color': 'rgb(57, 105, 172)', 
                'font-family': font_family  # Set font family here
            }),
        dcc.Graph(figure=fig1_2021, config={'displayModeBar': False}),
        dcc.Graph(figure=fig2_2021, config={'displayModeBar': False}),
        dcc.Graph(figure=fig3_2021, config={'displayModeBar': False}),
        dcc.Graph(figure=fig4_2021, config={'displayModeBar': False}),
        dcc.Graph(figure=fig5_2021, config={'displayModeBar': False})
    ])




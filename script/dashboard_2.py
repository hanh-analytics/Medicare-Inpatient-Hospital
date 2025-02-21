import pandas as pd
import plotly.express as px
import us
import dash
from dash import dcc, html

file_path = "/Users/DELL/Desktop/Projects/CMS Program Statistics - Medicare Inpatient Hospital/2021/CPS MDCR INPT 2021.xlsx"

# 1. Cost-sharing bar chart
def create_cost_sharing_bar_chart(file_path, chart_title="Average Cost-Sharing by Patient Category"):  
    # Read the data from the sheet containing relevant columns
    df2 = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 2", header=4, usecols=[0, 1, 2, 3, 4, 5, 6, 7], dtype=str)
    
    # Rename columns for clarity
    df2.columns = [
        "Demographic Group", "Total Enrollees", "Total With Utilization", "Total Discharges", 
        "Total Days of Care", "Total Program Payments", "Total Deductible Payments", "Total Coinsurance Payments"
    ]
    
    # Convert numeric columns to proper data types (removing dots for thousands separators)
    df2["Total Enrollees"] = pd.to_numeric(df2["Total Enrollees"].str.replace('.', '', regex=False), errors='coerce')
    df2["Total With Utilization"] = pd.to_numeric(df2["Total With Utilization"].str.replace('.', '', regex=False), errors='coerce')
    df2["Total Discharges"] = pd.to_numeric(df2["Total Discharges"].str.replace('.', '', regex=False), errors='coerce')
    df2["Total Days of Care"] = pd.to_numeric(df2["Total Days of Care"].str.replace('.', '', regex=False), errors='coerce')
    df2["Total Program Payments"] = pd.to_numeric(df2["Total Program Payments"].str.replace('.', '', regex=False), errors='coerce')
    df2["Total Deductible Payments"] = pd.to_numeric(df2["Total Deductible Payments"].str.replace('.', '', regex=False), errors='coerce')
    df2["Total Coinsurance Payments"] = pd.to_numeric(df2["Total Coinsurance Payments"].str.replace('.', '', regex=False), errors='coerce')
    
    # Drop rows with missing values in key columns
    df2 = df2.dropna(subset=["Total Enrollees", "Total With Utilization", "Total Discharges", "Total Program Payments"])
    
    # Function to categorize demographic groups
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
    
    # Calculate total cost-sharing (deductibles + coinsurance)
    df2["Total Cost-Sharing"] = df2["Total Deductible Payments"] + df2["Total Coinsurance Payments"]
    
    # Define custom order for the categories
    age_order = [
        "Under 18 Years", "18-24 Years", "25-34 Years", "35-44 Years", "45-54 Years", "55-64 Years", 
        "65-74 Years", "75-84 Years", "85-94 Years", "95 Years and Over"
    ]
     
    # Plot the bar chart manually (without using Plotly Express function)
    fig1 = px.bar(df2, x="Demographic Group", y="Total Cost-Sharing", color="Subcategory", 
                 title=chart_title, 
                 category_orders={"Subcategory": ["Age", "Sex", "Race", "Medicare-Medicaid Enrollment (MME) Status"]}, 
                 color_discrete_sequence=["rgb(57, 105, 172)", "rgb(0, 158, 115)", "rgb(244, 165, 35)", "rgb(214, 89, 99)"])
    
    return fig1


# 2. Stacked bar chart for spending differences in different hospital types
def create_spending_clustered_bar_chart(file_path, chart_title="Spending Differences by Hospital Type"):
    """Creates a clustered bar chart showing spending differences across hospital types."""
    
    # Load the data
    df = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 4", header=3)  # Adjust worksheet name if needed
    
    # Rename relevant columns
    df.rename(columns={
        "Type of Hospital": "Hospital Type", 
        "Total Program Payments": "Program Payments ($)", 
        "Total Deductible Payments": "Deductible Payments ($)", 
        "Total Coinsurance Payments": "Coinsurance Payments ($)"
    }, inplace=True)

    # Convert spending columns to numeric (handling commas if needed)
    for col in ["Program Payments ($)", "Deductible Payments ($)", "Coinsurance Payments ($)"]:
        df[col] = df[col].astype(str).str.replace(",", "", regex=False)
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    # Drop rows with missing values
    df.dropna(subset=["Hospital Type", "Program Payments ($)", "Deductible Payments ($)", "Coinsurance Payments ($)"], inplace=True)
    
    # Transform data to long format for clustering
    df_melted = df.melt(id_vars=["Hospital Type"], 
                         value_vars=["Program Payments ($)", "Deductible Payments ($)", "Coinsurance Payments ($)"], 
                         var_name="Spending Type", 
                         value_name="Amount ($)")

    # Create the clustered bar chart
    fig2 = px.bar(df_melted, 
                 x="Hospital Type", 
                 y="Amount ($)", 
                 color="Spending Type", 
                 title= "Spending Differences by Hospital Type", 
                 labels={"Amount ($)": "Spending ($)", "Hospital Type": "Hospital Type"}, 
                 barmode="group",  # Ensures clustering instead of stacking
                 color_discrete_sequence= ["rgb(57, 105, 172)", "rgb(0, 158, 115)", "rgb(244, 165, 35)"])

    # Apply logarithmic scale to the Y-axis
    fig2.update_layout(
        yaxis_type="log",  # Set the y-axis to logarithmic scale
        title="Spending Differences by Hospital Type"
    )
    return fig2


# 3. Strip plot comparing program payments across demographic groups
def create_strip_plot_dashboard(file_path, title="Program Payments by Demographic Group"):
    """Creates a strip plot comparing program payments across demographic groups using Plotly."""
    
    # Load the data
    df = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 2", header=4, dtype=str)

    # Exclude 'Total' and 'Unknown' rows
    df = df[~df.iloc[:, 0].isin(["Under 65 Years", "65 Years and Over"])]  # Assuming first column is "Demographic Group"

    # Rename only relevant columns
    df.rename(columns={
        df.columns[0]: "Demographic Group",
        df.columns[15]: "Total Program Payments"
    }, inplace=True)

    # Convert program payments to numeric
    df["Total Program Payments"] = df["Total Program Payments"].astype(str).str.replace(",", "", regex=False)
    df["Total Program Payments"] = pd.to_numeric(df["Total Program Payments"], errors="coerce")

    # Map subcategories to main categories
    category_map = {
        "Under 18 Years": "Age", "18-24 Years": "Age", "25-34 Years": "Age",
        "35-44 Years": "Age", "45-54 Years": "Age", "55-64 Years": "Age",
        "65-74 Years": "Age", "75-84 Years": "Age", "85-94 Years": "Age", "95 Years and Over": "Age",
        "Male": "Sex", "Female": "Sex",
        "Non-Hispanic White": "Race", "Black (or African-American)": "Race",
        "Asian/Pacific Islander": "Race", "Hispanic": "Race",
        "American Indian/Alaska Native": "Race", "Other": "Race",
        "MME": "MME Status", "Non-MME": "MME Status"
    }

    # Apply mapping
    df["Main Category"] = df["Demographic Group"].map(category_map)

    # Drop any row where the category mapping failed
    df.dropna(subset=["Main Category"], inplace=True)

    # Create the strip plot using Plotly
    fig3 = px.scatter(df, 
                     x="Main Category", 
                     y="Total Program Payments", 
                     color="Main Category",  # Color by Main Category
                     title=title,
                     labels={"Total Program Payments": "Program Payments ($)", "Main Category": "Demographic Group"},
                     category_orders={"Main Category": [
                         "Age", "Sex", "Race", "MME Status"
                     ]},
                     opacity=0.6,  # Slight transparency to reduce overlap
                     hover_data={"Demographic Group": True, "Total Program Payments": True} # Show Demographic Group on hover
                    )

    fig3.update_traces(marker=dict(symbol="circle", size=6))  # Set marker properties
    fig3.update_layout(
        xaxis_title="Demographic Group", 
        yaxis_title="Program Payments ($)", 
        xaxis_tickangle=45,
        showlegend=False  # Hide legend to reduce clutter
    )

    return fig3 

# Call the function
create_strip_plot_dashboard(file_path)

# 4. Choropleth map of program payments per discharge
def create_program_payments_choropleth_map(file_path, map_title="Geographical Program Payments Per Discharge Across States"):
    """Creates and returns a choropleth map of program payments per discharge."""

    # Load the data from the relevant sheet
    df_3 = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 3", header=3)
    
    # Rename columns for clarity
    df_3.rename(columns={
        "Area of Residence": "State", 
        "Program Payments Per Discharge": "Program Payments Per Discharge"
    }, inplace=True)
    
    # Convert the 'Program Payments Per Discharge' column to numeric (handling commas if needed)
    df_3["Program Payments Per Discharge"] = df_3["Program Payments Per Discharge"].astype(str).str.replace(",", "", regex=False)
    df_3["Program Payments Per Discharge"] = pd.to_numeric(df_3["Program Payments Per Discharge"], errors="coerce")
    
    # Clean up state names and abbreviations
    df_3["State"] = df_3["State"].str.strip()
    
    # Function to get state abbreviations
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

    # Exclude unnecessary rows
    exclude_values = [
        "BLANK", "All Areas", "United States", "NOTES:", "SOURCE:", "Territories, Possessions, and Other",
        "Puerto Rico", "Virgin Islands", "American Samoa", "Guam", "Northern Mariana Islands", "Foreign Countries", "Unknown",
        None
    ]
    df_3.dropna(subset=["State Abbrev", "Program Payments Per Discharge"], inplace=True)
    df_3 = df_3.loc[~df_3["State Abbrev"].isin(exclude_values)]
    
    # Create the choropleth map
    fig4 = px.choropleth(df_3,
                        locations="State Abbrev",
                        locationmode="USA-states",
                        color="Program Payments Per Discharge",
                        hover_data=["Program Payments Per Discharge", "State"],
                        color_continuous_scale="Blues",  # Choose an appropriate color scale
                        scope="usa",
                        title=map_title)
    
    return fig4




#5. Bar chart comparing health outcomes (Discharged Dead) across hospital types
def create_health_outcomes_bar_chart(file_path, title="Health Outcomes by Hospital Type"):
    """Creates a bar chart comparing health outcomes (Discharged Dead) across hospital types."""
    
    # Load data
    df = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 4", header=3)
    
    # Rename relevant columns
    df.rename(columns={"Type of Hospital": "Hospital Type", "Discharged Dead": "Health Outcome"}, inplace=True)
    
    # Convert health outcome column to numeric
    df["Health Outcome"] = pd.to_numeric(df["Health Outcome"], errors="coerce")
    
    # Drop rows with missing values
    df.dropna(subset=["Hospital Type", "Health Outcome"], inplace=True)
    
    # Filter out "Other Hospitals"
    df = df[df["Hospital Type"] != "Other Hospitals"]
    
    # Group by hospital type and calculate the mean of health outcomes (Discharged Dead)
    df_grouped = df.groupby("Hospital Type")["Health Outcome"].mean().reset_index()
    
    # Ensure all hospitals with data are represented, even those with very small values
    df_grouped = df_grouped[df_grouped["Health Outcome"].notna()]

    # Create bar chart with custom color
    fig5 = px.bar(df_grouped, 
                 x="Hospital Type", 
                 y="Health Outcome", 
                 title=title, 
                 labels={"Health Outcome": "Average Discharged Dead", "Hospital Type": "Hospital Type"},
                 color="Hospital Type",  # To differentiate the hospital types
                 category_orders={"Hospital Type": [
                     "Short-Stay Hospitals", "Critical Access Hospitals", "Long Term Care Hospitals", 
                     "Inpatient Psychiatric Facilities", "Inpatient Rehabilitation Facilities", 
                     "Religious Nonmedical Health Care Institutions", "Childrens' Hospitals"
                 ]},
                 color_discrete_sequence=["rgb(57, 105, 172)"])  # Deep blue color for all bars
    
    fig5.update_layout(xaxis_title="Hospital Type", yaxis_title="Average Discharged Dead", showlegend=False)
    
    # Adjust layout to better display small values
    fig5.update_traces(marker=dict(line=dict(width=0)))  # Remove borders around bars

    return fig5



# Example usage with custom titles:
fig1_2021 = create_cost_sharing_bar_chart(file_path, chart_title="Average Cost-Sharing by Patient Category")

fig2_2021 = create_spending_clustered_bar_chart(file_path, chart_title="Geographical Utilization Rates Across States") # Renamed to fig2_2021

fig3_2021 = create_strip_plot_dashboard(file_path, title="Program Payments by Demographic Group") # Renamed to fig3_2021

fig4_2021 = create_program_payments_choropleth_map(file_path, map_title="Geographical Program Payments Per Discharge Across States")

fig5_2021 = create_health_outcomes_bar_chart(file_path, title="Health Outcomes by Hospital Type")

# Check if figures are properly created
assert fig1_2021 is not None, "fig1_2021 is null"
assert fig2_2021 is not None, "fig2_2021 is null"
assert fig3_2021 is not None, "fig3_2021 is null"
assert fig4_2021 is not None, "fig4_2021 is null"
assert fig5_2021 is not None, "fig5_2021 is null"

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the font for both dashboard title and graph titles to "Open Sans"
font_family = "Open Sans, sans-serif"

# Define the layout of the Dash app
app.layout = html.Div([
    html.H1("Finance & Equity Analysis",
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

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)


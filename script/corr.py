import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
file_path = "/Users/DELL/Desktop/Projects/CMS Program Statistics - Medicare Inpatient Hospital/2021/CPS MDCR INPT 2021.xlsx"
    # Read the data from the sheet containing relevant columns
df2 = pd.read_excel(file_path, sheet_name="MDCR INPT HOSP 2", header=4, usecols=[0, 15, 21, 22], dtype=str)
    
    # Rename columns for clarity
df2.columns = [
        "Demographic Group", "Total Program Payments", "Total Deductible Payments", "Total Coinsurance Payments"
    ]
    
    # Convert numeric columns to proper data types (removing dots for thousands separators)
df2["Total Program Payments"] = pd.to_numeric(df2["Total Program Payments"].str.replace('.', '', regex=False), errors='coerce')
df2["Total Deductible Payments"] = pd.to_numeric(df2["Total Deductible Payments"].str.replace('.', '', regex=False), errors='coerce')
df2["Total Coinsurance Payments"] = pd.to_numeric(df2["Total Coinsurance Payments"].str.replace('.', '', regex=False), errors='coerce')
    
    # Drop rows with missing values in key columns
df2 = df2.dropna(subset=["Demographic Group", "Total Program Payments", "Total Deductible Payments", "Total Coinsurance Payments"])
    
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
        
# Compute correlation
corr, p_value = pearsonr(df2["Total Program Payments"], df2["Total Cost-Sharing"])
print(f"Pearson Correlation: {corr:.2f}, P-value: {p_value:.4f}")

# Visualize relationship
sns.scatterplot(x=df2["Total Program Payments"], y=df2["Total Cost-Sharing"])
plt.title("Correlation Between Program Payment and Cost Sharing")
plt.show()



    


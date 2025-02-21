# Dataset  

This folder contains Medicare inpatient hospital data used for analysis, visualization, and predictive modeling. The dataset includes information on hospital discharges, program payments, cost-sharing, and utilization trends across different demographic and geographic factors.  

## Files  

- **CPS MDCR INPT 2021.xlsx** - Primary dataset used for analysis, focusing on Medicare inpatient hospital data for the year 2021.  
- **CPS MDCR INPT 2020.xlsx** - Dataset used to extract historical data for the year 2015 to analyze trends over time.  

## Data Overview  

Each file contains structured data on:  
- **Discharges** - Number of inpatient hospital discharges.  
- **Program Payments** - Medicare payments for hospital services.  
- **Cost Sharing** - Out-of-pocket costs for beneficiaries.  
- **Hospital Types** - Various hospital classifications.  
- **Demographics** - Breakdown by age, gender, and other factors.  
- **Geographic Regions** - Regional distribution of Medicare utilization.  

## Usage  

These datasets are used for:  
- Analyzing trends in hospital efficiency and program payments.  
- Predicting future utilization and cost-sharing patterns.  
- Comparing demographic groups facing higher program costs.  
- Interactive dashboard visualizations.  

## Source  

The data is sourced from **CMS Program Statistics - Medicare Inpatient Hospital** reports.  

## Preprocessing  

Before analysis, the data undergoes:  
- **Cleaning** - Removing inconsistencies, formatting column names.  
- **Year Extraction** - Adjusting the `Year` column to ensure consistency.  
- **Merging** - Combining 2015 data from the 2020 file with 2021 data for trend comparisons.  

## Notes  

- Ensure the correct file path is set when running scripts.  
- The `CPS MDCR INPT 2020.xlsx` file is only used to extract 2015 data.  
- Data integrity checks should be performed before each analysis.  


# Medicare-Inpatient-Hospital
This repository contains code and tools for analyzing healthcare data, building interactive dashboards, and performing statistical analysis. The project focuses on Medicare inpatient hospital data and its implications on program utilization, payments, and healthcare policies. Key components of the project include:

## 1. Dashboards: 

Interactive visualizations built with Plotly and Dash to display healthcare trends and comparisons across hospital types, regions, and time periods. The dashboards provide insights into utilization patterns, program payments, cost-sharing variations, and demographic disparities in Medicare inpatient hospital data.

### Key Dashboards:
- 📊 Utilization & Access Analysis (dashboard1.py)

  - Tracks hospital admissions trends over time.

  - Compares inpatient hospital utilization across geographic regions.

  - Analyzes disparities in hospital utilization based on demographic factors (age, race, gender).

  - Identifies the most frequently utilized hospital types.
    
- 💰 Finance & Equity Analysis (dashboard2.py)

  - Visualizes changes in program payments for inpatient care over the years.

  - Examines the average cost per hospital stay for different demographic groups.

  - Compares cost-sharing amounts (out-of-pocket costs) across patient categories.

  - Highlights geographic and hospital-type differences in Medicare spending.
  
  - Evaluates disparities in healthcare costs among different population groups.

- 🏥 Hospital Performance & Policy Insights (dashboard3.py)

  - Ranks hospitals based on program payments and efficiency metrics.

  - Assesses how hospital size, type, and affiliation impact patient costs and care quality.

  - Tracks the effects of Medicare policy changes on utilization and costs.

  - Identifies regions and hospitals that could benefit from cost efficiency and equity interventions.
 
  Here’s a section on setting up the dashboard for your `README.md`:

### Dashboard Setup

To set up and run the dashboard, follow these steps:

1. **Clone the repository**:
   First, clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Then, create a virtual environment and install the required libraries:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Load the dataset**:
   Ensure the dataset files are available on your machine. Modify the file paths in the code (if needed) to match the location of your datasets.

4. **Run the dashboard**:
   To start the dashboard, use the following command:
   ```bash
   python app.py
   ```

5. **Access the dashboard**:
   Open your browser and navigate to http://localhost:5000 (or the IP address provided by your environment) to view the dashboard.


## 2. T-Test Analysis: Pre-Policy vs Post-Policy

In this analysis, a **two-sample t-test** was conducted to compare the mean total discharges before (2015–2018) and after (2019–2021) a policy change. The test aimed to assess whether the policy change had a statistically significant impact on hospital discharges. The result indicated **no significant difference** between the two periods, suggesting that the policy change did not meaningfully affect discharge rates. However, factors like the COVID-19 pandemic in 2020 may have influenced the data, warranting further investigation.

3. Predictive Modeling: Development of models to predict hospital efficiency by identifying high-efficiency hospitals based on program payments relative to utilization (i.e., cost per discharge or per day of care). Variables considered include program payments, hospital type, discharges, days of care, hospital size, and region.

The project provides insights into how healthcare policies and interventions affect Medicare utilization and payments, with an emphasis on visual representation for better decision-making.

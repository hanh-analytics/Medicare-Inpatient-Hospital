# 📚 Notebooks Folder

This folder contains Jupyter Notebooks that focus on analyzing Medicare inpatient hospital data through statistical tests and predictive modeling. Below is a description of the notebooks included in this directory.

## Notebooks Overview

### 1. **T-test Analysis (t-test.ipynb)**
This notebook contains the analysis of total discharges before and after a policy change using a **T-test**. The key steps covered in this notebook include:
- Data cleaning and preparation, including handling missing values and categorizing the data by the pre-policy and post-policy periods.
- Performing a **two-sample T-test** to assess whether there is a statistically significant difference in total discharges across the pre-policy and post-policy periods.
- Interpreting the results to evaluate the impact of the policy change on the total discharges.

Key points covered:
- Normality testing using the Shapiro-Wilk test.
- T-test calculations and result interpretation.

### 2. **Predictive Modeling: Hospital Efficiency (model.ipynb)**
This notebook develops **predictive models** to assess hospital efficiency based on Medicare program payments and utilization data. The goal is to identify high-efficiency hospitals by predicting the cost per discharge or cost per day of care.

Key steps:
- Data preparation, cleaning, and feature engineering based on hospital utilization, program payments, discharges, days of care, hospital type, and region.
- Development of different regression models to predict hospital efficiency, including linear regression and other machine learning algorithms.
- Evaluation of model performance through metrics such as R-squared, Mean Absolute Error (MAE), and other statistical tests.

Key points covered:
- Data preprocessing and feature selection.
- Model evaluation and comparison of results.

## How to Use
1. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

2. Open any of the notebooks using Jupyter Notebook or JupyterLab:
   ```bash
   jupyter notebook t-test.ipynb
   jupyter notebook model.ipynb
   ```

3. Follow the instructions within the notebooks to understand the methodology, perform analysis, and generate results.

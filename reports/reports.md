# Healthcare Data Analytics Dashboard Report: Insights on Utilization, Financial Aspects, Equity, and Policy Implications

## 1. Utilization and Access

![barchart](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/e6c24bfa9b2bbb3b09685f1100bd12f761e37a3c/visualizations/hospital_admission_line.png)

- **Trend in Hospital Admissions Over the Years**:

   - Overall, there was a significant decline in hospital admissions from 2016 to 2021. In 2016, the number of admissions was approximately 6.7 million, gradually decreasing to 6.3 million in the following years. A sharp decline of about 1 million admissions occurred in 2020, followed by a continued drop to 5.1 million in 2021.
      
   - The most significant drop occurred in 2020, likely due to the **COVID-19 pandemic**. Many hospitals postponed elective procedures and non-emergency admissions to prioritize COVID-19 patients. Patients also avoided hospitals due to **fear of infection**, leading to a reduction in non-COVID-related hospitalizations.
     
   - The gradual drop in hospital admissions from 2016 to 2019 was likely due to the shift toward outpatient care, value-based payment models reducing the need for inpatient stays.
 
   - Additionally, **home healthcare services, telemedicine, and alternative care models** provided more options outside hospitals.
 
   - Insurance policies and stricter admission criteria may have also contributed to fewer hospitalizations before the sharp decline in 2020 due to COVID-19.

- **Inpatient Hospital Utilization by Geographic Region**:

![map](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/e6c24bfa9b2bbb3b09685f1100bd12f761e37a3c/visualizations/geographic_utilization.png)

   - California had the highest program payments among U.S. states, around **$400,000**, followed by **Florida ($380K)** and **Texas ($352K)**. In the East, states like **New York ($300K), Illinois ($230K), and Pennsylvania ($227K)** had higher payments, while states in the **central U.S., Oregon, and Nevada** had much lower costs (under **$100K**). The **lowest program payments** were observed in **Vermont, New Hampshire, Maine**, and the island states of **Alaska and Hawaii**.

   - Possible explanations for this include:
   
      - The cost of medical services varies by state due to differences in labor costs, hospital charges, and Medicare reimbursement rates.
   
      - States like California, Florida, and Texas have large populations and high numbers of Medicare beneficiaries, leading to greater overall program payments.
    
      - States with more hospitals and higher inpatient utilization (e.g., New York, Pennsylvania) tend to have higher payments.
    
      - States with a higher proportion of elderly residents (e.g., Florida) may have increased **inpatient hospital utilization**, driving up costs.
    
      - States with lower payments (e.g., Vermont, Maine, Alaska, Hawaii) may have **fewer large hospitals, lower utilization rates**, or different state healthcare policies affecting reimbursement.


- **Disparities in Utilization Based on Demographic Characteristics**:

  ![ultilization](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/a50ec41aa7bdf3f8c2e1d8ca3068be2881e11582/visualizations/utilization_demographic.png)
  
   - Medicare utilization was highest among the 75-84 age group, which accounted for the largest proportion of beneficiaries. Surprisingly, younger age groups (18-24 and 25-34) also had notable utilization, likely due to beneficiaries with disabilities or chronic conditions. Other age groups had a more evenly distributed share of Medicare utilization.
     
   - One possible explanation is that the younger age groups are beneficiaries due to disabilities or chronic conditions, while the 75-84 age group has the highest utilization due to age-related health needs.

- **Most Frequently Utilized Types of Hospitals**:

  ![most frequently](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/654fdcaf448ce037dff77591a517a0a407b526ee/visualizations/bar_utilization_hospital_type.png.png)
  
   - Inpatient Rehabilitation Facilities had the highest utilization rate at 89%, followed closely by Long-Term Care Hospitals at 88%. Critical Access Hospitals ranked third with a utilization rate of 81%. Short-Stay Hospitals, Inpatient Psychiatric Facilities, and other hospitals—including Federal Emergency, Veterans Affairs, and foreign hospitals—had utilization rates around 65%, while the overall utilization rate across all hospitals was slightly lower. Religious Nonmedical Health Care Institutions had the lowest utilization rate at 43%, whereas Children's Hospitals had a utilization rate approximately 9% higher.
     
   - There are several possible reasons for the varying utilization rates across different types of hospitals:
     
      - **Inpatient Rehabilitation Facilities (IRFs)** have a high utilization rate because they are specialized in rehabilitation care, which often requires longer stays. Patients needing intensive rehabilitation after surgeries, injuries, or illnesses are more likely to be admitted to IRFs, contributing to the high utilization.
    
      - **Long-Term Care Hospitals (LTCHs)** also have high utilization, as they cater to patients with chronic conditions who require extended hospitalization. These patients often need long-term care due to serious illnesses or injuries, such as those recovering from complex surgeries or requiring ventilation.
    
      - **Critical Access Hospitals (CAHs)**, which are typically located in rural areas, have higher utilization rates because they serve as the primary healthcare providers in regions where access to larger hospitals may be limited.
    
      - **Hospitals like Inpatient Psychiatric Facilities or Short-Stay Hospital**s may have relatively lower utilization because  the duration of stay is often shorter, leading to less overall usage.
    
      - **Children’s Hospitals** typically have lower utilization rates because pediatric patients tend to have shorter stays for more focused treatments, and fewer people in the population require children’s healthcare services compared to adults.
    
      - Hospitals with specialized services, like **Religious Nonmedical Health Care Institutions**, might have lower utilization rates because they often provide less complex care or alternative therapies that might not be as widely needed.
    
      - For certain hospital types, such as **Federal Emergency, Veterans Affairs, and foreign hospitals**, the lower utilization rates may be linked to limited geographic accessibility, eligibility constraints, or specialty care requirements that may not be applicable to the broader population.



## 2. Financial Aspects

- **Program Payments for Inpatient Care Over Time**:

![line](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/654fdcaf448ce037dff77591a517a0a407b526ee/visualizations/payment_line.png)

   - The total program payments in 2016 were $133.5 billion, with a gradual increase to $138.5 billion over the next three years. However, in 2020, there was a sharp decline of approximately $9 billion, before a slight recovery to $131 billion in 2021.
      
   - The sharp decline in Medicare program payments in 2020 can primarily be attributed to the **COVID-19 pandemic**. The pandemic led to widespread disruptions in healthcare services, including hospital admissions, elective surgeries, and outpatient care.
     
   - Additionally, in response to the pandemic, there were changes in healthcare delivery, such as the expansion of telehealth services, which likely contributed to reduced program payments for traditional in-person services.

   - The subsequent recovery in 2021 suggests a partial return to normal healthcare utilization and spending as the healthcare system adapted to the ongoing crisis.

- **Average Cost Per Hospital Stay for Different Demographic Groups**:

![average](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/654fdcaf448ce037dff77591a517a0a407b526ee/visualizations/Cost_sharing_bar_chart.png)

 - **Age**
   
   - The average cost-sharing was highest for the age group 65 years and over, reaching $45 million. Specifically, the age groups 65-74 and 75-84 had average cost-sharing amounts exceeding $15 million each.

   - In contrast, average cost-sharing for individuals under 65 was significantly lower, at only $12 million. Within this group, all specific age breakdowns were below $10 million.

   - The disparity in average cost-sharing between age groups could be attributed to several factors:
      -    Older adults, especially those aged 65 and over, generally have higher healthcare utilization due to chronic conditions, multiple comorbidities, and age-related health issues that require more frequent hospital visits, treatments, and medications.
    
      -    Medicare, which covers individuals aged 65 and over, provides more comprehensive coverage for older adults. However, the coverage comes with higher out-of-pocket costs (such as copayments, deductibles, and coinsurance), which could contribute to higher cost-sharing amounts for this group.
    
 - **Sex**
    -  Equal average cost-sharing for both genders could be due to **Medicare Standardized Cost Structure**.
    
    -  Since Medicare determines cost-sharing amounts based on standardized policies rather than gender, copayments, deductibles, and coinsurance rates are the same for all beneficiaries, leading to similar cost-sharing averages.

   - **Race**:

      -  Non-Hispanic White beneficiaries accounted for the highest cost-sharing, at nearly $40M, followed by Black Americans, whose cost-sharing was significantly lower by approximately $30M. Other racial groups had an average cost-sharing of less than $5M.
    
      -  Possible reasons:
        
         - Non-Hispanic White individuals may have higher hospitalization rates due to a larger elderly population, increased access to inpatient care, or a greater prevalence of conditions requiring hospitalization.
       
         - Black Americans and other racial groups may face barriers to healthcare access, such as lower hospitalization rates due to financial constraints, geographic disparities, or systemic inequities in healthcare delivery.
       
         - Variations in supplemental insurance coverage (such as Medigap or employer-sponsored plans) may influence out-of-pocket cost-sharing amounts across different racial groups.

   - **Medicare Mediaid Enrollment (MME) Status**
  
      - The average cost-sharing for non-MME (Medicare-Medicaid Eligible) beneficiaries was nearly $35M, which was $17M higher than that of MME beneficiaries.
        
      - Possible explanations:
         -   MME beneficiaries qualify for both Medicare and Medicaid, which helps cover out-of-pocket expenses such as copayments, deductibles, and coinsurance, leading to lower cost-sharing.
       
         -   Individuals with MME status often have lower incomes and receive additional financial support through Medicaid, which further reduces their direct healthcare costs.
       
         -   Non-MME beneficiaries may rely on other forms of insurance or pay more out-of-pocket due to fewer financial assistance programs, increasing their total cost-sharing amount. 
  
- **Variations in Cost-Sharing Amounts by Patient Category**:

  ![varications](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/557bbe64f870b86bf59ee9a59a6e42cac5a04c78/visualizations/Spending_Difference_Hospital_type.png)
  
   - Overall, program payments were higher than both deductible and coinsurance payments across all hospital types. Short-stay hospitals had the highest values across all three payment categories compared to other hospital types.

   - **Program Payments**: Short-stay hospitals received the highest program payments. Critical Access Hospitals, Long-Term Care Hospitals, Inpatient Psychiatric Facilities, and Inpatient Rehabilitation Facilities had slightly lower but relatively evenly distributed program payments. Religious Nonmedical Health Care Institutions had the lowest program payments.

   - **Deductible & Coinsurance Payments**: Most hospital types had higher deductible payments than coinsurance payments, except for Long-Term Care Hospitals and Religious Nonmedical Health Care Institutions, where coinsurance payments were higher.
 
   - Possible reasons:
 
      - Short-stay hospitals handle the majority of inpatient admissions, leading to higher overall program payments. They cater to acute conditions requiring shorter hospital stays, making them the most frequently used hospital type.
    
      - In contrast, Critical Access Hospitals, Long-Term Care Hospitals, and other specialty hospitals serve specific patient populations, often with lower patient volumes, leading to relatively lower program payments.
    
      - Deductible payments are higher for most hospitals because they are charged at the start of a hospital stay, while coinsurance costs accumulate only after a certain number of days, affecting hospital types with longer average stays differently.
    
      -  Medicare covers most inpatient costs, but patient cost-sharing varies. Deductibles are typically charged per benefit period, while coinsurance applies to extended stays. Long-Term Care Hospitals often involve longer stays, resulting in higher coinsurance payments.


- **Geographic Differences in Medicare Spending**:
  ![geo](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/557bbe64f870b86bf59ee9a59a6e42cac5a04c78/visualizations/Choropleth_map_program_payments_per_discharge.png)
  
   - Overall, program payments per discharge across all states were above $12K. Alaska had the highest payments per discharge at $22K, followed by Maryland and California, both approximately $2K lower than Alaska.
     
   - States like Alaska and California have significantly higher healthcare costs due to **higher wages for healthcare workers, higher operational costs, and limited provider availability** in certain regions.
     
   - States with a high cost of living (e.g., California and Alaska) generally have **higher reimbursement rates**, driving up program payments per discharge.
 
   - Maryland operates under an **All-Payer Model**, which affects how hospitals are reimbursed, potentially leading to higher payments per discharge.
 
    - There is partial correlation between high program payments per discharge and total program payments:
      
      - California had the highest total program payments (~$400K), but its payments per discharge ($20K) were slightly lower than Alaska’s ($22K). This suggests that while California had a **high volume of inpatient admissions**, its payments per discharge were not the highest.
    
      - Alaska had the highest payments per discharge but one of the lowest total program payments. This suggests lower patient volume but higher costs per case, likely due to **limited hospital access, higher healthcare costs, and geographic challenges**.
    
      - Lower-cost states (e.g., central U.S., Oregon, Nevada) also had lower total program payments, indicating lower utilization and possibly lower costs per case.
    
   - **Summary**: While high total program payments can be driven by both high patient volume and high per-discharge costs, some states (e.g., Alaska) show that high per-discharge costs do not always translate to the highest total program payments due to lower utilization.


## 3. Equity and Disparities

- **Demographic Groups Facing Higher Program Payments or Out-of-Pocket Costs**:

![demo](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/2b2c0bde79b3db9cd2c8a6839936b4daf3656ff6/visualizations/stripplot.png)

   - **Age**
   
   - Program payments were highest for the older age groups, particularly 65-74 and 75-84. The 65-74 age group had the highest program payments at $46B, followed by the 75-84 group at $40B. The 85-94 age group ranked third, with payments around $19B. In contrast, all age groups under 65 had program payments below $20B. 

   - Possible reasons for this trend:
      -    As people age, they are more likely to require hospitalization, surgeries, chronic disease management, and specialized care, leading to higher program payments.
    
      -   Conditions like heart disease, diabetes, and respiratory disorders are more common in older populations, leading to more frequent hospital admissions and longer hospital stays.
    
      -   Younger individuals generally have fewer chronic conditions and may have alternative insurance options (e.g., employer-sponsored plans, Medicaid), leading to lower Medicare program payments.
    
 - **Sex**
   
    -   Both genders had similar program payments, around $65B, **with males receiving slightly higher payments than females**.
    
    -   Men generally experience higher rates of certain chronic conditions (e.g., heart disease, hypertension, and diabetes), leading to increased hospitalizations and medical costs.
  
    -   Some medical procedures and treatments (e.g., cardiac surgeries, organ transplants) that are more common among men tend to have higher costs, contributing to the higher program payments for males.

   - **Race**:

      -  Non-Hispanic White beneficiaries accounted for the highest program payments, at nearly $100M, followed by Black Americans, whose payments were significantly lower by approximately $86M. Other racial groups had average program payments below $10M.
      
      -  Possible reasons: Non-Hispanic White individuals make up the largest proportion of Medicare beneficiaries, leading to higher overall program payments.
    
      -  Generally, as program payments increase, average cost-sharing (deductibles, copayments, and coinsurance) might also rise. This is because higher-cost services or longer hospital stays result in both higher **total payments by Medicare** and **higher out-of-pocket costs for beneficiaries**. A graph is made to demonstrate the correlation between the total program payments and average cost-sharing:
    
   ![plot](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/43a38fde68a09f5a102698220178fd3563efb841/visualizations/corr.png)
    
      -  As we can see, there is a strong positive correlation:
        
         - Higher-cost procedures require higher patient out-of-pocket contributions.
       
         - States/hospitals with high Medicare spending also tend to have higher patient costs.
       
         - Wealthier states or high-cost healthcare regions drive both program payments & cost-sharing up.
           

- **Health Outcomes Correlated with Hospital Type**:

![health](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/43a38fde68a09f5a102698220178fd3563efb841/visualizations/Bar_chart_health_outcomes.png)

   - The average discharged dead in short-stay hospitals was the highest, at 350k, while all other hospital types had under 50k average dischard dead.
     
   - Possible reasons: Short-stay hospitals handle a significantly larger number of patients compared to specialized hospitals, increasing the absolute number of deaths. Moreover, short-stay hospitals conduct major surgeries and high-risk medical interventions, increasing the likelihood of post-operative mortality.



## 4. Hospital Performance and Characteristics

- **Types of Hospitals Delivering Highest or Lowest Program Payments**:
![log](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/43a38fde68a09f5a102698220178fd3563efb841/visualizations/Hospital_Program_Payment_Comparison.png)

   - When comparing the hospital payment with hospital types, Short-stay hospitals received the highest program payments. Critical Access Hospitals, Long-Term Care Hospitals, Inpatient Psychiatric Facilities, and Inpatient Rehabilitation Facilities had slightly lower but relatively evenly distributed payments. Religious Nonmedical Health Care Institutions had the lowest program payments.
     
   - Possible explanations: 
      
      - Short-stay hospitals handle a large number of admissions and discharges, contributing to their high total program payments.
    
      - Critical Access Hospitals, Long-Term Care Hospitals, and Inpatient Rehabilitation Facilities typically have longer patient stays but lower patient volume, leading to lower overall program payments.
    
      - Facilities like Religious Nonmedical Health Care Institutions often provide limited, non-medical treatments, resulting in the lowest program payments.

- **Impact of Hospital Size and Affiliation on Patient Costs and Care Quality**:
  ![impact](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/43a38fde68a09f5a102698220178fd3563efb841/visualizations/Impact_Hospital%20Size_Affiliation_on_Costs.png)
  
   - The largest bubble, representing Short-Stay Hospitals, indicates that they have the largest hospital size and the highest program payments ($110B). This suggests that Short-Stay Hospitals account for the majority of Medicare inpatient spending, as they handle high patient volumes and provide a broad range of medical services.
     
   - Inpatient Rehabilitation Facilities had the highest program payments among non-short-stay hospitals, slightly above other specialized hospitals.This is likely due to longer lengths of stay and specialized rehabilitative care, which can be costly despite lower patient volumes compared to Short-Stay Hospitals.
 
   - The Critical Access Hospitals, Inpatient Psychiatric Facilities, and Long-Term Care Hospitals had similar bubble sizes and program payments (all slightly lower than Inpatient Rehabilitation Facilities). This suggests that despite different hospital functions, their overall costs remain comparable, potentially due to Medicare payment structures and patient utilization patterns.
 
   - Other Hospitals (Federal Emergency, Veterans Affairs, and foreign hospitals), Children's Hospitals, and Religious Nonmedical Health Care Institutions had the smallest program payments and bubble sizes. Their lower costs may be due to limited inpatient admissions, specialized patient populations, or alternative funding sources (e.g., federal government funding for VA hospitals).


## 5. Policy Implications

- **Observable Impacts of Policy Changes Over the Years**:

![Policy](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/43a38fde68a09f5a102698220178fd3563efb841/visualizations/Observable_Impacts_of_Policy_Changes.png)

   - In 2015, there were 11 million discharges, coinciding with the announcement of the Medicare Access and CHIP Reauthorization Act (MACRA). This policy marked a significant shift in Medicare reimbursement, moving from a fee-for-service model toward value-based payments, incentivizing efficiency and quality over volume.

- By 2020, the total number of discharges had dropped sharply to 8.7 million, influenced by several key factors:

   - The implementation of the Site-Neutral Payment Policy, which reduced incentives for inpatient admissions by aligning payments across care settings.

   - The impact of the COVID-19 Public Health Emergency (PHE), which led to a decline in elective procedures, changes in hospital utilization, and a shift towards outpatient and telehealth services.

   - Ongoing Medicare reforms emphasizing cost efficiency and alternative payment models, reducing unnecessary hospital admissions.


## Conclusion

- **Key Insights & Recommendations**
  
   1. Trends in Hospital Utilization & Admissions:
      
   - Hospital admissions gradually declined from 2016 to 2019, followed by a sharp drop in 2020, likely due to Medicare policy changes and the COVID-19 pandemic.
     
   - Alaska, Maryland, and California had the highest program payments per discharge. **Recommendation:** Target cost-efficiency initiatives in high-cost states (e.g., Alaska, Maryland, California) to assess reimbursement models and pricing structures.
 
   2. Financial Aspects & Cost Burdens:

   - Medicare program payments increased from 2016 to 2019, before dropping significantly in 2020 due to COVID-19, then stabilizing slightly in 2021. **Recommendation:** Enhance value-based care adoption to further control costs and reduce unnecessary hospitalizations.
 
   -  Alaska, Maryland, and California had the highest program payments per discharge, suggesting higher healthcare costs, reimbursement rates, or hospital pricing structures in these states. **Recommendation:** Analyze drivers of high program payments per discharge in select states and consider alternative payment strategies.
 
   3. Equity & Disparities in Healthcare Costs:
 
   - Non-Hispanic White beneficiaries had the highest total program payments and cost-sharing amounts, while Black Americans and other racial groups had significantly lower totals. **Recommendation:** Investigate racial and socioeconomic differences in program payments and utilization to ensure equitable healthcare access.
 
   - Dual-Eligibility (MME) Impact on Costs: Beneficiaries with Medicare-Medicaid dual eligibility (MME) had significantly lower cost-sharing amounts than non-MME beneficiaries, suggesting Medicaid’s role in reducing out-of-pocket costs for low-income individuals. **Recommendation:** Enhance support for dual-eligible (MME) beneficiaries to lower financial burdens for low-income populations.

   4. Hospital Performance & Structure:

  - Impact of Hospital Size & Affiliation: Short-stay hospitals were significantly larger and had higher payments ($110B), while smaller hospitals (e.g., Critical Access, Inpatient Rehab, Psychiatric) received much lower payments (<$20B).
 
  - **Recommendation:**
     
     - Evaluate hospital efficiency by correlating program payments with patient outcomes to identify high-performing hospitals.
   
     - Assess performance of lower-utilization hospital types (e.g., Inpatient Psychiatric Facilities, Religious Nonmedical Hospitals) to determine their role and funding efficiency.
   
## **Further Exploration for Deeper Insights**  

For those who want to **dig deeper into this project**, here are some advanced analytical approaches and extensions:  

### **1. Advanced Statistical Analysis & Predictive Modeling**  
- **Time-Series Forecasting:**  
  - Use models like **ARIMA, Prophet, or LSTM** to **predict future Medicare program payments and hospital utilization** trends.  
  - Identify potential **seasonal patterns** in inpatient hospital discharges and spending.  
- **Regression Analysis:**  
  - Perform **linear regression** to analyze the relationship between **program payments, cost-sharing, and utilization rates** across different hospital types and demographics.  
  - Use **multivariate regression** to adjust for confounders such as age, region, and hospital size.  
- **Clustering Analysis:**  
  - Apply **K-Means or Hierarchical Clustering** to group hospitals based on efficiency, cost, and utilization patterns.  
  - Identify which hospitals perform best in cost-per-discharge and patient outcomes.  

### **2. Geographic & Demographic Disparities Analysis**  
- **Heatmaps & Spatial Analysis:**  
  - Use **GIS tools (e.g., QGIS, Python’s Geopandas, or Tableau)** to visualize **regional disparities in Medicare spending and utilization**.  
  - Investigate whether certain geographic areas have **lower access to inpatient hospital care**.  
- **Demographic Risk Factor Analysis:**  
  - Perform **statistical comparisons (T-tests, ANOVA)** to determine whether certain **age, race, or socioeconomic groups** face significantly higher hospital costs or lower accessibility.  

### **3. Cost Efficiency & Hospital Performance Evaluation**  
- **Cost-per-Outcome Analysis:**  
  - Compare **cost per discharge and cost per inpatient day** across different hospital types to identify **high-efficiency facilities**.  
- **Hospital Benchmarking:**  
  - Evaluate hospitals based on **readmission rates, mortality rates, and patient outcomes** to identify facilities providing **high-value care**.  

### **4. Exploring Policy Impacts on Medicare Utilization**  
- **Impact of Policy Changes (2015-2021):**  
  - Examine the effects of key Medicare policies (e.g., **MACRA 2015, Site-Neutral Payment Policy 2020**) on **discharge trends and hospital payments**.  
  - Conduct **difference-in-differences (DiD) analysis** to quantify the impact of policy shifts.  
- **COVID-19 Impact Analysis (2020-2021):**  
  - Investigate how COVID-19 **disrupted inpatient hospital utilization** and program payments.  
  - Compare **pre-pandemic vs. post-pandemic spending and patient demographics**.  

### **5. Scaling the Project with Big Data & Cloud Technologies**  
- **Big Data Pipelines:**  
  - Process large-scale Medicare datasets using **Hadoop or Apache Spark** for faster computation.  
- **Cloud Deployment:**  
  - Deploy dashboards and visualizations using **AWS (S3, Lambda, Glue) or GCP (BigQuery, Cloud Functions)**.  
  - Host a **Medicare insights dashboard using Streamlit or Dash on cloud platforms**.  




  

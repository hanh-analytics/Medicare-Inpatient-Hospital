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

---

## 3. Equity and Disparities

- **Demographic Groups Facing Higher Program Payments or Out-of-Pocket Costs**:

![demo](https://github.com/hanh-analytics/Medicare-Inpatient-Hospital/blob/557bbe64f870b86bf59ee9a59a6e42cac5a04c78/visualizations/Program_payments_strip_plot.png)


   - Identify demographic groups that face higher program payments or out-of-pocket costs.
   - Explore reasons behind these disparities (e.g., underlying health conditions, healthcare access).
   - Consider if these groups may benefit from policy interventions.

- **Geographic Areas with Lower Access to Inpatient Hospital Care**:
   - Examine regions with limited access to inpatient hospital care.
   - Discuss the impact of low access on patient outcomes and equity.
   - Investigate whether underserved regions face financial strain or poor healthcare outcomes.

- **Health Outcomes Correlated with Geographic Location or Hospital Type**:
   - Analyze the correlation between health outcomes (e.g., mortality rates, readmissions) and geographic location or hospital type.
   - Discuss the influence of hospital quality, accessibility, and geographic disparities on patient outcomes.

---

## 4. Hospital Performance and Characteristics

- **Types of Hospitals Delivering Highest or Lowest Program Payments**:
   - Identify which types of hospitals are associated with the highest or lowest program payments.
   - Discuss factors contributing to these differences (e.g., hospital size, teaching affiliation).
   - Explore whether these payments are tied to efficiency or care quality.

- **Impact of Hospital Size and Affiliation on Patient Costs and Care Quality**:
   - Explore how hospital size (e.g., small vs. large hospitals) and affiliation (e.g., teaching vs. non-teaching) impact patient costs and care quality.
   - Analyze whether larger hospitals tend to have higher or lower costs and whether teaching hospitals offer higher quality care.

---

## 5. Policy Implications

- **Observable Impacts of Policy Changes Over the Years**:
   - Identify key policy changes that may have impacted hospital utilization, program payments, or patient costs (e.g., MACRA, Site-Neutral Payment Policy, COVID-19).
   - Examine trends in the data before and after policy changes to assess their impact.
   - Discuss whether any policy adjustments have improved or worsened healthcare access, costs, or quality.

- **Hospitals or Regions That Might Benefit from Interventions**:
   - Identify which hospitals or regions could benefit most from interventions aimed at improving equity and cost efficiency.
   - Consider interventions that could reduce disparities (e.g., increased funding for underserved areas, targeted financial assistance).
   - Propose actions based on findings that could improve healthcare access and efficiency in specific regions or hospital types.

---

## Conclusion

- **Key Insights and Recommendations**:
   - Summarize the main findings from the dashboard and analysis.
   - Provide actionable recommendations for policymakers, hospital administrators, or other stakeholders.
   - Suggest areas for further research or data collection to enhance understanding of healthcare utilization, payments, and policy impacts.

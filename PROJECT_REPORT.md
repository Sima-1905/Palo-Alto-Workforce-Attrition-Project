# Workforce Attrition Patterns and Risk Hotspot Analysis at Palo Alto Networks

## 1. Executive Summary
This project analyzes workforce attrition using the supplied employee dataset containing **1,470 employee records and 31 original analytical fields**. The purpose is to identify where attrition is concentrated across departments, roles, demographics, tenure, overtime, business travel, distance from home and promotion history.

The overall attrition rate is **16.1%**. The results indicate that attrition is particularly concentrated among early-tenure employees, younger employees, overtime workers and selected job roles.

## 2. Problem Statement
HR leadership needs evidence-based answers to:
- Which departments and roles have the highest attrition?
- Which age and tenure groups are most affected?
- Is overtime or business travel associated with higher attrition?
- Are early-career employees leaving more often?
- Where should retention efforts be prioritized?

## 3. Data Validation and Cleaning
- Dataset size: **1,470 rows × 31 columns**.
- Missing values: **0** across the supplied dataset.
- Attrition is encoded as **0 = retained** and **1 = exited**.
- Department and role values were reviewed for consistency.
- Analytical fields were created for age groups and tenure buckets.

## 4. Overall Attrition
- Total employees: **1,470**
- Exited employees: **237**
- Retained employees: **1,233**
- Overall attrition rate: **16.1%**

## 5. Department Analysis
The department attrition rates are:
- **Sales: 20.6%**
- **Human Resources: 19.0%**
- **Research & Development: 13.8%**

The highest department-level attrition is observed in **Sales (20.6%)**.

## 6. Role Analysis
The highest role-level attrition rates are:
- **Sales Representative: 39.8%**
- **Laboratory Technician: 23.9%**
- **Human Resources: 23.1%**
- **Sales Executive: 17.5%**
- **Research Scientist: 16.1%**

The strongest role hotspot is **Sales Representative (39.8%)**.

## 7. Demographic Analysis
### Age
- <25: 35.8%
- 25-34: 19.1%
- 35-44: 9.2%
- 45-54: 11.5%
- 55+: 17.0%

The highest age-group attrition is **<25 (35.8%)**.

### Gender
- Female: 14.8%
- Male: 17.0%

### Marital Status
- Divorced: 10.1%
- Married: 12.5%
- Single: 25.5%

## 8. Tenure and Career Stage
- **0-2 years: 29.8%**
- **3-5 years: 13.8%**
- **6-10 years: 12.3%**
- **11+ years: 8.1%**

Employees with **0–2 years** at the company have the highest tenure-bucket attrition, at **29.8%**.

## 9. Workload and Mobility
### Overtime
- No: 10.4%
- Yes: 30.5%

The difference between overtime and non-overtime attrition is **20.1 percentage points**.

### Business Travel
- Non-Travel: 8.0%
- Travel_Frequently: 24.9%
- Travel_Rarely: 15.0%

Frequent travel has a higher observed attrition rate than non-travel in this dataset.

## 10. Recommendations
1. **Strengthen first-2-year retention:** structured onboarding, mentoring, regular manager check-ins and early-career development plans.
2. **Review overtime workload:** identify teams with sustained overtime and rebalance workload where practical.
3. **Investigate role hotspots:** conduct targeted stay interviews in high-attrition roles, especially sales-representative and laboratory-technician populations.
4. **Review travel burden:** assess whether frequent travel is affecting employee experience, scheduling and work-life balance.
5. **Create promotion visibility:** provide clearer career paths and development plans for employees experiencing long promotion gaps.
6. **Use segmented HR dashboards:** monitor attrition by department, role, age, tenure and workload instead of relying only on organization-wide averages.

## 11. Limitations
This analysis is descriptive. A higher attrition rate in a group indicates an association in this dataset, not that the factor itself causes employees to leave. Further statistical testing or predictive modeling would be needed for causal or predictive claims.

## 12. Conclusion
The analysis provides a practical diagnostic view of workforce attrition. The strongest signals are concentrated around **early tenure, younger age groups, overtime, frequent travel and selected job roles**. A targeted retention strategy based on these hotspots can help HR move from generalized action to evidence-driven workforce management.

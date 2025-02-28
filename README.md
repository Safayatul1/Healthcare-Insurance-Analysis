# Healthcare Insurance EDA

## Overview
This project provides an **Exploratory Data Analysis (EDA)** on a healthcare insurance dataset. The dataset consists of **1,338 records and 7 attributes**, analyzing key trends affecting insurance charges.

## Dataset Information
The dataset contains the following attributes:
- **Age**: Age of the insured individual.
- **Sex**: Gender of the individual (Male/Female).
- **BMI**: Body Mass Index, a measure of body fat.
- **Children**: Number of dependents covered under the insurance.
- **Smoker**: Indicates whether the individual is a smoker (Yes/No).
- **Region**: Geographic region where the policyholder resides.
- **Charges**: The medical insurance cost charged to the individual.

## Project Structure
```
Healthcare_Insurance_EDA/
│── BMI vs Insurance.png          # Scatter plot for BMI vs Charges
│── Boxplot.png                   # Boxplot for detecting outliers
│── Distribution graph.png         # Histograms for numerical features
│── README.md                     # Project documentation
│── Report_Healthcare Insurance.pdf # PDF report with findings & visualizations
│── Summary Statistics.png         # Summary statistics table
│── analysis.py                    # Python script for EDA
│── insurance.csv                   # Raw dataset
```

## Installation & Usage
To run this analysis, you need Python **3.x** and the following libraries:
```bash
pip install pandas numpy matplotlib
```
Run the analysis script:
```bash
python analysis.py
```

## Key Insights
- **Smokers pay significantly higher insurance charges** than non-smokers.
- **Higher BMI is associated with increased insurance costs**.
- **Outliers in insurance charges** exist, likely due to lifestyle factors.

## Visualizations
This analysis includes:
- **Histograms** for Age, BMI, Children, and Charges distributions *(Distribution graph.png)*.
- **Boxplots** for outlier detection in BMI and Charges *(Boxplot.png)*.
- **Scatter plot** showing BMI vs. Insurance Charges *(BMI vs Insurance.png)*.
- **Summary statistics table** *(Summary Statistics.png)*.

## Next Steps
- Develop a **predictive model** for estimating insurance costs.
- Analyze **regional variations** in insurance charges.
- Investigate **factors contributing to outliers** in charges.

## Contributions
Feel free to fork and contribute to this project. If you find this useful, give it a ⭐ on GitHub!


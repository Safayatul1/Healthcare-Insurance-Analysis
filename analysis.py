# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("insurance.csv")

# Display basic dataset info
print("Dataset Info:")
print(df.info())

# Check dataset shape (number of rows and columns)
print("\nDataset Shape:", df.shape)

# Display first few rows
print("\nFirst 5 Rows of Dataset:")
print(df.head())

# 1. Check for Missing Values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# 2. Summary Statistics
print("\nSummary Statistics for Numerical Columns:")
print(df.describe())

# 3. Distribution of Numerical Features (Histograms)
num_cols = ["age", "bmi", "children", "charges"]

plt.figure(figsize=(12, 8))
for i, col in enumerate(num_cols, 1):
    plt.subplot(2, 2, i)
    plt.hist(df[col], bins=30, edgecolor="black")
    plt.title(f"Distribution of {col}")
plt.tight_layout()
plt.show()

# 4. Outlier Detection (Boxplots)
plt.figure(figsize=(12, 8))
for i, col in enumerate(num_cols, 1):
    plt.subplot(2, 2, i)
    plt.boxplot(df[col], vert=False)
    plt.title(f"Boxplot of {col}")
plt.tight_layout()
plt.show()

# 5. Convert Categorical Variables to Numeric
df_encoded = df.copy()

# Encoding binary categorical variables
df_encoded["sex"] = df_encoded["sex"].map({"male": 1, "female": 0})  # Male = 1, Female = 0
df_encoded["smoker"] = df_encoded["smoker"].map({"yes": 1, "no": 0})  # Smoker = 1, Non-smoker = 0

# Encoding 'region' using one-hot encoding
df_encoded = pd.get_dummies(df_encoded, columns=["region"], drop_first=True)

# 6. Correlation Matrix
correlation_matrix = df_encoded.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# 7. Impact of Smoking on Insurance Charges
smoker_charges = df.groupby("smoker")["charges"].mean()
print("\nAverage Insurance Charges for Smokers vs. Non-Smokers:")
print(smoker_charges)

# 8. BMI vs. Insurance Charges (Scatter Plot)
plt.figure(figsize=(8, 6))
plt.scatter(df["bmi"], df["charges"], alpha=0.5)
plt.xlabel("BMI")
plt.ylabel("Charges")
plt.title("BMI vs Insurance Charges")
plt.show()

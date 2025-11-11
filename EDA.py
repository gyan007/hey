# 1️ Data Cleaning


import pandas as pd
import numpy as np
# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eve'],
    'Age': [25, np.nan, 30, 22, 28],
    'Score': [85, 90, np.nan, 70, 95]
}
df = pd.DataFrame(data)
print("Original:\n", df)
# Drop missing rows
df = df.dropna()
# Fill missing values (example: with mean)
# df['Age'].fillna(df['Age'].mean(), inplace=True)
# Remove duplicates
df.drop_duplicates(inplace=True)
print("\nCleaned:\n", df)


#  2️ Data Preprocessing


# Convert data types
df['Age'] = df['Age'].astype(int)
# Normalize/Scale numeric data
df['Score'] = df['Score'] / 100  # example of scaling 0–1
# Encode categorical data
df['Gender'] = ['F', 'M', 'M', 'F'][:len(df)]
df['Gender'] = df['Gender'].map({'M': 1, 'F': 0})
print("\nPreprocessed:\n", df)


#  3️ Exploratory Data Analysis (EDA)


import seaborn as sns
import matplotlib.pyplot as plt
print("\nBasic Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())
# Pairplot to see relationships
sns.pairplot(df)
plt.show()
# Correlation Heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
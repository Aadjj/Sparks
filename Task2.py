# Author:- Syed Adnan Ahmed

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("C:\\Users\\Mohammed Khubaib\\OneDrive\\Desktop\\SampleSuperstore (1).csv")

# Display the first few rows of the dataset
print(data.head())

# Check the dimensions of the dataset
print("Data Shape:", data.shape)

# Get summary statistics of the numerical columns
print("Summary Statistics:\n", data.describe())

# Check the data types of the columns
print("Data Types:\n", data.dtypes)

# Check for missing values
print("Missing Values:\n", data.isnull().sum())

# Check for duplicate rows
print("Duplicate Rows:", data.duplicated().sum())

# Visualize the distribution of profit
plt.figure(figsize=(10, 6))
sns.histplot(data['Profit'], kde=True)
plt.title('Distribution of Profit')
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.show()

# Visualize the sales by region
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sales', data=data, palette='Blues')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.show()

# Visualize the profit by category
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Profit', data=data, palette='Greens')
plt.title('Profit by Category')
plt.xlabel('Category')
plt.ylabel('Profit')
plt.show()

# Visualize the sales and profit by sub-category
plt.figure(figsize=(12, 6))
sns.barplot(x='Sub-Category', y='Sales', data=data, palette='Reds')
plt.title('Sales by Sub-Category')
plt.xlabel('Sub-Category')
plt.ylabel('Sales')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x='Sub-Category', y='Profit', data=data, palette='Oranges')
plt.title('Profit by Sub-Category')
plt.xlabel('Sub-Category')
plt.ylabel('Profit')
plt.xticks(rotation=90)
plt.show()

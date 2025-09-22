# Task 1: Load and Explore the Dataset


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris

# Load dataset (Iris dataset is built-in)
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})  # map integers to names
    
    print("✅ Dataset loaded time to have fun with python learn on PLP!")
except FileNotFoundError:
    print("❌ File not found. Please check your dataset path.")
except Exception as e:
    print("❌ Error loading dataset:", e)

# Display first few rows
print("\n--- First 5 rows of dataset ---")
print(df.head())

# Check structure
print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Missing Values per Column ---")
print(df.isnull().sum())

# Clean missing values (not really needed for iris, but included)
df = df.dropna()  # or df.fillna(method="ffill") to fill missing values


# Task 2: Basic Data Analysis

# Basic statistics
print("\n--- Descriptive Statistics ---")
print(df.describe())

# Grouping by species
group_means = df.groupby("species").mean()
print("\n--- Mean values per species ---")
print(group_means)

# Simple insight
print("\nObservation: Virginica generally has larger petal measurements than Setosa.")

# Task 3: Data Visualization

# 1. Line chart (simulate time-series: use row index as "time")
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.plot(df.index, df["petal length (cm)"], label="Petal Length")
plt.title("Line Chart of Sepal vs Petal Length over Index")
plt.xlabel("Index (simulated time)")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(6,4))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(6,4))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (relationship between sepal length and petal length)
plt.figure(figsize=(6,4))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, s=60)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

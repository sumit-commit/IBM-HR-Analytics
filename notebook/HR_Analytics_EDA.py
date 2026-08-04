import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")

# Load Dataset
df = pd.read_csv("data/hr_employee_attrition.csv")

"""# **Data Cleaning**"""

df.head()

df.shape

df.info()

df.describe()

# Checking For Null Values
df.isnull().sum()

"""No Null Values"""

df.columns

# Checking For Duplicates
df.duplicated().sum()

"""No duplicates"""

# Checking For Uniques Values for Different Columns
for col in df.select_dtypes(include='object'):
    print(col)
    print(df[col].unique())
    print()

# Checking Data Types
df.dtypes

"""Formatting Column Names"""

import re

df.columns = [
    re.sub(r'(?<!^)(?=[A-Z])', '_', col).lower()
    for col in df.columns
]

df.columns

"""Drop columns"""

cols_to_drop = ['employee_count', 'over18', 'standard_hours', 'employee_number']

df.drop(columns=cols_to_drop, inplace=True, errors='ignore')

df.shape

"""Creating Binary Flags"""

df['attrition_flag'] = df['attrition'].map({'Yes': 1, 'No': 0})
df['over_Time_flag'] = df['over_time'].map({'Yes': 1, 'No': 0})

categorical_cols = df.select_dtypes(include='object').columns

for col in categorical_cols:
    df[col] = df[col].str.strip()

df.shape

"""Save Cleaned Data"""

df.to_csv("cleaned_hr_data.csv", index=False)

"""# **Exploratory Data Analysis**

Key Metrics
"""

total_employees = len(df)
attrition_count = df['attrition_flag'].sum()
attrition_rate = (attrition_count / total_employees) * 100

print(f"Total Employees: {total_employees}")
print(f"Total Left: {attrition_count}")
print(f"Overall Attrition Rate: {attrition_rate:.2f}%")

"""Attrition Rate by Department"""

dept_eda = df.groupby('department')['attrition_flag'].mean() * 100
print("\n--- Attrition Rate by Department ---")
print(dept_eda.round(2))

"""Top 5 Job Roles with Highest Attrition"""

role_eda = df.groupby('job_role')['attrition_flag'].mean() * 100
print("\n--- Top 5 Job Roles with Highest Attrition ---")
print(role_eda.sort_values(ascending=False).head(5).round(2))

"""Average Monthly Income Comparison"""

income_eda = df.groupby('attrition_flag')['monthly_income'].mean()
print("\n--- Average Monthly Income Comparison ---")
print(f"Staying (0): ${income_eda[0]:.2f}")
print(f"Left (1):    ${income_eda[1]:.2f}")

"""Attrition Rate by Overtime Status"""

ot_eda = df.groupby('over_time')['attrition_flag'].mean() * 100
print("\n--- Attrition Rate by Overtime Status ---")
print(f"No Overtime:  {ot_eda['No']:.2f}%")
print(f"Works Overtime: {ot_eda['Yes']:.2f}%")

"""# **Visualization**"""

# Set up the visualization canvas
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
sns.set_theme(style="whitegrid")

# Attrition Count (Imbalance Check)
sns.countplot(x='attrition_flag', hue='attrition_flag', data=df, ax=axes[0,0], palette='Set2', legend=False)
axes[0,0].set_title('Overall Employee Attrition Count')
axes[0,0].set_xticks([0, 1])
axes[0,0].set_xticklabels(['Staying (0)', 'Left (1)'])

# Monthly Income Boxplot by Attrition
sns.boxplot(x='attrition_flag', y='monthly_income', hue='attrition_flag', data=df, ax=axes[0,1], palette='Set2', legend=False)
axes[0,1].set_title('Monthly Income Distribution vs Attrition')
axes[0,1].set_xticks([0, 1])
axes[0,1].set_xticklabels(['Staying (0)', 'Left (1)'])

# Job Satisfaction vs Attrition
sns.barplot(x='job_satisfaction', y='attrition_flag', hue='job_satisfaction', data=df, ax=axes[1,0], errorbar=None, palette='Blues_d', legend=False)
axes[1,0].set_title('Attrition Rate by Job Satisfaction Level (1-4)')
axes[1,0].set_ylabel('Attrition Proportion')

# Distance From Home vs Attrition
sns.kdeplot(data=df, x='distance_from_home', hue='attrition_flag', fill=True, common_norm=False, ax=axes[1,1], palette='Set1')
axes[1,1].set_title('Distance From Home Distribution for Staying vs Leaving')

plt.tight_layout()
plt.show()

# Department Distribution

sns.countplot(y='department', data=df, hue='department', palette='Set2', legend=False)

# Job Role Distribution

sns.countplot(
    y='job_role',
    data=df, hue='job_role', legend=False, palette='Set2',
    order=df['job_role'].value_counts().index
)

# Monthly Income Distribution

sns.histplot(df['monthly_income'], bins=30, color = 'royalblue')

#Monthly Income by Department

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x='department',
    y='monthly_income',
    hue='department',
    legend=False
)

plt.xticks(rotation=20)

plt.show()

# Set up a 2x2 grid canvas for the 4 charts
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
sns.set_theme(style="whitegrid")

# Attrition by Gender (Top Left)
sns.barplot(x='gender', y='attrition_flag', hue='gender', data=df, ax=axes[0, 0], errorbar=None, palette='Set2', legend=False)
axes[0, 0].set_title('Attrition Rate by Gender')
axes[0, 0].set_ylabel('Attrition Rate (Proportion)')

# Attrition by Department (Top Right)
sns.barplot(x='department', y='attrition_flag', hue='department', data=df, ax=axes[0, 1], errorbar=None, palette='Set2', legend=False)
axes[0, 1].set_title('Attrition Rate by Department')
axes[0, 1].set_ylabel('Attrition Rate (Proportion)')

# Attrition by Job Role (Bottom Left)
sns.barplot(x='attrition_flag', y='job_role', hue='job_role', data=df, ax=axes[1, 0], errorbar=None, palette='Set2', legend=False)
axes[1, 0].set_title('Attrition Rate by Job Role')
axes[1, 0].set_xlabel('Attrition Rate (Proportion)')

# Attrition by Overtime (Bottom Right)
sns.barplot(x='over_time', y='attrition_flag', hue='over_time', data=df, ax=axes[1, 1], errorbar=None, palette='Set2', legend=False)
axes[1, 1].set_title('Attrition Rate by Overtime Status')
axes[1, 1].set_ylabel('Attrition Rate (Proportion)')
axes[1, 1].set_xticks([0, 1])
axes[1, 1].set_xticklabels(['No Overtime (0)', 'Works Overtime (1)'])

# Clean up layout spacing so text elements do not overlap
plt.tight_layout()
plt.show()

# Set up a 2x2 grid canvas for the 4 charts
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
sns.set_theme(style="whitegrid")

# Job Satisfaction vs Attrition (Top Left)
sns.barplot(x='job_satisfaction', y='attrition_flag', hue='job_satisfaction', data=df, ax=axes[0, 0], errorbar=None, palette='Blues_d', legend=False)
axes[0, 0].set_title('Attrition Rate by Job Satisfaction (1=Low, 4=High)')
axes[0, 0].set_ylabel('Attrition Rate')
axes[0, 0].set_xlabel('Satisfaction Level')

# Environment Satisfaction vs Attrition (Top Right)
sns.barplot(x='environment_satisfaction', y='attrition_flag', hue='environment_satisfaction', data=df, ax=axes[0, 1], errorbar=None, palette='Blues_d', legend=False)
axes[0, 1].set_title('Attrition Rate by Environment Satisfaction (1=Low, 4=High)')
axes[0, 1].set_ylabel('Attrition Rate')
axes[0, 1].set_xlabel('Satisfaction Level')

# Work-Life Balance vs Attrition (Bottom Left)
sns.barplot(x='work_life_balance', y='attrition_flag', hue='work_life_balance', data=df, ax=axes[1, 0], errorbar=None, palette='Greens_d', legend=False)
axes[1, 0].set_title('Attrition Rate by Work-Life Balance (1=Bad, 4=Best)')
axes[1, 0].set_ylabel('Attrition Rate')
axes[1, 0].set_xlabel('Work-Life Balance Score')

# Business Travel vs Attrition (Bottom Right)
sns.barplot(x='business_travel', y='attrition_flag', hue='business_travel', data=df, ax=axes[1, 1], errorbar=None, palette='Purples_d',
            order=['Non-Travel', 'Travel_Rarely', 'Travel_Frequently'])
axes[1, 1].set_title('Attrition Rate by Business Travel Frequency')
axes[1, 1].set_ylabel('Attrition Rate')
axes[1, 1].set_xlabel('Travel Frequency')

# Adjust layout spacing to keep the canvas clean and readable
plt.tight_layout()
plt.show()

# Set up a 2x2 grid canvas for the 4 charts
fig, axes = plt.subplots(2, 2, figsize=(18, 14))
sns.set_theme(style="whitegrid")

# Attrition by Marital Status (Top Left)
sns.barplot(
    x='marital_status',
    y='attrition_flag',
    hue='marital_status',
    data=df,
    ax=axes[0, 0],
    errorbar=None,
    palette='Set2',
    legend=False
)
axes[0, 0].set_title('Attrition Rate by Marital Status')
axes[0, 0].set_ylabel('Attrition Rate')
axes[0, 0].set_xlabel('Marital Status')

# Attrition by Education Field (Top Right) - Rotated text to prevent overlap
sns.barplot(
    x='attrition_flag',
    y='education_field',
    hue='education_field',
    data=df,
    ax=axes[0, 1],
    errorbar=None,
    palette='Set2',
    legend=False
)
axes[0, 1].set_title('Attrition Rate by Education Field')
axes[0, 1].set_xlabel('Attrition Rate')
axes[0, 1].set_ylabel('Education Field')

# Attrition by Years at Company (Bottom Left) - Line plot works best for continuous time trends
sns.lineplot(
    x='years_at_company',
    y='attrition_flag',
    data=df,
    ax=axes[1, 0],
    errorbar=None,
    color='teal',
    linewidth=2.5
)
axes[1, 0].set_title('Attrition Trend by Years at Company')
axes[1, 0].set_ylabel('Attrition Rate')
axes[1, 0].set_xlabel('Years Worked at Company')

# Attrition by Age Group (Bottom Right) - Fills the 4th canvas slot perfectly
# Create temporary age bins for cleaner grouping
df['age_group'] = pd.cut(df['age'], bins=[18, 25, 35, 45, 55, 65], labels=['18-25', '26-35', '36-45', '46-55', '56+'])
sns.barplot(x='age_group', y='attrition_flag', data=df, ax=axes[1, 1], errorbar=None, legend=False)
axes[1, 1].set_title('Attrition Rate by Age Group')
axes[1, 1].set_ylabel('Attrition Rate')
axes[1, 1].set_xlabel('Age Range')


# Clean up layout spacing so titles and axis labels do not crash
plt.tight_layout()
plt.show()

# Drop the temporary column to keep your main dataframe clean
df.drop(columns=['age_group'], errors='ignore', inplace=True)

## Filter out only the numerical columns for correlation calculation

# This excludes text-based columns like Department or JobRole
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
corr_matrix = df[numeric_cols].corr()

# Focus specifically on how columns relate to Attrition

# This prints a clean ranked text list next to your visual plot
print("--- Correlation Scores directly with Attrition ---")
print(corr_matrix['attrition_flag'].sort_values(ascending=False))

# Set up a large canvas for a clear, readable grid matrix
plt.figure(figsize=(20, 16))

# Generate the heatmap with color coding, values, and a clean layout
# 'RdBu_r' gives Red for positive correlation, Blue for negative correlation
sns.heatmap(
    corr_matrix,
    annot=True,          # Show the correlation coefficient number in each cell
    fmt=".2f",           # Round the numbers to 2 decimal places
    cmap='RdBu_r',       # High contrast color map for positive/negative trends
    vmin=-1, vmax=1,     # Standard correlation boundaries
    square=True,         # Force cells to be perfect squares
    linewidths=0.5,      # Add a thin border line between cells
    cbar_kws={"shrink": .8} # Slightly shrink the color bar legend
)

plt.title('HR Analytics Dashboard - Core Feature Correlation Heatmap', fontsize=18, fontweight='bold', pad=20)
plt.xticks(rotation=45, ha='right', fontsize=11)
plt.yticks(fontsize=11)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Calculate the exact numerical averages for text validation
income_by_dept = df.groupby('department')['monthly_income'].mean().reset_index()
print("--- Average Monthly Income by Department ---")
for index, row in income_by_dept.iterrows():
    print(f"{row['department']}: ${row['monthly_income']:.2f}")

ax = sns.barplot(
    x='department',
    y='monthly_income',
    hue='department',
    data=df,
    errorbar=None,
    legend=False
)

# Explicitly loop through the bars to draw the clean dollar labels manually
for p in ax.patches:
    height = p.get_height()
    ax.text(
        p.get_x() + p.get_width() / 2.0,  # X coordinate: Center of the bar
        height + 150,                     # Y coordinate: Just above the top edge
        f"${height:,.2f}",                # Clean string mapping format
        ha='center',
        fontweight='bold',
        fontsize=11
    )

plt.title('Average Monthly Income across Corporate Departments', fontsize=14, fontweight='bold', pad=15)
plt.ylabel('Average Monthly Income ($)', fontsize=12)
plt.xlabel('Department', fontsize=12)
plt.ylim(0, df['monthly_income'].max() * 0.5)

plt.tight_layout()
plt.show()

df.rename(columns={"over_Time_flag": "over_time_flag"}, inplace=True)

df.info()

df.to_csv(
    "cleaned_hr_data.csv",
    index=False
)
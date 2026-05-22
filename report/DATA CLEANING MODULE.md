## DATA CLEANING MODULE 

# Purpose

The cleaning module is responsible for:

loading the raw dataset
inspecting dataset quality
validating dataset consistency
identifying missing values
generating deterministic data summaries
Functional Responsibilities
Dataset Intake

Reads raw CSV dataset using:

pd.read_csv()
Data Inspection

Displays:

initial dataset preview
dataset structure
statistical summaries

Implemented using:

df.head()
df.describe()
Missing Value Analysis

Computes:

total missing values
missing value percentages
Unique Value Analysis

Computes unique feature counts:

df.nunique()

# ### 1. Data Preprocessing:
# - Import the dataset and perform necessary data preprocessing steps, including data cleaning, handling missing  values, and converting data types if need

#importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#reading the dataset
file_path = "data\data.csv" 


# Replace missing values for a string feature
missing_values = ["n.a.", "NA", "n/a", "na"]

# Try reading the CSV file with different encodings
try:
    df = pd.read_csv(file_path, encoding='utf-8', na_values = missing_values)
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='latin1', na_values = missing_values)

print("Displaying the dataframe:\n",df)   #displaying the dataset

print("Displaying the first 10 rows of the dataset\n",df.head(10))   #displaying the dataset with all columns for the first 10 rows

print("Displaying the last 10 rows of the dataset\n", df.tail(10))   #displaying the dataset with all columns for the last 10 rows

print("Displaying all the information about the dataset\n:", df.info())    #displaying all the information about the dataset

print("Displaying the summary of each columns:\n", df.describe(include="all"))    #displaying the summary of each columns

print("Displaying the datatypes\n",df.dtypes) #displaying the datatypes of dataset

# Data Dictonary
# - InvoiceNo: The invoice number for each transaction.
# - StockCode: Code for each item.
# - Description: Description of the item.
# - Quantity: The quantity of each item purchased.
# - InvoiceDate: The date and time of the transaction.
# - UnitPrice: Price per unit of the item.
# - CustomerID: ID of the customer.
# - Country: Country of the customer.

print("Displaying the column names in the dataframe:\n",df.columns) #displaying the columns names

print("Number of null values present in each column:\n",df.isnull().sum()) #counting the no.of null values present in each column

print("Percentage of null values present in the dataset:\n",(df.isnull().sum()/df.shape[0])*100) #checking the percent of data that is missing


# Display a few rows where the CustomerID is missing
missing_customerID = df[df['CustomerID'].isnull()]
print(missing_customerID.head(10))


# 2. Remove missing values in CustomerID

# Step 1: Create a condition to check for non-null (not missing) CustomerID values
condition_for_non_null_customerid = pd.notnull(df['CustomerID'])

# Step 2: Apply this condition to filter the DataFrame. This will retain only the rows where CustomerID is not null
df = df[condition_for_non_null_customerid]

df = df[pd.notnull(df['CustomerID'])]

# Convert CustomerID from float to int
df['CustomerID'] = df['CustomerID'].astype(int)

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

#Dropping the duplicate rows
df = df.drop_duplicates()

print("Displaying dataframe after handling duplicates:\n",df) #displaying the dataframe

print("Information of the dataset\n",df.info())  
# checking if the data type of CustomerID and InvoiceDate are changed to integer and datetime object respectively

print("Displaying no.of null values after handling:\n",df.isnull().sum()) #counting the no.of null values after handling missing values.

print("percent of data that is missing after handling missing values:\n", (df.isnull().sum()/df.shape[0])*100)  #checking the percent of data that is missing after handling missing values.


print("Summary of the dataset\n", df.describe()) #displaying the summary of each columns after handling missing values 

df.to_csv("data\data_preprocessed.csv", index = False) #downloading the preprocessed dataset

print("Download Complete")
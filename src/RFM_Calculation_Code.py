###  2. RFM Calculation:
# - Calculate the RFM metrics for each customer:
# - Recency (R): How recently a customer made a purchase. Calculate the number of days since the customer's last purchase.
# - Frequency (F): How often a customer makes a purchase. Calculate the total number of orders for each customer.
# - Monetary (M): The total monetary value of a customer's purchases. Calculate the sum of the total price for each customer.


#reading the data after preprocessing

#importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

#reading the preprocessed dataset
df = pd.read_csv(r'C:\Users\RUTHVIKA REDDY\OneDrive\Desktop\Projects\Customer Segmentation\data_preprocessed.csv')

# Calculate Recency (R)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

max_date = df['InvoiceDate'].max()
df['Recency'] = (max_date - df.groupby('CustomerID')['InvoiceDate'].transform('max')).dt.days

# Calculate Frequency (F)
df['Frequency'] = df.groupby('CustomerID')['InvoiceNo'].transform('nunique')

# Calculate Monetary (M)
df['Monetary'] = df.groupby('CustomerID')['UnitPrice'].transform('sum')

# Create a new DataFrame for RFM metrics
rfm_table = df[['CustomerID', 'Recency', 'Frequency', 'Monetary']].drop_duplicates()

# Display the RFM table
print("RFM Table:\n",rfm_table)

# Print Recency (R)
print("Recency (R):")
print(rfm_table[['CustomerID', 'Recency']])

# Print Frequency (F)
print("\nFrequency (F):")
print(rfm_table[['CustomerID', 'Frequency']])

# Print Monetary (M)
print("\nMonetary (M):")
print(rfm_table[['CustomerID', 'Monetary']])

import matplotlib.pyplot as plt
# Scatter plot for Recency vs Frequency
plt.scatter(rfm_table['Recency'], rfm_table['Frequency'])
plt.title('Recency vs Frequency')
plt.xlabel('Recency')
plt.ylabel('Frequency')
plt.show()

# Scatter plot for Frequency vs Monetary
plt.scatter(rfm_table['Frequency'], rfm_table['Monetary'])
plt.title('Frequency vs Monetary')
plt.xlabel('Frequency')
plt.ylabel('Monetary')
plt.show()


fig = plt.figure(figsize=(10, 8))  # Adjust the size as needed
ax = fig.add_subplot(111, projection='3d')

ax.scatter(rfm_table['Recency'], rfm_table['Frequency'], rfm_table['Monetary'])
ax.set_xlabel('Recency')
ax.set_ylabel('Frequency')
ax.set_zlabel('Monetary')
plt.title('3D Scatter Plot for RFM')

plt.show()
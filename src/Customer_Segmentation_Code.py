### 3. RFM Segmentation:
# -  Assign RFM scores to each customer based on their quartiles (or custom-defined bins). You can use quartiles (1 to 4) or custom scores (e.g., 1 to 5) for each RFM metric.
# -  Combine the RFM scores to create a single RFM score for each customer.

#importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#reading the preprocessed dataset
df = pd.read_csv(r'C:\Users\RUTHVIKA REDDY\OneDrive\Desktop\Projects\Customer Segmentation\data_preprocessed.csv')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Calculate Recency (R)
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

# Step 1: Scoring RFM Metrics

# Assign quartile scores for Recency
rfm_table['RecencyScore'] = pd.qcut(rfm_table['Recency'], 4, labels=[4, 3, 2, 1])

# Assign quartile scores for Frequency
rfm_table['FrequencyScore'] = pd.qcut(rfm_table['Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4])

# Assign quartile scores for Monetary
rfm_table['MonetaryScore'] = pd.qcut(rfm_table['Monetary'], 4, labels=[1, 2, 3, 4])

# Step 2: Combine Scores to form RFM Score
rfm_table['RFMScore'] = rfm_table['RecencyScore'].astype(str) + rfm_table['FrequencyScore'].astype(str) + rfm_table['MonetaryScore'].astype(str)

# Step 3: Create Final Output Table
final_output = rfm_table[['CustomerID', 'RecencyScore', 'FrequencyScore', 'MonetaryScore', 'RFMScore']]

# Display the final output table
final_output.head()

# Sort the final table by RFM Score in descending order
sorted_final_output = final_output.sort_values(by='RFMScore', ascending=False)

# Display the sorted table
sorted_final_output.head(100)

# ### 4. Customer Segmentation:
# - Use clustering techniques (e.g., K-Means clustering) to segment customers based on their RFM scores.
# - Experiment with different numbers of clusters to find the optimal number that provides meaningful segments.

# Step 1: Feature Selection
rfm_features = rfm_table[['RecencyScore', 'FrequencyScore', 'MonetaryScore']]

# Step 2: Scaling (Optional)
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_features)

# Step 3: Choosing the Number of Clusters
# You can experiment with different values for 'num_clusters'
num_clusters = 4

# Step 4: Applying K-Means
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
rfm_table['Cluster'] = kmeans.fit_predict(rfm_scaled)

# Step 5: Analyzing Results
# Display the number of customers in each cluster
print(rfm_table['Cluster'].value_counts())

# Step 6: Visualizing the Clusters
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(rfm_table['RecencyScore'], rfm_table['FrequencyScore'], rfm_table['MonetaryScore'], c=rfm_table['Cluster'], cmap='viridis')
ax.set_xlabel('RecencyScore')
ax.set_ylabel('FrequencyScore')
ax.set_zlabel('MonetaryScore')
ax.set_title(f'Customer Segmentation - {num_clusters} Clusters')

# Add a colorbar
fig.colorbar(scatter, ax=ax, label='Cluster')

plt.show()

# Experiment with different numbers of clusters

max_clusters = 10  # You can adjust this based on your preferences

# Store the inertia (sum of squared distances to the closest centroid) for each number of clusters
inertia = []

for num_clusters in range(1, max_clusters + 1):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(rfm_scaled)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve with a line connecting the points
plt.plot(range(1, max_clusters + 1), inertia, marker='o', linestyle='-', color='b')

# Mark the elbow point
elbow_point = (3, inertia[2])  # Adjust based on your analysis
plt.scatter(*elbow_point, color='red', marker='o', label='Elbow Point')

plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method to Find Optimal Number of Clusters')
plt.legend()
plt.show()

### 5. Segment Profiling:
# - Analyze and profile each customer segment. Describe the characteristics of customers in each segment, including their RFM scores and any other relevant attributes

# Convert Categorical columns to numerical values
rfm_table['RecencyScore'] = rfm_table['RecencyScore'].astype(int)
rfm_table['FrequencyScore'] = rfm_table['FrequencyScore'].astype(int)
rfm_table['MonetaryScore'] = rfm_table['MonetaryScore'].astype(int)

# Group customers by the 'Cluster' column
segment_profiles = rfm_table.groupby('Cluster').agg({
    'RecencyScore': ['mean', 'min', 'max'],
    'FrequencyScore': ['mean', 'min', 'max'],
    'MonetaryScore': ['mean', 'min', 'max'],
    'CustomerID': 'count'  # Number of customers in each segment
}).reset_index()

# Rename the columns for better readability
segment_profiles.columns = ['Cluster', 'RecencyMean', 'RecencyMin', 'RecencyMax',
                             'FrequencyMean', 'FrequencyMin', 'FrequencyMax',
                             'MonetaryMean', 'MonetaryMin', 'MonetaryMax',
                             'CustomerCount']

# Display the segment profiles
print (segment_profiles)
# ## 7. Visualization:
# 
# - Create visualizations (e.g., bar charts, scatter plots, or heat maps) to illustrate the RFM distribution and the clusters formed

import seaborn as sns
import matplotlib.pyplot as plt
from Customer_Segmentation_Code import rfm_table

# Set up subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# Bar chart for Recency distribution
sns.countplot(x='RecencyScore', data=rfm_table, ax=axes[0, 0])
axes[0, 0].set_title('Recency Distribution')

# Bar chart for Frequency distribution
sns.countplot(x='FrequencyScore', data=rfm_table, ax=axes[0, 1])
axes[0, 1].set_title('Frequency Distribution')

# Bar chart for Monetary distribution
sns.countplot(x='MonetaryScore', data=rfm_table, ax=axes[1, 0])
axes[1, 0].set_title('Monetary Distribution')

# Scatter plot for Clusters
sns.scatterplot(x='RecencyScore', y='FrequencyScore', hue='Cluster', data=rfm_table, ax=axes[1, 1])
axes[1, 1].set_title('Clusters Based on RFM Scores')

# Adjust layout
plt.tight_layout()
plt.show()

# Scatter plot for RFM distribution
plt.figure(figsize=(18, 5))

plt.subplot(1, 3, 1)
sns.scatterplot(x='RecencyScore', y='FrequencyScore', hue='Cluster', data=rfm_table, palette='viridis', alpha=0.7)
plt.title('Recency vs. Frequency')

plt.subplot(1, 3, 2)
sns.scatterplot(x='FrequencyScore', y='MonetaryScore', hue='Cluster', data=rfm_table, palette='viridis', alpha=0.7)
plt.title('Frequency vs. Monetary')

plt.subplot(1, 3, 3)
sns.scatterplot(x='RecencyScore', y='MonetaryScore', hue='Cluster', data=rfm_table, palette='viridis', alpha=0.7)
plt.title('Recency vs. Monetary')

plt.tight_layout()
plt.show()

# Create a DataFrame for heatmap
heatmap_data = rfm_table.groupby('Cluster').agg({
    'RecencyScore': 'mean',
    'FrequencyScore': 'mean',
    'MonetaryScore': 'mean',
}).reset_index()

# Pivot the DataFrame for heatmap
heatmap_data_pivot = heatmap_data.pivot(index='Cluster', columns='RecencyScore', values='MonetaryScore')

# Create a heatmap with statistics
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data_pivot, cmap='viridis', annot=True, fmt=".2f", linewidths=.5, cbar_kws={"label": "MonetaryScore"})
plt.title('RFM Distribution and Clusters')
plt.xlabel('RecencyScore')
plt.ylabel('Cluster')

plt.show()


# Display the underlying data
print("Data for Heatmap:")
print(heatmap_data_pivot)
print("\nStatistics:")
print(heatmap_data)
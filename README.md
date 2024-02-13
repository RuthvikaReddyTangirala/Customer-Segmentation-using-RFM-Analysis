# Introduction

![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/570c207d-8230-44d6-8553-4229abb2f7e6)

For any business, understanding customer behavior and product sales is crucial for survival and success, whether it operates online or has a physical location. Utilized VS code and Python to help an online retail business increase its revenue and profit margin by providing valuable insights through customer segmentation and an RFM (Recency, Frequency, Monetary) analysis on the dataset. We obtained the dataset from a Kaggle notebook sourced through the UCI Machine Learning Repository. 
  
Analyzing customer data is crucial for businesses to identify the most suitable target audience for different advertising strategies. To begin with, we sorted the data and conducted an RFM analysis, which helped us extract valuable insights into the ideal customer base. We analyzed their activity time, purchase frequency, and spending patterns to identify the most relevant customer groups. Finally, assigned each group an RFM score based on the above parameters and determined the appropriate approach. 
  
Meticulously cleaned and prepared the dataset obtained from the Kaggle notebook to complete this project analysis. Additionally, we have followed a structured and reliable method for exploring the dataset using Python's Pandas library on the Jupyter Notebook platform. Our ultimate goal is to offer comprehensive and actionable insights on marketing and advertising strategies to help the business increase profitability and achieve overall success. 

# Data Source

https://www.kaggle.com/datasets/carrie1/ecommerce-data 

![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/8fa087f4-2a13-4a49-95ed-a0e8e55e9b35)

The customer dataset in the analysis was obtained from a Kaggle notebook sourced through the UCI Machine Learning Repository. The dataset contains information on various products, their cost and description, quantity purchased, customer ID, and country of purchase. The initial exploration of the dataset involved: 
-	checking and converting data types 
-	checking for and removing null values 
-	dropping duplicate rows 
-	feature extraction and clustering 
-	recency, frequency, and monetary calculations 
The dataset provides valuable insights on when the customer had purchased the order and the number of orders placed which allows us to perform an RFM analysis with ease and create customer segmentation based on that analysis.  

## Installation
### Prerequisites
- Python 3.x
- pip or conda
- Git (for cloning the repository)

## Steps
##### Clone the repository:
git clone https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis.git

##### Navigate to the project directory:
cd Customer-Segmentation-using-RFM-Analysis

##### Install the required dependencies:
pip install -r requirements.txt

##### Storing the data
Download the data from the provided data source and store it in the path data\data

## Data Preprocessing for Customer Segmentation using RFM Analysis

### Overview
This README documents the data preprocessing steps implemented for the Customer Segmentation project using RFM (Recency, Frequency, Monetary) Analysis. The preprocessing script is designed to clean and prepare the dataset for further analysis, ensuring data quality and consistency.

### Features
- Handling missing values by identifying and replacing with NaN
- Reading CSV files with support for different encodings
- Cleaning data by removing duplicates and converting data types
- Filtering the dataset to remove entries with missing CustomerID
#### Prerequisites
- Python 3.x
- Pandas library
- Numpy library
- Matplotlib library
- Seaborn library
Ensure all dependencies are installed using the following command:
- pip install pandas numpy matplotlib seaborn
### How to Use
1. Place your dataset in the same directory as the script, or modify the file_path variable to point to your dataset's location.
2. Run the script using a Python interpreter. This can be done through the command line or using an IDE.
3.The script performs several preprocessing steps:
- Reads the dataset, handling different encodings and missing values.
- Displays various information about the dataset including data types, summary statistics, and missing values.
- Filters out rows with missing CustomerID.
- Converts CustomerID to integer and InvoiceDate to datetime format.
- Removes duplicate rows.
4. After preprocessing, the script saves the cleaned dataset as data_preprocessed.csv in the specified directory.
### Data Dictionary
- InvoiceNo: Invoice number for each transaction.
- StockCode: Item code.
- Description: Item description.
- Quantity: Quantity of each item purchased.
- InvoiceDate: Date and time of the transaction.
- UnitPrice: Price per item unit.
- CustomerID: Customer identifier.
- Country: Customer's country.
Data after replacing missing values for string feature and CustomerID
![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/8500f3e4-d3c1-472e-88a7-daef748314b3)

## RFM Calculation 

### RFM Metric Calculation
- Recency (R): The number of days since the last purchase by the customer. A lower recency value indicates a recent purchase.
- Frequency (F): The total number of transactions made by the customer. A higher frequency indicates a more frequent shopper.
- Monetary (M): The total money spent by the customer. A higher monetary value indicates a higher spender.

### How to Use
1. Ensure your preprocessed dataset is named data_preprocessed.csv and located in the data directory.
2. Run the script. It performs the following steps:
- Reads the preprocessed dataset.
- Calculates Recency, Frequency, and Monetary values for each customer.
- Creates a new DataFrame to hold RFM metrics and removes duplicate entries.
- Visualizes the RFM metrics through scatter plots and a 3D scatter plot to provide insights into customer behavior.

### Visualization
The script includes visualization of RFM metrics to aid in understanding customer segments:

- Scatter plots for Recency vs. Frequency and Frequency vs. Monetary.
- A 3D scatter plot combining all three RFM metrics.

These visualizations help in identifying patterns and segments among customers based on their purchasing behavior.

The RFM metrics are: 
![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/0bd9ac70-cd77-42ee-a622-c17ac8d0fc64)

Visualization of RFM metrics: 

![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/9efe8ae3-3903-4f44-90af-ff3f98570d13)

## RFM Segmentation and Customer Segmentation

It outlines the steps for performing RFM (Recency, Frequency, Monetary) segmentation and customer segmentation using clustering techniques. The process assigns RFM scores based on customer activity, combines these scores to create a single RFM score, and then segments customers into meaningful groups using K-Means clustering.

### Prerequisites
Make sure all dependencies are installed using the following command:
- pip install pandas numpy matplotlib seaborn scikit-learn

### RFM Segmentation Process
- RFM Score Assignment: Customers are scored based on quartiles for each RFM metric. Scores are combined to form a single RFM score.
- Customer Segmentation: Applies K-Means clustering to segment customers based on their RFM scores.
- Segment Profiling: Analyzes and profiles each customer segment by their RFM scores and other relevant attributes.

### How to Use
1. Ensure your dataset is preprocessed and named data_preprocessed.csv.
2. Run the script. It performs the following steps:
- Calculates RFM metrics.
- Assigns scores and creates a combined RFM score.
- Segments customers using K-Means clustering.
- Profiles each segment for deeper insights.

### Segmentation and Profiling
- RFM Segmentation: Assigns quartile-based scores for Recency, Frequency, and Monetary metrics. A combined RFM score is generated for each customer.
- Customer Segmentation: Utilizes K-Means to segment customers into groups. Experimentation with the number of clusters helps find the optimal segmentation.
- Segment Profiling: Customer segments are analyzed to understand the characteristics of each segment. Profiles include average scores and customer counts.

### Visualization
Includes scatter plots and 3D scatter plots to visualize the RFM metrics and customer segments. The Elbow Method is used to determine the optimal number of clusters for segmentation.

### RFM Segmentation 
#### Scoring RFM Metrics: 
![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/6f8bffa2-d3aa-4516-af21-cf181a4da189)
#### Customer Segmentation 
Segmenting customers based on their RFM scores using k-means clustering: 
![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/efbc9b76-d4b9-4b04-bf9a-ea16e36f34e4)
#### Experimenting with different numbers of clusters: 
![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/2bb9b20a-8e7f-4de8-afa0-991cb5d86cc0)
#### Segment Profiling 
![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/c0c44567-6d7b-40ac-aa71-36703a60f46e)

1. Cluster 0: 
- RecencyMean: The average recency score is approximately 2.05, suggesting that customers in this segment made purchases recently. 
- FrequencyMean: The average frequency score is around 2.84, indicating that customers in this segment make purchases moderately frequently. 
- MonetaryMean: The average monetary score is 3.13, suggesting that customers in this segment contribute a relatively high monetary value. 
- CustomerCount: This segment contains 959 customers. 
2. Cluster 1: 
- RecencyMean: The average recency score is approximately 1.38, suggesting that customers in this segment made very recent purchases. 
- FrequencyMean: The average frequency score is around 1.25, indicating that customers in this segment make purchases less frequently. 
- MonetaryMean: The average monetary score is 1.58, suggesting that customers in this segment contribute a relatively low monetary value. 
- CustomerCount: This segment contains 1407 customers. 
3. Cluster 2: 
- RecencyMean: The average recency score is approximately 3.68, suggesting that customers in this segment made purchases less recently. 
- FrequencyMean: The average frequency score is around 3.72, indicating that customers in this segment make purchases quite frequently. 
- MonetaryMean: The average monetary score is 3.72, suggesting that customers in this segment contribute a relatively high monetary value. 
- CustomerCount: This segment contains 1167 customers. 
4. Cluster 3: 
- RecencyMean: The average recency score is approximately 3.36, suggesting that customers in this segment made purchases less recently. 
- FrequencyMean: The average frequency score is around 2.50, indicating that customers in this segment make purchases moderately frequently. 
- MonetaryMean: The average monetary score is 1.60, suggesting that customers in this segment contribute a relatively low monetary value. 
- CustomerCount: This segment contains 805 customers. 
#### Interpretation: 
- Cluster 1 represents recently active but less frequent and lower-value customers. 
- Cluster 2 represents active and frequent customers with higher monetary contributions. 
- Cluster 3 represents less recent, moderately frequent, and lower-value customers. 
This interpretation is based on the average scores for recency, frequency, and monetary values within each cluster. 



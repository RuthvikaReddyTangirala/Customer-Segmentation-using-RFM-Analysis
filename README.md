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

### Marketing Recommendations 
1. Cluster 0: Recent and High-Value Customers Recommendations: 
- Promotional Offers: Offer exclusive promotions or discounts to incentivize repeat purchases from this segment. 
- Loyalty Programs: Introduce a loyalty program to reward these customers for their high-value contributions. 
- New Product Releases: Inform this segment about new product releases to encourage them to make additional purchases. 
2. Cluster 1: Very Recent but Lower-Value Customers Recommendations: 
- Engagement Campaigns: Implement targeted engagement campaigns to encourage more frequent purchases. 
- Upselling Opportunities: Identify opportunities for upselling or cross-selling to increase the average transaction value. 
- Personalized Recommendations: Provide personalized product recommendations based on their recent purchases to increase relevancy. Cluster 2: Active and High-Value Customers Recommendations: 
- Exclusive Access: Provide early access to sales or exclusive products to reward their loyalty. 
- VIP Programs: Establish a VIP program with premium benefits for this segment to enhance their loyalty. 
- Cross-Sell Complementary Products: Suggest complementary products to increase the average transaction value. 
3. Cluster 3: Less Recent and Moderate-Value Customers Recommendations: 
- Reactivation Campaigns: Implement reactivation campaigns to bring these customers back with special offers. 
- Retention Discounts: Offer special discounts for their next purchase to encourage repeat business. 
- Feedback Surveys: Gather feedback to understand reasons for reduced activity and tailor offerings accordingly. 
General Recommendations: 
- Segment-Specific Communication: Tailor marketing communication to each segment's preferences and behaviors. 
- Multichannel Engagement: Utilize various channels such as email, social media, and targeted advertising to reach customers where they are most active. 
- Data-Driven Personalization: Leverage customer data to personalize marketing messages, recommendations, and promotions for each segment. 
- Customer Feedback: Collect feedback from each segment to continuously improve products, services, and overall customer experience. 
- By implementing these tailored strategies, the business can build stronger relationships with each customer segment, enhance customer satisfaction, and optimize revenue generation. Regularly analyzing and adjusting these strategies based on customer feedback and evolving market trends will further contribute to the success of the business. 

### Visualization for RFM Segmentation and Clusters
- Recency Distribution: Bar chart showing the distribution of recency scores across customers.
- Frequency Distribution: Bar chart showing the distribution of frequency scores across customers.
- Monetary Distribution: Bar chart showing the distribution of monetary scores across customers.
- Clusters Based on RFM Scores: Scatter plot illustrating the clustering of customers based on their RFM scores.
- RFM Distribution Scatter Plots: Series of scatter plots comparing Recency vs. Frequency, Frequency vs. Monetary, and Recency vs. Monetary, colored by clusters.
- Heatmap of RFM Distribution and Clusters: Heatmap displaying the average monetary score for each cluster across different recency scores.
  
Ensure you have completed the RFM segmentation and have the rfm_table DataFrame ready, as described in the customer segmentation documentation.

Run the visualization script to generate the charts. Adjust the script as necessary to match your dataset and analysis specifics.

#### Bar chart for Recency distribution, Frequency distribution and Monetary distribution             

![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/c51b3e63-7e14-46fb-ae52-27d6a06b6921)

#### Scatter plot for Clusters 

![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/339e8626-ffb2-4616-b9f7-d30313f3b9dd)

#### Scatter plot for RFM distribution 

![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/c99cdcee-7214-4d83-a54c-7192ca34c938)

#### RFM Distribution and Clusters Heatmap 

![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/78d1987e-3b72-4744-93f2-5ce5097475c8)

## Customer Insights Analysis

### Customer Analysis 

![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/146e61fe-8f4c-4722-b571-592db8200ab7)


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/5674106b-c201-4a68-b3e3-9e8cea9a6a72)

The average number of orders per customer is 4. The minimum no.of orders per customer is 1 and the maximum no.of orders per customer is 209. 

### Product Analysis 


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/917f2fc7-d878-4cf9-933e-4a2ce394fe97)


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/977d2776-25d9-4df0-91c2-3777bd98d8a4)

### Time Analysis 


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/60e5cfc9-b10b-4b2c-9afb-ebbc4e0045f6)

The average order processing time is: 0 days 00:01:20.285854438. The result "0 days 00:01:2 0.285854438" indicates that, on average, there is approximately 1 minute and 20 seconds of p rocessing time between consecutive orders based on the assumption that the processing time i s the time between placing the current order and placing the next one. 


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/b64cf3e0-528a-408c-9370-cf70cadb25ae)

•	As the data contains mostly one year of the data it is hard to determine if there are any seasonalities. 
•	From the given data it can be seen that orders has increased towards the end of the year. 
•	It has increased from the fall season, may be due to start of holiday season. 
•	It has peaked in the month of November, which can be explained with the heavy purchasing during thanksgiving and black Friday season. 

### Geographical Analysis 


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/d23635d3-480f-4a52-b038-678fe4dd6e7e)
![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/c566155f-1464-407b-b75b-8e426daf3225)


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/ceeb91f3-df85-4ebf-86c5-53042c4921d3)

Correlation coefficient of -0.47 suggests a moderate negative correlation between the country of the customer and the number of orders. This implies that, on average, as the number of orders increases for a particular country, the average order value tends to decrease. 


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/729e9c85-9879-4447-85c2-cf5d9d9dccaf)

### Payment Analysis 


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/1c4c3071-500d-492b-9409-1c36ddb82ba9)


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/aeb6848d-8674-46fd-81f6-6419c9546211)


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/71a36e4a-2ca6-43d3-9db1-360c4fa8748d)

Overall Correlation between Payment Methods and Order Amount: 0.1120 

- The overall correlation value between payment methods and the order amount is 0.1121. This value indicates a very weak positive correlation on average. 
- This correlation coefficient is very small, suggesting that there is no significant linear relationship between the payment method and the order amount. 
- In other words, the choice of payment method does not appear to have a substantial impact on the total order amount based on the linear correlation analysis.

### Customer Behaviour 


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/887efd7b-513f-4c5d-a760-f62e13ec8a58)

Recency: 
•	The average recency (mean) is approximately 91 days, suggesting that, on average, customers made their most recent purchase around 91 days ago. 
•	The minimum recency is 0, indicating that some customers made a purchase very recently. 
•	The maximum recency is 373, indicating that some customers made their last purchase a considerable time ago. 
Frequency: 
•	The average frequency (mean) is around 91.86, indicating that, on average, customers made around 92 purchases. 
•	The minimum frequency is 1, indicating that some customers made only one purchase. 
•	The maximum frequency is 7812, indicating that some customers made a very high number of purchases. 
Monetary: 
•	The average monetary value (mean) is approximately 1893.53, suggesting that, on average, customers spent around 1893.53 dollars . 
•	The minimum monetary value is negative (-4287.63), indicating that some customers have negative order values (possibly due to refunds or returns). 
•	The maximum monetary value is 279,489.02 dollars, indicating that some customers have made very high-value purchases. 
Inferences: 
•	There is a wide range of recency, suggesting that there are both recent and long-time customers. 
•	The distribution of frequency indicates that while many customers make a moderate number of purchases, there are also customers who make a very high number of purchases. 
•	The monetary values vary widely, with some customers making high-value purchases. 

### Returns and Refunds 


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/548be506-6000-470a-9994-4ba0450b2eaa)

The return rate of the other category is high compared to the rest of the categories, which shows that they are correlated to an extent.

We can see that there is very less positive and negative correlation between returns and the products which says that there is not much high chance of returning the product based on the categories. 


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/e6b2d61e-707b-4d17-92b2-18d1e935e434)


### Profitability Analysis 


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/59dd835d-1e8c-49d5-8a8c-3dc18c1a4d45)

Total Revenue generated from the products: 8278519.423999998 

### Customer Satisfaction 


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/5409a7c8-8ada-48e4-899e-30f1900fef1e)

Product with the Best Rating: BLUE/NAT SHELL NECKLACE W PENDANT 

Product with the Worst Rating: ASSORTED COLOUR SILK GLASSES CASE 


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/b04d4a37-501a-4d1d-9463-f80daaa9df9b)


![image](https://github.com/RuthvikaReddyTangirala/Customer-Segmentation-using-RFM-Analysis/assets/113473457/2555af53-fab9-4fb5-bffc-9bf6b1711976)

Average Sentiment: 0.316849944223663 

The average sentiment score of approximately 0.32 suggests that, on average, the sentiment expressed in the feedback column is positive. 

With an average sentiment score of 0.32: 
The majority of the predefined comments associated with star ratings are leaning towards positive expressions. Customers, on average, use language in the comments that reflects a positive sentiment or satisfaction. 

## SUMMARY 

Customer cluster analysis reveals three segments based on recency, frequency, and value. Cluster 1: recently active but less frequent/lower value customers - needs targeted engagement. Cluster 2: highly valuable, active, regular customers - need personalized strategies. Cluster 3: less recent, moderately frequent, lower-value customers - need reactivation efforts. 
 
To make the most of insights: 
1.	Tailor marketing communication for each segment and use a multichannel approach. 
2.	Personalize messages, recommendations, and promotions with customer data. 
3.	Collect feedback from each segment for continuous improvement. 
 
"WHITE HANGING HEART T-LIGHT HOLDER" is the most purchased product among the top 10, while "PAPER CRAFT, LITTLE BIRDIE" generates the highest revenue. Use this information to guide inventory management and promotions for better business success. Order processing time takes around 1 minute and 20 seconds between consecutive orders. Apple Pay is the most common payment method, but it has a weak correlation with order amount. 
 
On average, customers are active for about 13 days and 18 hours. The customer base is diverse, with moderate and high purchase frequency and varying monetary values. Finally, the average sentiment score of 0.32 from customer feedback suggests a generally positive tone in the comments associated with star ratings. This indicates that customers express satisfaction and positive experiences in their feedback. These insights help understand customer behavior, preferences, and satisfaction levels, offering guidance for business strategies and improvements. 
 
LIMITATIONS AND FUTURE WORK 
 
It is important to take into account the various constraints of the analysis. First off, the caliber of the dataset used has a significant impact on the caliber of the outcomes. Any errors, omissions, or discrepancies in the dataset might jeopardize the reliability of the conclusions. Furthermore, the dataset's very short time span—December 1, 2010 to December 9, 2011—may make it difficult to identify long-term patterns or seasonality, which might restrict the capacity to gather thorough observations on consumer behavior. In addition, a complete profitability analysis is impeded by the lack of cost information for the items, which makes it difficult to compute profit margins and evaluate the products' overall financial health. 

In order to improve the study and overcome these constraints, future work should concentrate on enhancing data quality by means of stringent cleaning and validation procedures. A more comprehensive assessment of trends and patterns might be possible by extending the dataset's coverage span. To ensure a thorough profitability analysis, real product cost information must be included. It is best to use actual payment method data rather than estimated possibilities in order to comprehend client payment preferences. In addition, adding real customer evaluations and comments might help future analyses do sentiment analysis more accurately. More sophisticated client segmentation strategies might be investigated, and dynamic product categorization techniques like natural language processing can take the place of the conventional keywordbased strategy. 

For any questions or further information, please reach out to Ruthvika Reddy Tangirala at ruthvikareddytangirala20@gmail.com (or) through LinkedIn www.linkedin.com/in/ruthvikareddytangirala

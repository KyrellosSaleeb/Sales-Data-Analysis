import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



#Step 1: Load the Data
File_Path = "D:\Data Track\Data Analysis\Projects\Sales_Data_Project.csv"

Data  = pd.read_csv(File_Path)


#1.1: investigate the data
print(Data.info())
print(Data.head())
print(Data.head(0))
print(Data.head(1))

#Step 2: Data Cleaning and Preparation
#2.1: Check for Missing Values
print(Data.isnull().sum())

#2.2: Check for Duplicates:
print(Data.duplicated())


#2.3: Ensure Correct Data Types:
print(Data.dtypes)
print(Data.info())
print(Data['Date'].dtypes)
Data['Date'] = pd.to_datetime(Data['Date'])
print(Data['Date'].dtypes)
print(Data.dtypes)
print(Data.info())

#2.4: Create a New Column for Total Profit= Profit Margin * Revenue
Data['Total Profit'] = Data['Revenue'] * Data['Profit Margin'] 
print(Data.info())


filtered_data = Data[Data['Date'] >= '2023-06-01']
print(filtered_data)


#Step 3: Exploratory Data Analysis (EDA)
#3.1: Descriptive Statistics
print(Data.describe())

def IQR_fun(DataFrame, Column):
    Q1 = DataFrame[Column].quantile(0.25)
    Q3 = DataFrame[Column].quantile(0.75)
    IQR = Q3 - Q1
    
    # Define bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    
    outliers = DataFrame[(DataFrame[Column] < lower_bound) | (DataFrame[Column] > upper_bound)]
    filtered_data = DataFrame[(DataFrame[Column] >= lower_bound) & (DataFrame[Column] <= upper_bound)]

    return outliers, filtered_data

plt.figure(figsize=(8, 6))  # Set figure size
plt.boxplot([Data['Units Sold'],Data['Unit Price'],Data['Revenue'],Data['Profit Margin'],Data['Total Profit']], labels=['Units Sold','Unit Price','Revenue','Profit Margin','Total Profit']) 
plt.title("Multiple Boxplots")
plt.ylabel("Values")
plt.show()

print('\n\n\n\n\n\nUnits Sold')
print(IQR_fun(Data,'Units Sold'))

print('Units Price')
print(IQR_fun(Data,'Unit Price'))

print('Revenue')
print(IQR_fun(Data,'Revenue'))

print('Profit Margin')
print(IQR_fun(Data,'Profit Margin'))

print('Total Profit')
print(IQR_fun(Data,'Total Profit'))


#3.2: Trend Analysis:
plt.fill_between(Data['Date'], Data['Revenue'], color='skyblue', alpha=0.5)
plt.title("Date vs Revenue")
plt.show()

plt.bar(Data['Region'],Data['Units Sold'])
plt.title("Region vs Units Sold")
plt.show()

#3.3: Top Products:
plt.bar(Data['Product'],Data['Units Sold'])
plt.title("Product vs Units Sold")
plt.show()

plt.bar(Data['Product'],Data['Revenue'])
plt.title("Products vs Revenue")
plt.show()

#3.3: Top Products
plt.bar(Data['Product'],Data['Profit Margin'])
plt.title("Products vs Profit Margin'")
plt.show()

Products_group = Data.groupby('Product').agg(
    total_revenue =('Revenue', 'sum'),
    total_Units =('Units Sold', 'sum')).reset_index()
print(Products_group)
"""
B>A>C>D Top Products vs revenue
"""


#3.4:Region Analysis
result = Data.groupby('Region').agg(
    Avg_ProfitMargin=('Profit Margin', 'mean'),
    Total_Revenue=('Revenue', 'sum')
).reset_index()
print(result)

region_revenue = Data.groupby('Region')['Revenue'].sum().reset_index()

#3.5: Correlation Analysis
plt.bar(region_revenue['Region'],region_revenue['Revenue'])
plt.title("regional distribution of revenue")
plt.show()

correlation_matrix = Data.corr()
print(correlation_matrix)
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()




#Step 4: Advanced Analysis
#4.1: Time Series Analysis:
Data['Date_M'] = Data['Date'].dt.to_period('M')
Data['Date_W'] = Data['Date'].dt.to_period('W')

Monthly_Group = Data.groupby('Date_M').agg(
    Total_Rev = ('Revenue','sum'),
    Total_units = ('Units Sold', 'sum')).reset_index()

Weekly_Group = Data.groupby('Date_W').agg(
    Total_Rev = ('Revenue','sum'),
    Total_units = ('Units Sold', 'sum')).reset_index()

print(Monthly_Group)
print(Weekly_Group)


plt.plot(Data['Date_M'].astype(str))
plt.title('Monthly Revenue Trends', fontsize=16)
plt.show()



#4.2: Profitability Analysis
Data['Profit_Percentage'] = ((Data['Profit Margin']*100) / Data['Revenue']) * 100
Profit_Group_Region = Data.groupby(['Region','Product']).agg(
    Avg_Profit_Percentage= ('Profit_Percentage','mean'),
    Total_Revenue = ('Revenue','sum')).reset_index()
print(Profit_Group_Region)




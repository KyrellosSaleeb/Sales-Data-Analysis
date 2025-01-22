# Sales Data Analysis Project

This repository contains a Python-based project for performing exploratory data analysis (EDA) on a sales dataset. The project includes steps to investigate the data, check for issues like missing values and duplicates, perform statistical analysis, and visualize key metrics.

## Features

1. **Data Investigation**
   - Displaying dataset information.
   - Viewing the first few rows of the dataset.

2. **Data Cleaning**
   - Checking for missing values.
   - Identifying duplicate entries.
   - Creating a new column for total profit.

3. **Statistical Analysis**
   - Generating descriptive statistics.
   - Identifying outliers using the Interquartile Range (IQR) method.

4. **Data Visualization**
   - Boxplots for key metrics like units sold, unit price, revenue, profit margin, and total profit.
   - Line plot for revenue over time.
   - Bar charts for product and region-wise performance.
   - Heatmap for correlation analysis.

5. **Insights and Grouped Analysis**
   - Aggregated metrics for products (e.g., total revenue, total units sold).
   - Region-wise analysis (e.g., average profit margin, total revenue).
   - Correlation matrix to understand relationships between metrics.

## Dependencies

The project uses the following Python libraries:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `csv`

Install these dependencies using pip:
```bash
pip install numpy pandas matplotlib seaborn
```

## Files
  * Sales_Data_Project.csv: Input data file containing sales data.
  * main.py: Python script containing all the code for data analysis and visualization.

## Key Functions
IQR_Calculate(DataFrame, Column)
This function calculates the interquartile range for a specified column in a DataFrame, identifies outliers, and returns the filtered data.

Parameters:
  * DataFrame: The input DataFrame.
  * Column: The column to calculate IQR for.

Returns:  
  * outliers: Rows with outlier values.
  * filtered_data: Data without outliers.
  
## Visualizations
The project generates several visualizations:

  * Boxplots for identifying outliers in key metrics.
  * Line plots and bar charts for trends and comparisons.
  * Heatmaps to visualize correlations between variables.

## Insights
The project helps derive valuable insights from the sales data, such as:

  * Top-performing products and regions.
  * Relationships between revenue, profit margin, and other variables.
  * Identification of outliers for further investigation.

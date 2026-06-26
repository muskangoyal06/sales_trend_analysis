# Sales Trend Analysis

This project analyzes sales data to identify trends, understand data quality, and prepare the dataset for further analysis and visualization.

The project uses Python and Pandas to load, inspect, and clean the dataset before performing exploratory data analysis.

# Dataset
Dataset: Superstore Sales Dataset

The dataset contains information about:

* Orders
* Customers
* Products
* Sales
* Profit
* Regions
* Shipping details

# Technologies Used

* Python
* Pandas
* Visual Studio Code

# Project Setup

1. Clone the repository.
2. Open the project folder in Visual Studio Code.
3. Create and activate a virtual environment.
4. Install the required packages.

```bash
pip install pandas
```
# Data Loading
Completed the following tasks:

* Imported the Pandas library.
* Loaded the CSV file into a DataFrame.
* Displayed sample records using `head()`.
* Displayed all column names.
* Verified column data types.

# Data Cleaning
# Step 1: Missing Value Analysis
Performed missing value detection across the entire dataset.

Steps performed:

1. Identified missing values using Pandas.
2. Counted missing values for each column.
3. Filtered columns containing at least one missing value.
4. Calculated the percentage of missing values.
5. Rounded percentages to two decimal places.

NOTE: 
1. Replace every value with:
Missing? -> True
Not Missing? -> False
2. Convert:
True -> 1
False -> 0
3. Add all the 1s in each column
Result: Number of missing values per column

# Findings

| Column      | Missing Values | Missing Percentage |
| ----------- | -------------- | ------------------ |
| Postal Code | 11             | 0.11%              |

# Investigation

The records with missing Postal Codes were examined to verify whether other location information was available.
The following fields were still populated:

* City
* State
* Region

# Decision

The Postal Code column contained 11 missing values, representing 0.11% of the dataset.
Since Postal Code is not required for sales trend analysis, product analysis, profit analysis, or regional analysis, the missing values were retained and excluded from any postal code-specific analysis.

# Step 2: Duplicate Record Check
Performed a duplicate record check to identify any repeated rows in the dataset.

# Step 3: Data Type Verification
Reviewed all column data types to ensure they are appropriate for analysis.

# Step 4: Date Conversion
Identified that the following date columns were stored as object (string) data types:
* Order Date
* Ship Date

The dataset uses the format:

```text
dd/mm/yyyy
```
Examples:

```text
08/11/2017
12/06/2017
11/10/2016
```

Both date columns were converted to datetime format to support time-series analysis and trend calculations.







## Upcoming Work

The following tasks are planned:

### Sales Analysis

* Calculate total sales.
* Calculate monthly sales trends.
* Identify top-selling products.
* Identify top-performing regions.

### Data Visualization

* Sales by month.
* Sales by category.
* Profit by region.

### Business Insights

Generate business insights based on the analysis results.

## Repository Structure

```text
Sales-Trend-Analysis/
│
├── README.md
├── train.csv
├── data_cleaning.py
├── sales_analysis.py
├── sales_trend_visualization.py
├── main.py
├── visualizations/
│   ├── monthly_sales.png
│   ├── yearly_sales.png
│   ├── category_sales.png
│   └── orders_by_region.png
└── requirements.txt
```

## Status

Project Status: In Progress

Current Phase: Data Cleaning and Preparation

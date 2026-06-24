
#Step 1: Import the CSV module
import pandas as pd

#Step 2: Read the CSV file
df = pd.read_csv("D:/Python Projects/Sales Trend Analysis/train.csv")
    
#Step 3: Print the dataframe
print(df.head())

#Print all the column names
print(df.columns)

#Identify missing values
df_null = df.isnull()

#print the table with values True or False to identify if there are missing values.
#True - missing value
#False - no missing value
print(df_null)

#count the number of missing values in each column
df_null_columns = df_null.sum()

#Find columns that have atleast one missing value
df_null_columns = df_null_columns[df_null_columns > 0]
print(df_null_columns)

#Calculate the percentage of missing values
df_null_columns_percentage = (df_null_columns / len(df)) * 100

#Round it to nearest 2 decimal points
df_null_columns_percentage = df_null_columns_percentage.round(2)
print(df_null_columns_percentage)

#Verify that City, Region and State are still present for those rows where Postal Code is Null
print(df[df['Postal Code'].isnull()][['City', 'State','Region','Postal Code']])

#Check for dupliacte rows
df_duplicate = df.duplicated().sum()
print(df_duplicate)

#Check data types
print(df.dtypes)

#Inspect the dates
print(df[['Order Date','Ship Date']].head())

#Convert to Datetime
df['Order Date'] = pd.to_datetime(df['Order Date'],format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'],format='%d/%m/%Y')

print(df.dtypes)

#Calculate total slaes
total_sales = df['Sales'].sum()
print(f"Total Sales: {total_sales}")

#Calculate monthly sales
#Extract month
df['Month'] = df['Order Date'].dt.month_name()
print(df['Month'].head())

#Group the sales by the month
grouped_month = df.groupby('Month')

#sum all the sales in each group which will lead to monthly slaes
monthly_sales = round(grouped_month['Sales'].sum(),2)
print("Monthly Sales: ", monthly_sales)

#Calculate yearly sales
#Extract year
df['Year'] = df['Order Date'].dt.year
print(df['Year'].head())

#Group the sales by the year
grouped_year = df.groupby('Year')

#sum all the sales in each group which will lead to yearly slaes
yearly_sales = round(grouped_year['Sales'].sum(),2)
print("Yearly Sales: ", yearly_sales)


#Top Selling Products
#group by product names
grouped_products = df.groupby('Product Name')

#sales per product
product_sales = grouped_products['Sales'].sum()
print(product_sales.head())

#sort in descending order
top_product_sales = product_sales.sort_values(ascending = False)
print(top_product_sales.head())

#Top Regions
#group by region names
grouped_regions = df.groupby('Region')

#sales per region
region_sales = grouped_regions['Sales'].sum()
print(region_sales.head())

#sort in descending order
top_region_sales = region_sales.sort_values(ascending = False)
print(top_region_sales.head())
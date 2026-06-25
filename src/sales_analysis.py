import data_cleaning
import pandas as pd

#Function for calculating the total sales
def calculate_total_sales(df):
    #Calculate total slaes
    total_sales = df['Sales'].sum().round(2)
    return total_sales
      
    
#Function for calculating monthly sales
def calculate_monthly_sales(df):
    #Extract month
    df['Month'] = df['Order Date'].dt.month
    

    #Group the sales by the month
    grouped_month = df.groupby('Month')

    #sum all the sales in each group which will lead to monthly slaes
    monthly_sales = round(grouped_month['Sales'].sum(),2)
    return monthly_sales
    
    
#Function for calculating yearly sales
def calculate_yearly_sales(df):
    #Extract year
    df['Year'] = df['Order Date'].dt.year

    #Group the sales by the year
    grouped_year = df.groupby('Year')

    #sum all the sales in each group which will lead to yearly slaes
    yearly_sales = round(grouped_year['Sales'].sum(),2)
    return yearly_sales    

    
#Function for analysing the top selling products
def analyse_top_selling_products(df):
    #group by product names
    grouped_products = df.groupby('Product Name')

    #sales per product
    product_sales = grouped_products['Sales'].sum()

    #sort in descending order
    top_product_sales = product_sales.sort_values(ascending = False)
    return top_product_sales  
       
       
#Function for analysing the top regions with maximum sales
def analyse_top_region(df):
    #group by region names
    grouped_regions = df.groupby('Region')

    #sales per region
    region_sales = grouped_regions['Sales'].sum()

    #sort in descending order
    top_region_sales = region_sales.sort_values(ascending = False)
    return top_region_sales   
    
    
#Function for generating sales analysis report        
def generate_sales_analysis_report(df):
    
    print("\n\t\t\t Sales Analysis Report")
    
    total_sales = calculate_total_sales(df)
    print(f"\nTotal Sales: {total_sales}")
    
    monthly_sales = calculate_monthly_sales(df)
    print(f"\nMonthly Sales: {monthly_sales}")
    
    yearly_sales = calculate_yearly_sales(df)
    print(f"\nYearly Sales: {yearly_sales}")
    
    top_selling_products = analyse_top_selling_products(df)
    print(f"\nTop Selling products:\n\n {top_selling_products.head(10)}") 
    
    top_regions = analyse_top_region(df)
    print(f"\nTop Regions:\n\n {top_regions.head()}")
    
    
if __name__ == "__main__":
    
    file_path = "D:/Python Projects/Sales Trend Analysis/data/train.csv"
    df = data_cleaning.load_data(file_path)
    data_cleaning.analyse_missing_values(df)
    data_cleaning.duplicate_data(df)
    df = data_cleaning.date_conversion(df)
    generate_sales_analysis_report(df)
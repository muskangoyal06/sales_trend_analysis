from data_cleaning import load_data, generate_data_quality_report
from sales_analysis import calculate_monthly_sales, calculate_yearly_sales
import pandas as pd
import matplotlib.pyplot as plt

file_path = file_path = "D:/Python Projects/Sales Trend Analysis/data/train.csv"

df = load_data(file_path)
df = generate_data_quality_report(df)

print(df.head())

# ==================================================
# VISUALIZATION 1: SALES BY MONTH
# ==================================================


#import monthly_sales from the sales analysis file
monthly_sales = calculate_monthly_sales(df)

#currently month is the index, we need to add a new numeric index 
monthly_sales = monthly_sales.reset_index()
print(monthly_sales.head())

#to change the month cloumn to month names
#convert it to date time type first and then convert to month name
monthly_sales['Month'] = pd.to_datetime(monthly_sales['Month'], format='%m').dt.month_name()

#check the datatype of the columns
print("Before Conversion\n", monthly_sales.dtypes)
print(type(monthly_sales['Month'].iloc[0]))

#assigning the figure size of the graph
plt.figure(figsize = (10,5))

#plotting the line graph mentioning between which values
plt.plot(monthly_sales['Month'], monthly_sales['Sales'])

for x,y in zip(monthly_sales['Month'], monthly_sales['Sales']):
    plt.annotate(str(y), (x,y), textcoords="offset points", xytext = (0, 8), ha = "center", rotation = 45)

#Rotate the xaxis labels
plt.xticks(rotation = 90)

#assigning titale to the graph
plt.title("Total Sales v/s Month")

#Assigning labels to x-axis and y-axis
plt.xlabel("Month")
plt.ylabel("Total Sales")

#tightening the layout for spacing issues
plt.tight_layout()

#showing the graph
plt.show()

# ==================================================
# VISUALIZATION 1: SALES BY YEAR
# ==================================================

#import yearly_sales from the sales analysis file
yearly_sales = calculate_yearly_sales(df)

#currently year is the index, we need to add a new numeric index 
yearly_sales = yearly_sales.reset_index()

#Sort the years
yearly_sales = yearly_sales.sort_values("Year")
print(yearly_sales.head())

#assigning the figure size of the graph
plt.figure(figsize = (5,5))

#plotting the line graph mentioning between which values
plt.plot(yearly_sales['Year'], yearly_sales['Sales'])

for x,y in zip(yearly_sales['Year'], yearly_sales['Sales']):
    plt.annotate(str(y), (x,y), textcoords="offset points", xytext = (0, 8), ha = "center", rotation = 45)

#Rotate the xaxis labels
plt.xticks(rotation = 90)

#assigning titale to the graph
plt.title("Total Sales v/s Year")

#Assigning labels to x-axis and y-axis
plt.xlabel("Year")
plt.ylabel("Total Sales")

#tightening the layout for spacing issues
plt.tight_layout()

#showing the graph
plt.show()

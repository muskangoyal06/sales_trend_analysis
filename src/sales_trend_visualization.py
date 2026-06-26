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
# VISUALIZATION 2: SALES BY YEAR
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


# ==================================================
# VISUALIZATION 3: SALES BY CATEGORY
# ==================================================

#Group the sales by the category
grouped_category = df.groupby('Category')

#sum all the sales in each group which will lead to categorical sales
categorical_sales = round(grouped_category['Sales'].sum(), 2)

print(categorical_sales)

#Reset the index
categorical_sales = categorical_sales.reset_index()

#assigning the figure size of the graph
plt.figure(figsize = (5,5))

#Generate different colors automatically
colors= plt.cm.tab10(range(len(categorical_sales)))

#plot the bar graph
plt.bar(categorical_sales['Category'], categorical_sales['Sales'], color = colors)

#Provide the total sales value on top of each chart
for x,y in zip(categorical_sales['Category'], categorical_sales['Sales']):
    plt.annotate(str(y), (x,y), ha = 'center', textcoords= 'offset points', xytext = (0,8))
    
#Give it a tile
plt.title("Total Sales v/s Category")

#Give label
plt.xlabel("Category")
plt.ylabel("Total Sales")

#tighten the layout for spacing
plt.tight_layout()

#Show the bar graph
plt.show()


# ==================================================
# VISUALIZATION 4: ORDER BY REGION
# ==================================================

#group the regions together
grouped_region = df.groupby('Region')

#count number of orders in each region
region_orders = grouped_region['Order ID'].count() 

#reset index
region_orders = region_orders.reset_index()

print(region_orders)

#assign figure size
plt.figure(figsize = (12.5,5))

#different colors
colors = plt.cm.tab10(range(len(region_orders)))

#plot horizontal bar chart
plt.barh(region_orders['Region'], region_orders['Order ID'], color = colors)

#Provide the total number of orders on top of each chart
for x,y in zip(region_orders['Region'], region_orders['Order ID']):
    plt.annotate(str(y), (y,x), va = 'center', textcoords= 'offset points', xytext = (8,0))

#assign title
plt.title("Total Orders v/s Region")

#assignlabels
plt.xlabel("Total Orders")
plt.ylabel("Region")

#show the horizonatl bar chart
plt.show()

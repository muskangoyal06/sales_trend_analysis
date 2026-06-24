import pandas as pd


#Function for loading data
def load_data(file_path):
    #read the csv file
    df = pd.read_csv(file_path)
    return df
    
    
#Function for analysing missing values
def analyse_missing_values(df):
    #Display missing counts
    missing_counts = df.isnull().sum()
    missing_counts = missing_counts[missing_counts>0]
    
    
    
    #Calculate the percentage of missing values
    missing_percent = round((missing_counts/len(df)) * 100, 2)
    
    return missing_counts, missing_percent
    
    
    
#Function for verifying missing postal code
def postal_code_missing(df):
    
    #verify data whe postal code is null
    #verify if the city, region and state is present for the missing postal codes
    missing_postal = df[df['Postal Code'].isnull()]
    return missing_postal
    
    
#Function for dropping duplicate values if present  
def duplicate_data(df):
    
    #check if any duplicate rows are present
    duplicate = df.duplicated()
    #count how many duplicate rows are present
    total_duplicates = duplicate.sum()
    
    return total_duplicates
    
  
        
#Function for date conversion     
def date_conversion(df):
    
    #Date columns
    date_columns = ['Order Date', 'Ship Date']
    
    #Convert to Datetime using a single loop for updating both the columns
    for value in date_columns:
        df[value] = pd.to_datetime(df[value],format='%d/%m/%Y')
    
    return df


#Function for generating data quality report
def generate_data_quality_report(df):
    
    
    print("\n\t\t Data Quality Report \n")
    print(df.head())
    print(df.columns)
    
    
    missing_values, missing_percent = analyse_missing_values(df)
    if missing_values.empty:
        print("No missing values found")
    else:
        print("\nMissing values: ", missing_values)
    
    print("\nMissing values percentage: ", missing_percent)
    
    
    missing_postal = postal_code_missing(df)
    #check if the missing_postal data is empty i.e. there is no missing postal codes
    if not missing_postal.empty:
        print("\nRows with missing Postal Code: ",)
        print("\n", missing_postal[['City', 'State', 'Region']])
    else:
        print("\nNo postal codes missing")
    
    
    total_duplicates = duplicate_data(df)
    if total_duplicates > 0:
        print(f"\nNumber of duplicate rows present: {total_duplicates}")
        print("\n Removing duplicate rows")
        df = df.drop_dupliactes()   
    else:
        print("\nNo duplicate rows found.")
    
    
    print("\n Data types brfore conversion: ", df.dtypes)
    df = date_conversion(df)
    print("\n Date types after conversion: ", df.dtypes)
    
    
    
if __name__ == "__main__":

    file_path = "D:/Python Projects/Sales Trend Analysis/data/train.csv"
    df = load_data(file_path)
    generate_data_quality_report(df)
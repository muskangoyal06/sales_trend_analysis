import data_cleaning
import sales_analysis

def main():
    
    file_path = "D:/Python Projects/Sales Trend Analysis/data/train.csv"
    df = data_cleaning.load_data(file_path)
    
    # Data quality report
    data_cleaning.generate_data_quality_report(df)
    sales_analysis.generate_sales_analysis_report(df)
    
    
if __name__ == "__main__":
    main()
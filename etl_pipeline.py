import pandas as pd
import numpy as np

def create_dummy_data():
    """
    Creates a dummy dataset with intentional errors for testing.
    """
    data = {
        'order_id': [101, 102, 103, 104, 102, 105],
        'customer': ['Alice', 'Bob', 'Charlie', 'David', 'Bob', 'Eve'],
        'amount': [250, 500, np.nan, 750, 500, 300],
        'date': ['2023-01-01', '01/02/2023', '2023-01-03', '2023-01-04', '01/02/2023', '2023-01-05']
    }
    df = pd.DataFrame(data)
    df.to_csv('raw_sales_data.csv', index=False)
    print("✅ Dummy data created.")

def clean_data(file_path):
    """
    Reads a CSV file, cleans the data, and returns a clean DataFrame.
    """
    # Extract
    df = pd.read_csv(file_path)
    
    # Transform: Drop missing values
    df = df.dropna()
    
    # Transform: Standardize dates (using mixed format handling)
    df['date'] = pd.to_datetime(df['date'], format='mixed')
    
    # Transform: Remove duplicates
    df = df.drop_duplicates()
    
    return df

if __name__ == "__main__":
    # 1. Create the data
    create_dummy_data()
    
    # 2. Run the pipeline
    print("🚀 Starting ETL Pipeline...")
    clean_df = clean_data('raw_sales_data.csv')
    
    # 3. Load (Save)
    clean_df.to_csv('clean_sales_data.csv', index=False)
    
    print(f"✅ Pipeline Finished! Saved {clean_df.shape[0]} clean rows.")

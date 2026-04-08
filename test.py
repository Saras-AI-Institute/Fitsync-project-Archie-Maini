import pandas as pd  # REQUIRED if handling pandas-specific exceptions
from modules.processor import load_data

try:
    # Attempt to load the data
    df = load_data()
    
    # Check if DataFrame is returned properly
    if df is not None:
        print(df.head(20))
    else:
        print("The DataFrame returned by load_data() is None.")
except FileNotFoundError:
    print("The CSV file was not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("The CSV file is empty.")
except pd.errors.ParserError:
    print("There was an error parsing the CSV file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    print(f"An unexpected error occurred: {e}")
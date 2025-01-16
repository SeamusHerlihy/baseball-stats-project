# Baseball Stats Project
# Author: Seamus Herlihy

import pandas as pd

def load_data(filepath):
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        print("CSV file not found. Please ensure the file is in the correct location.")
        return None

def filter_data(data, column, min_value=None, max_value=None):
    if column not in data.columns:
        print(f"Column '{column}' not found in data.")
        return None
    
    filtered_data = data
    if min_value is not None:
        filtered_data = filtered_data[filtered_data[column] >= min_value]
    if max_value is not None:
        filtered_data = filtered_data[filtered_data[column] <= max_value]
    
    return filtered_data

def main():
    filepath = "data/C.csv"
    data = load_data(filepath)
    if data is None:
        return
    
    print("Available columns:", list(data.columns))

    column = input("Enter the column to filter by: ").strip()
    min_value = input("Enter minimum value (or press Enter to skip): ").strip()
    max_value = input("Enter maximum value (or press Enter to skip): ").strip()

    try:
        min_value = float(min_value) if min_value else None
        max_value = float(max_value) if max_value else None
    except ValueError:
        print("Invalid numeric input.")
        return
    
    filtered_data = filter_data(data, column, min_value, max_value)
    if filtered_data is not None:
        print(filtered_data)

if __name__ == "__main__":
    main()

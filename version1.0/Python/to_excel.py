import pandas as pd

def csv_to_excel_limited_rows(input_csv_path, output_excel_path, row_limit=900000):
    # Load the CSV file
    df = pd.read_csv(input_csv_path)
    
    # Select only the 'device_profile_id' and 'e_data' columns
    selected_columns = df[['device_profile_id', 'e_data']]
    
    # Limit the number of rows to row_limit
    limited_rows = selected_columns.head(row_limit)
    
    # Write the limited rows to an Excel file
    limited_rows.to_excel(output_excel_path, index=False)

# Example usage
input_csv_path = '~/Documents/Projects/data_science/smart_campus_hit/data/main_data_frame_cleaned.csv'  # Replace with the path to your input CSV file
output_excel_path = '~/Documents/Projects/data_science/smart_campus_hit/data/pivot.xlsx'  # Replace with your desired output Excel file path

# Call the function with row limit
csv_to_excel_limited_rows(input_csv_path, output_excel_path)
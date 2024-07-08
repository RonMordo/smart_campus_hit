import pandas as pd
import json

def load_and_analyze_data(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)
    
    # Safely convert 'e_data' from JSON-formatted string to dictionary
    df['e_data_dict'] = df['e_data'].apply(lambda x: json.loads(x) if pd.notnull(x) else {})
    
    # Define a function to extract unique keys across all 'e_data_dict' entries for a given sensor
    def extract_unique_keys(e_data_list):
        unique_keys = set()
        for e_data in e_data_list:
            unique_keys.update(e_data.keys())
        return unique_keys
    
    # Group by 'device_profile_id' and apply the function to extract unique keys
    sensor_measurements = df.groupby('device_profile_id')['e_data_dict'].apply(lambda x: extract_unique_keys(x))
    
    return sensor_measurements

# Example usage
file_path = '~/Documents/Projects/data_science/smart_campus_hit/data/main_data_frame_cleaned.csv'  # Replace with the actual file path
sensor_measurements = load_and_analyze_data(file_path)
sensor_measurements.to_csv('~/Documents/Projects/data_science/smart_campus_hit/data/deviceID_edata_pivot.csv')
print(sensor_measurements)

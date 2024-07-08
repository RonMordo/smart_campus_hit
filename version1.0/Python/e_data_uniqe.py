import pandas as pd

# Replace 'your_file_path.csv' with the path to your large dataset
file_path = '~/Documents/Projects/data_science/smart_campus_hit/data/main_data_frame_cleaned.csv'

# Load the CSV file
df = pd.read_csv(file_path)

# Count the number of unique entries in the 'e_data' column
unique_rows_e_data = df['device_profile_id'].nunique()

# Print the number of unique rows
print(f'Number of unique rows in the e_data column: {unique_rows_e_data}')

import pandas as pd
import json

# Convert 'e_data' from JSON-formatted string to dictionary
df['e_data'] = df['e_data'].apply(json.loads)

# Function to aggregate unique keys from 'e_data' for each sensor
def aggregate_keys(series):
    keys = set()
    for item in series:
        keys.update(item.keys())
    return list(keys)

# Group by 'device_profile_id' and aggregate unique keys in 'e_data'
sensor_measurements = df.groupby('device_profile_id')['e_data'].agg(aggregate_keys)

# Convert the series to a dataframe for easier reading
sensor_measurements_df = sensor_measurements.reset_index()
sensor_measurements_df.rename(columns={'e_data': 'measured_parameters'}, inplace=True)
sensor_measurements_df.to_csv('~/Documents/Projects/data_science/smart_campus_hit/data/sensor_mesurements.csv')

# Display the result
print(sensor_measurements_df)

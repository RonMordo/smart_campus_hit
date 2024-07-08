import pandas as pd
import json

PATH = 'data/main_data_frame_cleaned.csv'

# Load the dataset
file_path = PATH  # Update this to your CSV file path
data = pd.read_csv(file_path)

# Convert 'e_data' from JSON string to dictionary and extract relevant metrics
data['e_data_dict'] = data['e_data'].apply(lambda x: json.loads(x))
data['ambient_temperature'] = data['e_data_dict'].apply(lambda x: x.get('data_ambient_temperature', None))
data['relative_humidity'] = data['e_data_dict'].apply(lambda x: x.get('data_relative_humidity', None))

# Pivot Data on Room Number and Sensor Type
pivot_table_room_type = pd.pivot_table(data, index='room_number', columns='type', aggfunc='size', fill_value=0)

# Aggregate Sensor Data by Type
aggregated_data = data.groupby('type').agg({
    'ambient_temperature': ['mean', 'min', 'max'],
    'relative_humidity': ['mean', 'min', 'max']
}).reset_index()

# Optional: Save the pivoted and aggregated data to new CSV files
pivot_table_room_type.to_csv('pivot_table_room_type.csv')
aggregated_data.to_csv('aggregated_sensor_data.csv')

print("Pivot and aggregation complete. Results saved to 'pivot_table_room_type.csv' and 'aggregated_sensor_data.csv'.")

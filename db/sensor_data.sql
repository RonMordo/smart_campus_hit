CREATE TABLE sensor_data (
    sensor_data_id SERIAL PRIMARY KEY,
    e_data json NOT NULL,
    location_type NUMERIC NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT NULL,
    sensor_id NUMERIC NOT NULL,
    location_id INTEGER NOT NULL,
    FOREIGN KEY (location_id) REFERENCES join_location_id(location_id)
);

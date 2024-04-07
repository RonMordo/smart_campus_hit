CREATE TABLE outside_location (
    location_id SERIAL PRIMARY KEY NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    height FLOAT NOT NULL,
    FOREIGN KEY (location_id) REFERENCES join_location_id(location_id)
);

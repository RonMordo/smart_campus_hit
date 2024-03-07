CREATE TABLE sensors (
    sensor_id SERIAL PRIMARY KEY,
    highet NUMERIC NOT  NULL,
    angle NUMERIC NOT  NULL,
    distance_from_entrance NUMERIC NOT NULL,
    sensor_type VARCHAR(255) NOT NULL,
    room_id INTEGER NOT NULL
);
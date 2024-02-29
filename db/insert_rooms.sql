CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    building_number INTEGER NOT NULL,
    floor INTEGER NOT NULL,
    room_type VARCHAR(255) NOT NULL
);
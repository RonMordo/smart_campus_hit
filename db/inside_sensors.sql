CREATE TABLE inside_location (
    location_id SERIAL PRIMARY KEY NOT NULL,
    height FLOAT NOT NULL,
    angle FLOAT NOT NULL,
    distance_from_entrance FLOAT NOT NULL,
    room_id INTEGER NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id),
    FOREIGN KEY (location_id) REFERENCES join_location_id(location_id)
);

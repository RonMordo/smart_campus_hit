from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from faker import Faker
import random

Base = declarative_base()

class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True)
    building_number = Column(Integer, nullable=False)
    room_number = Column(Integer, nullable=False)
    room_type = Column(String, nullable=False)

class LocationInside(Base):
    __tablename__ = 'location_inside'
    id = Column(Integer, primary_key=True)
    height = Column(Float, nullable=False)
    angle = Column(Float, nullable=False)
    distance_from_door = Column(Float, nullable=False)
    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)
    room = relationship("Room", back_populates="locations_inside")

Room.locations_inside = relationship("LocationInside", order_by=LocationInside.id, back_populates="room")

class LocationOutside(Base):
    __tablename__ = 'location_outside'
    id = Column(Integer, primary_key=True)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    height = Column(Float, nullable=False)

class DataSensorInside(Base):
    __tablename__ = 'data_sensor_inside'
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    e_data = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    last_update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    location_id = Column(Integer, ForeignKey('location_inside.id'), nullable=False)
    location = relationship("LocationInside", back_populates="data_sensors")

LocationInside.data_sensors = relationship("DataSensorInside", order_by=DataSensorInside.id, back_populates="location")

class DataSensorOutside(Base):
    __tablename__ = 'data_sensor_outside'
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    e_data = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    last_update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    outside_id = Column(Integer, ForeignKey('location_outside.id'), nullable=False)
    location = relationship("LocationOutside", back_populates="data_sensors")

LocationOutside.data_sensors = relationship("DataSensorOutside", order_by=DataSensorOutside.id, back_populates="location")

def generate_sensor_data(sensor_type):
    if sensor_type == 'Temperature':
        data = f"{fake.random_int(min=-20, max=40)} °C"
    elif sensor_type == 'Humidity':
        data = f"{fake.random_int(min=20, max=100)} %"
    elif sensor_type == 'Motion':
        data = fake.random_element(elements=['No motion', 'Motion detected'])
    elif sensor_type == 'Volume':
        data = f"{fake.random_int(min=30, max=120)} dB"
    elif sensor_type == 'Air Quality':
        data = f"{fake.random_int(min=0, max=500)} AQI"
    else:
        data = ""  # Default to generic text if unknown type
    return data

# Replace with your actual PostgreSQL credentials
DB_NAME = 'campus_db'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'postgres_container'  # Assuming the database is hosted locally
DB_PORT = '5432'

DATABASE_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Creating an engine
engine = create_engine(DATABASE_URL)

# Creating all tables
Base.metadata.create_all(engine)

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

# Generating fake data
fake = Faker()

# Adding fake rooms
for _ in range(10):
    room = Room(
        building_number=fake.random_int(min=1, max=10),
        room_number=fake.random_int(min=100, max=399),
        room_type=fake.random_element(elements=('Classroom', 'Lab', 'Office', 'Storage'))
    )
    session.add(room)
session.commit()


# Adding fake locations inside
for _ in range(20):
    location_inside = LocationInside(
        height=random.uniform(2.0, 10.0),
        angle=random.uniform(0, 360),
        distance_from_door=random.uniform(0.5, 20.0),
        room_id=random.choice(session.query(Room.id).all())[0]
    )
    session.add(location_inside)
session.commit()

# Adding fake locations outside
for _ in range(10):
    location_outside = LocationOutside(
        x=random.uniform(0.0, 100.0),
        y=random.uniform(0.0, 100.0),
        height=random.uniform(2.0, 10.0)
    )
    session.add(location_outside)
session.commit()

# Adding fake data sensors inside
for _ in range(30):
    sensor_type = fake.random_element(elements=['Temperature', 'Humidity', 'Motion', 'Volume'])
    data_sensor_inside = DataSensorInside(
        type=sensor_type,
        e_data=generate_sensor_data(sensor_type),
        creation_date=fake.date_time_this_year(),
        last_update_date=fake.date_time_this_year(),
        location_id=random.choice(session.query(LocationInside.id).all())[0]
    )
    session.add(data_sensor_inside)
session.commit()

# Adding fake data sensors outside
for _ in range(15):
    sensor_type = fake.random_element(elements=['Temperature', 'Humidity', 'Air Quality'])
    data_sensor_outside = DataSensorOutside(
        type=sensor_type,
        e_data=generate_sensor_data(sensor_type),
        creation_date=fake.date_time_this_year(),
        last_update_date=fake.date_time_this_year(),
        outside_id=random.choice(session.query(LocationOutside.id).all())[0]
    )
    session.add(data_sensor_outside)
session.commit()


print("Fake data has been successfully added to the database.")
# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 (or whatever port your application uses)
EXPOSE 5000

# Define environment variable
ENV FLASK_APP smartCampus.py

# Run smartCampus.py when the container launches
CMD ["python", "smartCampus.py"]


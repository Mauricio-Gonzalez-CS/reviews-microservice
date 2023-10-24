# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to install dependencies
COPY requirements.txt .

# Add a COPY instruction to copy the file into the container
COPY /data/students.json .

COPY /data .

# Install Python dependencies
RUN pip install -r requirements.txt

RUN pip install fastapi

# Copy the rest of the application code
COPY . .

# Expose a port that your service will listen on
EXPOSE 8080

# Define the command to start your microservice
CMD ["python", "main.py"]

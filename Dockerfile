# Use an official Python runtime as a base image
FROM python: 3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt

# Install the required dependencies in the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the garden.py file to the container
COPY garden.py

# Set the default command to run when the container starts
CMD ["python", "garden.py"]


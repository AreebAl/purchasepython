# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first for better caching of layers
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Make port 8014 available to the world outside this container
EXPOSE 8014

# Run the application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8014", "app:app"]

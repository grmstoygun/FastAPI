# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /FastAPI

# Copy the current directory contents into the container at /app
COPY . /FastAPI

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run api.py when the container launches
CMD ["fastapi", "run", "api.py", "--port", "80"]

# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /usr/src/app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir  -r requirements.txt

# Define environment variable
ENV NAME OPENAI_API_KEY

# Run app.py when the container launches
ENTRYPOINT ["python", "src/data_extraction.py"]

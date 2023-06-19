# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Copy the Django project code into the container
COPY . /code/


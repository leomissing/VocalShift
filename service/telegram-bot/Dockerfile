# Use the official Python 3.10 image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements.txt file to the container's working directory
COPY requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

# Install the Python dependencies specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of the application code to the container's working directory
COPY . /code/.
RUN python /code/main.py
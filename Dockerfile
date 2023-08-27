# Use an official Python runtime as a parent image
FROM python:3.8

# system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app and get codebase there
WORKDIR /app
COPY app/ /app/

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# set up entrypoints
ENTRYPOINT ["streamlit", "run", "main.py"]

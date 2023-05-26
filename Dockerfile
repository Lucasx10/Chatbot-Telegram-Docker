# Base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code into the container
COPY . .

# Set the environment variables
ENV PYTHONUNBUFFERED=1

# Run the script
CMD ["python", "main.py"]

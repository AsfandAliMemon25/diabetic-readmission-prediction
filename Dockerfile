# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Expose the port Flask will run on
EXPOSE 8000

# Command to run the Flask app
CMD ["python", "app.py"]

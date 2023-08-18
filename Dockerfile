# Use the official Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the project requirements file to the working directory
COPY requirements.txt .

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Expose the port your app runs on
EXPOSE 3000

# Define the command to run your app
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:3000"]

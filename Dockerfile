# Use the official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY app.py .
COPY templates/ templates/ 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8081

# Run the app
CMD ["python", "app.py"]


#test commitasdas
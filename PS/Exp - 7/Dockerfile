# Use a minimal Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install system deps (optional but good for TLS, timezones, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates tzdata && rm -rf /var/lib/apt/lists/*

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Expose the Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

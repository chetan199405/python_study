# Use a base Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run the app
CMD ["python", "app.py"]

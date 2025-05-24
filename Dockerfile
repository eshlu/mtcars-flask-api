# Use official Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1

# Set working directory
WORKDIR /app

# Copy requirement file and install dependencies
COPY app/requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy app source code
COPY app/ ./app/
COPY data/ ./data/

# Train model on build (optional — or you can pre-train and just copy .pkl)
WORKDIR /app/app
RUN python model.py

# Expose the port Flask runs on
EXPOSE 5000

# Start Flask server
CMD ["python", "predict.py"]
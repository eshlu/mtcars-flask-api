# Deployment Instructions: Mtcars Flask API

This document outlines how to build, run, and deploy the Mtcars Flask API using Docker and Google Cloud Run.

## Requirements

- Docker
- Google Cloud SDK (`gcloud`)
- A Google Cloud project with billing enabled
- DockerHub account (public image pushed)

## 1. Build and Push Docker Image

Rebuild the image using `buildx` to ensure compatibility with Cloud Run (requires `amd64` platform).

```
docker buildx create --use  # one-time setup
docker buildx build --platform linux/amd64 \
  -t your-dockerhub-username/mtcars-flask-api:latest \
  --push .
\
```

## 2. Deploy to Google Cloud Run

Enable necessary services:
```
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com
```

Deploy:
```
gcloud run deploy mtcars-api \
  --image=docker.io/your-dockerhub-username/mtcars-flask-api:latest \
  --platform=managed \
  --region=us-central1 \
  --allow-unauthenticated
```

## 3. Example Input/Output
Example request:
```
curl -X POST https://your-cloud-run-url/predict \
  -H "Content-Type: application/json" \
  -d '{
    "cyl": 6,
    "disp": 160,
    "hp": 110,
    "drat": 3.9,
    "wt": 2.62,
    "qsec": 16.46,
    "vs": 0,
    "am": 1,
    "gear": 4,
    "carb": 4
  }'
```
Example response:
```
{
  "predicted_mpg": 21.55
}
```

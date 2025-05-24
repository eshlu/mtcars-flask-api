# mtcars-flask-api
In this repo:
- A containerized machine learning API built using the classic mtcars.csv dataset
- Showcases end-to-end development of a predictive linear regression model that estimates a car’s miles per gallon (mpg) based on various car specifications
- Serves predictions via a Flask-based REST API

## Repo Structure:
Mtcars-Flask-API/
│
├── app/                      # Flask app source code
│   ├── model.py              # Script to train and save the linear model
│   ├── predict.py            # Flask app for serving predictions
│   └── requirements.txt      # Python dependencies
│
├── data/
│   └── mtcars.csv            # Dataset used to train the model
│
├── Dockerfile                # Docker instructions for building the image
├── README.md                 # Project overview and usage
├── deployment/               # Instructions for local and cloud deployment
│   └── README.md             # How to build, run locally, and deploy to GCP
└── stephanie-lu_hw3.md          # Homework submission file with repo link

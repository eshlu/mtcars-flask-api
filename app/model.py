import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv('../data/mtcars.csv')

# Drop non-numeric identifier column if it exists (e.g., car names)
if 'model' in df.columns:
    df = df.drop(columns=['model'])

# Define predictors and response
X = df.drop(columns=['mpg'])
y = df['mpg']

# Ensure all features are numeric
X = X.apply(pd.to_numeric)

# Fit linear regression model
model = LinearRegression()
model.fit(X, y)

# Save model to disk
joblib.dump(model, 'linear_model.pkl')

print("Model trained and saved as 'linear_model.pkl'")
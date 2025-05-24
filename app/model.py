import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

df = pd.read_csv('../data/mtcars.csv')

if 'model' in df.columns:
    df = df.drop(columns=['model'])

X = df.drop(columns=['mpg'])
y = df['mpg']

X = X.apply(pd.to_numeric)
model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'linear_model.pkl')

print("Model trained and saved as 'linear_model.pkl'")
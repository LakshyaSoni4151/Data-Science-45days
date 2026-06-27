import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI App
app = FastAPI()

# Load Trained Model
model = joblib.load("model.joblib")

# Input Schema
class Movie(BaseModel):
    popularity: float

# Home Route
@app.get("/")
def home():
    return {
        "Message": "Movie Rating Prediction API"
    }

# Prediction Route
@app.post("/predict")
def predict(movie: Movie):

    input_data = pd.DataFrame({
        "popularity": [movie.popularity]
    })

    prediction = model.predict(input_data)

    return {
        "Popularity": movie.popularity,
        "Predicted Vote Average": round(float(prediction[0]), 2)
    }
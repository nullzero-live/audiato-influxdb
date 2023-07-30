
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

def predict(input_data):
    model = joblib.load('model.pkl')
    prediction = model.predict(input_data)
    return prediction

app = FastAPI()

class DataIn(BaseModel):
    feature1: float
    feature2: float
    # Add more features if necessary

@app.post("/predict")
async def predict_route(data_in: DataIn):
    # Convert the incoming data to the format expected by your model
    input_data = [[data_in.feature1, data_in.feature2]]
    prediction = predict(input_data)
    return {"prediction": prediction.tolist()}


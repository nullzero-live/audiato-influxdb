
import os
import joblib
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from influx import WrapperInfluxDB
from utils import DataIn

# Put all environment variables in a .env file
load_dotenv(find_dotenv())

app = FastAPI()

#Establish connection to InfluxDB
def main():
    client = WrapperInfluxDB(host=os.getenv("INFLUX_HOST"), 
                            username=os.getenv("INFLUX_USER"), 
                            password=os.getenv("INFLUX_PASS"), 
                            port=8086, 
                            database=os.getenv("INFLUX_DB"))


    @app.post("/predict")
    async def predict_route(data_in: DataIn):
        #model - does this belong here?????
        model = joblib.load('influx-model.pkl')
        # Convert the incoming data to the format expected by your model
        input_data = [[data_in.feature1, data_in.feature2]]
        prediction = model.predict(input_data)
        
        return {"prediction": prediction.tolist()}
    
    def detect_notify():
        prediction = 1
        if prediction == 1:
            alert = "Placeholder for notification function"
        else:
            alert = "No notification required"
        return alert

    #Test client connection                         
    print(f"CLIENT IS: {client}")
    version = client.client.ping()
    print("Successfully connected to InfluxDB: " + version)
    client.get_list_database()



'''From classifier - save in  case needed
#function for predictions from serialized models
def predict(input_data):
    model = joblib.load('model.pkl')
    prediction = model.predict(input_data)
    return prediction '''




import os
import joblib
from dotenv import load_dotenv

from influxdb import WrapperInfluxDB
from utils import DataIn, predict_route

# Put all environment variables in a .env file
load_dotenv()
app = FastAPI()

#Establish connection to InfluxDB
def main():
    client = WrapperInfluxDB(host=os.getenv("INFLUXDB_HOST"), 
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

    #Test client connection                         
    print(f"CLIENT IS: {client}")
    version = client.client.ping()
    print("Successfully connected to InfluxDB: " + version)
    client.get_list_database()

def detect_notify():
    pass

'''From classifier - save in  case needed
#function for predictions from serialized models
def predict(input_data):
    model = joblib.load('model.pkl')
    prediction = model.predict(input_data)
    return prediction '''



# Influx DB API Connection via Authiato 
import os
#import pydantic
from influxdb import InfluxDBClient
import json


class WrapperInfluxDB:
    def __init__(self, host, username, password, port, database, ssl=True, verify_ssl=True):
        self.client = InfluxDBClient(host, 
                                     port, 
                                     username, 
                                     password, 
                                     database,
                                     ssl,
                                     verify_ssl)

    
    def query(self, query):     
    # Method to query the db
        query = '''
            from(bucket: "proxmox")
                |> range(start: -1h)
                |> filter(fn: (r) => r._measurement == "memory")
            '''
        result = self.client.query(query)
        return result
    
    def close_connection(self):
        self.client.__del__()
    
#Establish connection to InfluxDB

client = WrapperInfluxDB(host='influxdb.hs88.live/', 
                         username='p4rlx', password='Unacceptable', port=8086, database="logmon")
print(f"CLIENT IS: {client}")
version = client.client.ping()
print("Successfully connected to InfluxDB: " + version)
#client.get_list_database()


   




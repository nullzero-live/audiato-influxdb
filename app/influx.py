# Influx DB API Connection via Authiato 
import os
from influxdb import InfluxDBClient

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
    



   




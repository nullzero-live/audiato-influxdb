from fastapi import FastAPI
from pydantic import BaseModel

#Features based on data source and objectives
class DataIn(BaseModel):
    feature1: float
    feature2: float
    # Add more features if necessary


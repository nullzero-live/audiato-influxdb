from fastapi import FastAPI
from pydantic import BaseModel


class DataIn(BaseModel):
    feature1: float
    feature2: float
    # Add more features if necessary


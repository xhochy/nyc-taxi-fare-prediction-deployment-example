import pickle
from datetime import datetime

import pandas as pd
from fastapi import FastAPI

with open("model.pkl", "rb") as f:
    model_pipeline = pickle.load(f)

app = FastAPI()


@app.get("/predict")
def predict(
    pickup_latitude: float,
    pickup_longitude: float,
    dropoff_latitude: float,
    dropoff_longitude: float,
    tpep_pickup_datetime: datetime,
    passenger_count: int,
) -> int:
    df = pd.DataFrame(
        {
            "pickup_latitude": pickup_latitude,
            "pickup_longitude": pickup_longitude,
            "dropoff_latitude": dropoff_latitude,
            "dropoff_longitude": dropoff_longitude,
            "tpep_pickup_datetime": tpep_pickup_datetime,
            "passenger_count": passenger_count,
        },
        index=[0],
    )
    return model_pipeline.predict(df)[0]

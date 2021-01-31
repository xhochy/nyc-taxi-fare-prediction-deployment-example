import pickle
from typing import List

import click
import pandas as pd
from nyc_taxi_fare.pipeline import lgbm_pipeline


@click.command()
@click.argument("training_data", nargs=-1, required=True)
@click.argument("model_location", nargs=1)
def train(training_data: List[str], model_location: str):
    # The column projection here is important as otherwise
    # the ColumnTransformer will complain about too many input columns in
    # the serving phase.
    used_columns = [
        "fare_amount",
        "pickup_latitude",
        "pickup_longitude",
        "dropoff_latitude",
        "dropoff_longitude",
        "tpep_pickup_datetime",
        "passenger_count",
    ]
    df = pd.concat(
        [pd.read_parquet(x, columns=used_columns) for x in training_data],
        ignore_index=True,
    )
    y = df.pop("fare_amount")

    pipeline = lgbm_pipeline()
    pipeline.fit(df, y)

    with open(model_location, "wb") as f:
        pickle.dump(pipeline, f, protocol=pickle.HIGHEST_PROTOCOL)

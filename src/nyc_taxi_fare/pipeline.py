import numpy as np
import pandas as pd
from lightgbm import LGBMRegressor
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer


def haversine_distance(lat1, lng1, lat2, lng2):
    lat1, lng1, lat2, lng2 = (np.radians(x) for x in (lat1, lng1, lat2, lng2))
    d = (
        np.sin(lat2 / 2 - lat1 / 2) ** 2
        + np.cos(lat1) * np.cos(lat2) * np.sin(lng2 / 2 - lng1 / 2) ** 2
    )
    return 2 * 6371 * np.arcsin(np.sqrt(d))  # 6,371 km is the earth radius


def haversine_distance_from_df(df):
    return pd.DataFrame(
        {
            "haversine_distance": haversine_distance(
                df["pickup_latitude"],
                df["pickup_longitude"],
                df["dropoff_latitude"],
                df["dropoff_longitude"],
            )
        }
    )


def split_pickup_datetime(df):
    return pd.DataFrame(
        {
            "pickup_dayofweek": df["tpep_pickup_datetime"].dt.dayofweek,
            "pickup_hour": df["tpep_pickup_datetime"].dt.hour,
            "pickup_minute": df["tpep_pickup_datetime"].dt.minute,
        }
    )


def feature_enginering():
    return make_column_transformer(
        (FunctionTransformer(), ["passenger_count"]),
        (
            FunctionTransformer(func=split_pickup_datetime),
            ["tpep_pickup_datetime"],
        ),
        (
            FunctionTransformer(
                func=haversine_distance_from_df,
            ),
            [
                "pickup_latitude",
                "pickup_longitude",
                "dropoff_latitude",
                "dropoff_longitude",
            ],
        ),
    )


def lgbm_pipeline():
    return make_pipeline(
        feature_enginering(),
        LGBMRegressor(objective="regression_l1"),
    )

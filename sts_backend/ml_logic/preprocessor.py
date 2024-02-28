import numpy as np
import pandas as pd

from colorama import Fore, Style

from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer

from taxifare.ml_logic.encoders import transform_time_features, transform_lonlat_features, compute_geohash


def preprocess_features(X: pd.DataFrame) -> np.ndarray:
    # def create_sklearn_preprocessor() -> ColumnTransformer:
    #     """
    #     Scikit-learn pipeline that transforms a cleaned dataset of shape (_, 7)
    #     into a preprocessed one of fixed shape (_, 65).

    #     Stateless operation: "fit_transform()" equals "transform()".
    #     """

    #     # PASSENGER PIPE
    #     p_min = 1
    #     p_max = 8
    #     passenger_pipe = FunctionTransformer(lambda p: (p - p_min) / (p_max - p_min))

    #     # DISTANCE PIPE
    #     dist_min = 0
    #     dist_max = 100

    #     distance_pipe = make_pipeline(
    #         FunctionTransformer(transform_lonlat_features),
    #         FunctionTransformer(lambda dist: (dist - dist_min) / (dist_max - dist_min))
    #     )

    #     # TIME PIPE
    #     timedelta_min = 0
    #     timedelta_max = 2090

    #     time_categories = [
    #         np.arange(0, 7, 1),  # days of the week
    #         np.arange(1, 13, 1)  # months of the year
    #     ]

    #     time_pipe = make_pipeline(
    #         FunctionTransformer(transform_time_features),
    #         make_column_transformer(
    #             (OneHotEncoder(
    #                 categories=time_categories,
    #                 sparse_output=False,
    #                 handle_unknown="ignore"
    #             ), [2,3]), # corresponds to columns ["day of week", "month"], not the other columns

    #             (FunctionTransformer(lambda year: (year - timedelta_min) / (timedelta_max - timedelta_min)), [4]), # min-max scale the columns 4 ["timedelta"]
    #             remainder="passthrough" # keep hour_sin and hour_cos
    #         )
    #     )

    #     # GEOHASH PIPE
    #     lonlat_features = [
    #         "pickup_latitude", "pickup_longitude", "dropoff_latitude",
    #         "dropoff_longitude"
    #     ]

    #     # Below are the 20 most frequent district geohashes of precision 5,
    #     # covering about 99% of all dropoff/pickup locations,
    #     # according to prior analysis in a separate notebook
    #     most_important_geohash_districts = [
    #         "dr5ru", "dr5rs", "dr5rv", "dr72h", "dr72j", "dr5re", "dr5rk",
    #         "dr5rz", "dr5ry", "dr5rt", "dr5rg", "dr5x1", "dr5x0", "dr72m",
    #         "dr5rm", "dr5rx", "dr5x2", "dr5rw", "dr5rh", "dr5x8"
    #     ]

    #     geohash_categories = [
    #         most_important_geohash_districts,  # pickup district list
    #         most_important_geohash_districts  # dropoff district list
    #     ]

    #     geohash_pipe = make_pipeline(
    #         FunctionTransformer(compute_geohash),
    #         OneHotEncoder(
    #             categories=geohash_categories,
    #             handle_unknown="ignore",
    #             sparse_output=False
    #         )
    #     )

    #     # COMBINED PREPROCESSOR
    #     final_preprocessor = ColumnTransformer(
    #         [
    #             ("passenger_scaler", passenger_pipe, ["passenger_count"]),
    #             ("time_preproc", time_pipe, ["pickup_datetime"]),
    #             ("dist_preproc", distance_pipe, lonlat_features),
    #             ("geohash", geohash_pipe, lonlat_features),
    #         ],
    #         n_jobs=-1,
    #     )

    #     return final_preprocessor

    # print(Fore.BLUE + "\nPreprocessing features..." + Style.RESET_ALL)

    # preprocessor = create_sklearn_preprocessor()
    # X_processed = preprocessor.fit_transform(X)

    # print("✅ X_processed, with shape", X_processed.shape)

    # return X_processed
    pass

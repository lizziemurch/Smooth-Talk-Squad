# import numpy as np
# import pandas as pd

# from pathlib import Path
# from colorama import Fore, Style
# from dateutil.parser import parse

# from sts_backend.params import *
# from sts_backend.ml_logic.data import get_data_with_cache, clean_data, load_data_to_bq
# from sts_backend.ml_logic.model import initialize_model, compile_model, train_model, evaluate_model
# from sts_backend.ml_logic.preprocessor import preprocess_features
# from sts_backend.ml_logic.registry import load_model, save_model, save_results
# from sts_backend.ml_logic.registry import mlflow_run, mlflow_transition_model

# def preprocess() -> None:
#     """
#     - Query the raw dataset from Le Wagon's BigQuery dataset
#     - Cache query result as a local CSV if it doesn't exist locally
#     - Process query data
#     - Store processed data on your personal BQ (truncate existing table if it exists)
#     - No need to cache processed data as CSV (it will be cached when queried back from BQ during training)
#     """

#     print(Fore.MAGENTA + "\n ⭐️ Use case: preprocess" + Style.RESET_ALL)

#     # Query raw data from BigQuery using `get_data_with_cache`
#     min_date = parse(min_date).strftime('%Y-%m-%d') # e.g '2009-01-01'
#     max_date = parse(max_date).strftime('%Y-%m-%d') # e.g '2009-01-01'

#     query = f"""
#         SELECT {",".join(COLUMN_NAMES_RAW)}
#         FROM {GCP_PROJECT_WAGON}.{BQ_DATASET}.raw_{DATA_SIZE}
#         WHERE pickup_datetime BETWEEN '{min_date}' AND '{max_date}'
#         ORDER BY pickup_datetime
#     """

#     # Retrieve data using `get_data_with_cache`
#     data_query_cache_path = Path(LOCAL_DATA_PATH).joinpath("raw", f"query_{min_date}_{max_date}_{DATA_SIZE}.csv")
#     data_query = get_data_with_cache(
#         query=query,
#         gcp_project=GCP_PROJECT,
#         cache_path=data_query_cache_path,
#         data_has_header=True
#     )

#     # Process data
#     data_clean = clean_data(data_query)

#     X = data_clean.drop("fare_amount", axis=1)
#     y = data_clean[["fare_amount"]]

#     X_processed = preprocess_features(X)

#     # Load a DataFrame onto BigQuery containing [pickup_datetime, X_processed, y]
#     # using data.load_data_to_bq()
#     data_processed_with_timestamp = pd.DataFrame(np.concatenate((
#         data_clean[["pickup_datetime"]],
#         X_processed,
#         y,
#     ), axis=1))

#     load_data_to_bq(
#         data_processed_with_timestamp,
#         gcp_project=GCP_PROJECT,
#         bq_dataset=BQ_DATASET,
#         table=f'processed_{DATA_SIZE}',
#         truncate=True
#     )

#     print("✅ preprocess() done \n")

# @mlflow_run
# def train(
#         min_date:str = '2009-01-01',
#         max_date:str = '2015-01-01',
#         split_ratio: float = 0.02, # 0.02 represents ~ 1 month of validation data on a 2009-2015 train set
#         learning_rate=0.0005,
#         batch_size = 256,
#         patience = 2
#     ) -> float:

#     """
#     - Download processed data from your BQ table (or from cache if it exists)
#     - Train on the preprocessed dataset (which should be ordered by date)
#     - Store training results and model weights

#     Return val_mae as a float
#     """

#     print(Fore.MAGENTA + "\n⭐️ Use case: train" + Style.RESET_ALL)
#     print(Fore.BLUE + "\nLoading preprocessed validation data..." + Style.RESET_ALL)

#     min_date = parse(min_date).strftime('%Y-%m-%d') # e.g '2009-01-01'
#     max_date = parse(max_date).strftime('%Y-%m-%d') # e.g '2009-01-01'

#     # Load processed data using `get_data_with_cache` in chronological order
#     # Try it out manually on console.cloud.google.com first!

#     # Below, our columns are called ['_0', '_1'....'_66'] on BQ, student's column names may differ
#     query = f"""
#         SELECT * EXCEPT(_0)
#         FROM {GCP_PROJECT}.{BQ_DATASET}.processed_{DATA_SIZE}
#         WHERE _0 BETWEEN '{min_date}' AND '{max_date}'
#         ORDER BY _0 ASC
#     """

#     data_processed_cache_path = Path(LOCAL_DATA_PATH).joinpath("processed", f"processed_{min_date}_{max_date}_{DATA_SIZE}.csv")
#     data_processed = get_data_with_cache(
#         gcp_project=GCP_PROJECT,
#         query=query,
#         cache_path=data_processed_cache_path,
#         data_has_header=False
#     )

#     if data_processed.shape[0] < 10:
#         print("❌ Not enough processed data retrieved to train on")
#         return None

#     # Create (X_train_processed, y_train, X_val_processed, y_val)
#     train_length = int(len(data_processed)*(1-split_ratio))

#     data_processed_train = data_processed.iloc[:train_length, :].sample(frac=1).to_numpy()
#     data_processed_val = data_processed.iloc[train_length:, :].sample(frac=1).to_numpy()

#     X_train_processed = data_processed_train[:, :-1]
#     y_train = data_processed_train[:, -1]

#     X_val_processed = data_processed_val[:, :-1]
#     y_val = data_processed_val[:, -1]

#     # Train model using `model.py`
#     model = load_model()

#     if model is None:
#         model = initialize_model(input_shape=X_train_processed.shape[1:])

#     model = compile_model(model, learning_rate=learning_rate)
#     model, history = train_model(
#         model, X_train_processed, y_train,
#         batch_size=batch_size,
#         patience=patience,
#         validation_data=(X_val_processed, y_val)
#     )

#     val_mae = np.min(history.history['val_mae'])

#     params = dict(
#         context="train",
#         training_set_size=DATA_SIZE,
#         row_count=len(X_train_processed),
#     )

#     # Save results on the hard drive using taxifare.ml_logic.registry
#     save_results(params=params, metrics=dict(mae=val_mae))

#     # Save model weight on the hard drive (and optionally on GCS too!)
#     save_model(model=model)

#     # The latest model should be moved to staging
#     if MODEL_TARGET == 'mlflow':
#         mlflow_transition_model(current_stage="None", new_stage="Staging")

#     print("✅ train() done \n")

#     return val_mae


# @mlflow_run
# def evaluate(
#         min_date:str = '2014-01-01',
#         max_date:str = '2015-01-01',
#         stage: str = "Production"
#     ) -> float:
#     """
#     Evaluate the performance of the latest production model on processed data
#     Return MAE as a float
#     """
#     print(Fore.MAGENTA + "\n⭐️ Use case: evaluate" + Style.RESET_ALL)

#     model = load_model(stage=stage)
#     assert model is not None

#     min_date = parse(min_date).strftime('%Y-%m-%d') # e.g '2009-01-01'
#     max_date = parse(max_date).strftime('%Y-%m-%d') # e.g '2009-01-01'

#     # Query your BigQuery processed table and get data_processed using `get_data_with_cache`
#     query = f"""
#         SELECT * EXCEPT(_0)
#         FROM {GCP_PROJECT}.{BQ_DATASET}.processed_{DATA_SIZE}
#         WHERE _0 BETWEEN '{min_date}' AND '{max_date}'
#     """

#     data_processed_cache_path = Path(f"{LOCAL_DATA_PATH}/processed/processed_{min_date}_{max_date}_{DATA_SIZE}.csv")
#     data_processed = get_data_with_cache(
#         gcp_project=GCP_PROJECT,
#         query=query,
#         cache_path=data_processed_cache_path,
#         data_has_header=False
#     )

#     if data_processed.shape[0] == 0:
#         print("❌ No data to evaluate on")
#         return None

#     data_processed = data_processed.to_numpy()

#     X_new = data_processed[:, :-1]
#     y_new = data_processed[:, -1]

#     metrics_dict = evaluate_model(model=model, X=X_new, y=y_new)
#     mae = metrics_dict["mae"]

#     params = dict(
#         context="evaluate", # Package behavior
#         training_set_size=DATA_SIZE,
#         row_count=len(X_new)
#     )

#     save_results(params=params, metrics=metrics_dict)

#     print("✅ evaluate() done \n")

#     return mae


# def pred(X_pred: pd.DataFrame = None) -> np.ndarray:
#     """
#     Make a prediction using the latest trained model
#     """

#     print("\n⭐️ Use case: predict")

#     if X_pred is None:
#         X_pred = pd.DataFrame(dict(
#         pickup_datetime=[pd.Timestamp("2013-07-06 17:18:00", tz='UTC')],
#         pickup_longitude=[-73.950655],
#         pickup_latitude=[40.783282],
#         dropoff_longitude=[-73.984365],
#         dropoff_latitude=[40.769802],
#         passenger_count=[int(1)],
#     ))

#     model = load_model()
#     assert model is not None

#     X_processed = preprocess_features(X_pred)
#     y_pred = model.predict(X_processed)

#     print("\n✅ prediction done: ", y_pred, y_pred.shape, "\n")
#     return y_pred


# if __name__ == '__main__':
#     preprocess(min_date='2009-01-01', max_date='2015-01-01')
#     train(min_date='2009-01-01', max_date='2015-01-01')
#     evaluate(min_date='2009-01-01', max_date='2015-01-01')
#     pred()

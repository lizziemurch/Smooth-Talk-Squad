import math
import numpy as np
import pandas as pd
from sts_backend.utils import simple_time_and_memory_tracker

# def transform_time_features(X: pd.DataFrame) -> np.ndarray:
#     assert isinstance(X, pd.DataFrame)

#     timedelta = (X["pickup_datetime"] - pd.Timestamp('2009-01-01T00:00:00', tz='UTC')) / pd.Timedelta(1,'D')

#     pickup_dt = X["pickup_datetime"].dt.tz_convert("America/New_York").dt
#     dow = pickup_dt.weekday
#     hour = pickup_dt.hour
#     month = pickup_dt.month

#     hour_sin = np.sin(2 * math.pi / 24 * hour)
#     hour_cos = np.cos(2*math.pi / 24 * hour)

#     return np.stack([hour_sin, hour_cos, dow, month, timedelta], axis=1)

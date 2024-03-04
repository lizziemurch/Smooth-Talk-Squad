import os
import numpy as np

##################  VARIABLES  ##################
MODEL_TARGET = os.environ.get("MODEL_TARGET")
PREDICT_RESOURCE = os.environ.get("PREDICT_RESOURCE")
Y_THRESHOLD = os.environ.get("Y_THRESHOLD")

################## VALIDATIONS #################

env_valid_options = dict(
    MODEL_TARGET=["local", "gcs", "mlflow"],
)

def validate_env_value(env, valid_options):
    env_value = os.environ[env]
    if env_value not in valid_options:
        raise NameError(f"Invalid value for {env} in `.env` file: {env_value} must be in {valid_options}")


for env, valid_options in env_valid_options.items():
    validate_env_value(env, valid_options)

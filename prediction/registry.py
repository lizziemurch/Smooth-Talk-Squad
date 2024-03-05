import os

from colorama import Fore, Style
from tensorflow import keras
from params import *

def load_model() -> keras.Model:
    """
    Return a saved model:
    - locally (latest one in alphabetical order)
    - or from GCS (most recent one) if MODEL_TARGET=='gcs'  --> for unit 02 only

    Return None (but do not Raise) if no model is found
    """
    # if MODEL_TARGET == "local":
    print(Fore.BLUE + f"\nLoad latest model from local registry..." + Style.RESET_ALL)
    model = keras.models.load_model(os.path.join('prediction','models','first_model_adapt.h5'))
    return model

    # TO BE CONTINUE ...
    # elif MODEL_TARGET == "gcs":
        # # 🎁 We give you this piece of code as a gift. Please read it carefully! Add a breakpoint if needed!
        # print(Fore.BLUE + f"\nLoad latest model from GCS..." + Style.RESET_ALL)

        # client = storage.Client()
        # blobs = list(client.get_bucket(BUCKET_NAME).list_blobs(prefix="model"))

        # try:
        #     latest_blob = max(blobs, key=lambda x: x.updated)
        #     latest_model_path_to_save = os.path.join(LOCAL_REGISTRY_PATH, latest_blob.name)
        #     latest_blob.download_to_filename(latest_model_path_to_save)

        #     latest_model = keras.models.load_model(latest_model_path_to_save)

        #     print("✅ Latest model downloaded from cloud storage")

        #     return latest_model
        # except:
        #     print(f"\n❌ No model found in GCS bucket {BUCKET_NAME}")

            # return None
        # pass

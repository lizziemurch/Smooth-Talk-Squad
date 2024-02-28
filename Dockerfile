
# THIS FILE IS NOT FINISHED YET
FROM python:3.8.12-buster

WORKDIR /prod

# First, pip install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Then only, install sts_backend!
COPY sts_backend sts_backend
RUN pip install .

COPY Makefile Makefile
RUN make reset_local_files

CMD uvicorn sts_backend.api.fast:app --host 0.0.0.0 --port $PORT

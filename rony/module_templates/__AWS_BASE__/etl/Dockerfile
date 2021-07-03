FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        ca-certificates \
        git \
        curl \
        wget &&\
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache \
    pandas \
    pyarrow \
    boto3 \
    sagemaker

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

RUN mkdir -p /opt/ml/processing/output/ && \
    mkdir -p /opt/ml/processing/input/ && \
    mkdir -p /opt/ml/processing/code/

ENV PATH="/opt/ml:${PATH}"

COPY run.py /opt/ml/processing/code/run.py

ENTRYPOINT ["python", "/opt/ml/processing/code/run.py"]
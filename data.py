import os
from os.path import exists
import boto3
import pandas as pd
import streamlit as st


# AWS_S3_BUCKET = "hatch-2022"
# AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
# AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
# client = Minio(
#     "minio.etheredge.co",
#     access_key=AWS_ACCESS_KEY_ID,
#     secret_key=AWS_SECRET_ACCESS_KEY,
# )

s3_client = boto3.client(
    "s3",
    endpoint_url="https://minio.etheredge.co",
    # aws_access_key_id=AWS_ACCESS_KEY_ID,
    # aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    # aws_session_token=AWS_SESSION_TOKEN,
)
# response = s3_client.get_object(Bucket=AWS_S3_BUCKET, Key="final_data.parquet")
# status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
# if status == 200:
#     final_df = pd.read_parquet(response["Body"])

s3 = boto3.client('s3', endpoint_url='https://minio.etheredge.co')
if not exists("final_data.parquet"):
    with open('final_data.parquet', 'wb') as f:
        s3.download_fileobj('hatch-2022', 'final_data.parquet', f)
        print("Downloaded file")

st.cache()
def get_data():
    df = pd.read_parquet("final_data.parquet")
    return df

st.cache()
def get_names():
    names = get_data()["scientificName"].unique()
    return names

# if not exists("fast_data"):
#     with open('s3_fast_data.parquet', 'wb') as f:
#         s3.download_fileobj('hatch-2022', 'fast_data', f)
#         print("Downloaded file")
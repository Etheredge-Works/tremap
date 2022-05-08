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
if not exists("final_data_clean.parquet"):
    with open('final_data_clean.parquet', 'wb') as f:
        s3.download_fileobj('hatch-2022', 'final_data.parquet', f)
        print("Downloaded file")

st.cache()
def get_data():
    df = pd.read_parquet("final_data_clean.parquet")
    return df

st.cache()
def get_names():
    names = get_data()["scientificName"].unique().tolist()
    return sorted(names)

def get_images(names):
    df = get_data()
    images = []
    captions = []
    nameesss = []
    raw_df = pd.DataFrame()
    for name in names:
        filtered_df = df[df["scientificName"] == name]
        raw_df = pd.concat([raw_df, filtered_df])
        images += filtered_df["identifier"].tolist()
        captions += filtered_df["recordedBy"].tolist()
        nameesss += [name for _ in range (len(filtered_df))]
    final = []
    for caption, name in zip(captions, nameesss):
        final.append(f"{name} recorded by {caption}")
    return images, captions, nameesss, final, raw_df

# if not exists("fast_data"):
#     with open('s3_fast_data.parquet', 'wb') as f:
#         s3.download_fileobj('hatch-2022', 'fast_data', f)
#         print("Downloaded file")
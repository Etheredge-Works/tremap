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

with st.spinner("Getting data..."):
    s3 = boto3.client('s3', endpoint_url='https://minio.etheredge.co')
    if not exists("final_data_clean.parquet"):
        s3.download_fileobj('hatch-2022', 'final_data_clean.parquet', "final_data_clean.parquet")
        print("Downloaded file")
    else:
        print("File already exists")

st.cache()
def get_data():
    df = pd.read_parquet("final_data_clean.parquet")
    df['species'] = df['species'].fillna('')
    df['genus'] = df['genus'].fillna('')
    df['stateProvince'] = df['stateProvince'].fillna('')
    df['countryCode'] = df['countryCode'].fillna('')
    # df
    # df.fillna("", inplace=True)
    # df['']
    
    return df

st.cache()
def get_names():
    names = get_data()["scientificName"].unique().tolist()

    return sorted(names)

def get_images(key, values):
    df = get_data()
    images = []
    captions = []
    s_names = []
    raw_df = pd.DataFrame()
    for value in values:
        filtered_df = df[df[key] == value]
        raw_df = pd.concat([raw_df, filtered_df])
        images += filtered_df["identifier"].tolist()
        captions += filtered_df["recordedBy"].tolist()

        if len(filtered_df) > 1:
            s_names += filtered_df["scientificName"].tolist()
        else:
            s_names += [filtered_df["scientificName"].iloc[0]]
    final = []
    for caption, name in zip(captions, s_names):
        final.append(f"{name} recorded by {caption}")
    return images, captions, s_names, final, raw_df

# if not exists("fast_data"):
#     with open('s3_fast_data.parquet', 'wb') as f:
#         s3.download_fileobj('hatch-2022', 'fast_data', f)
#         print("Downloaded file")
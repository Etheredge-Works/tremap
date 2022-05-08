import pandas as pd
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
# url = "https://minio.etheredge.co/hatch-2022/final_data.parquet?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ISZXRXUZP724OAWH8KAU%2F20220508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220508T063140Z&X-Amz-Expires=604800&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJJU1pYUlhVWlA3MjRPQVdIOEtBVSIsImV4cCI6MzYwMDAwMDAwMDAwMCwicG9saWN5IjoiY29uc29sZUFkbWluIn0.pYQS_1DNTTzmTiaWTg-RdZL_70-dj6ve5RgqCdCs-RjgpvkFa_cvdW7t8PB1OWqSdorWWIwWJWHU_IFYdWk91Q&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=68d1860f5e454fc0ac1569b622dc1aca2dc626d686fac5e42422313b266b850a"
# url = "http://172.21.0.4:9000/hatch-2022/final_data.parquet?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=90AHR20RZL62S1XOWXRL%2F20220508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220508T150410Z&X-Amz-Expires=604800&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiI5MEFIUjIwUlpMNjJTMVhPV1hSTCIsImV4cCI6MzYwMDAwMDAwMDAwMCwicG9saWN5IjoiY29uc29sZUFkbWluIn0.OBvA4LoqkE1TjoFhTla7vPIv9yQyo0u1TUTXjveWq8jXGUtMYzN3bQeL6mw-WvJIreCcCHzxnvblTgAv8EF-Rw&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=39b3fc757dfe0afb07c898dcd5d53c7703732d366d302d0722f1c0571ac344cf"
# df = pd.read_csv(url + "data/multimedia.txt", delimiter="\t")


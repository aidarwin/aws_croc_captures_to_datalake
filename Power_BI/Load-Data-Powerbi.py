import boto3, os, io
import pandas as pd 

my_key= 'AKIAVECH3E5NYVPEXZOP' 
my_secret= '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' 

my_bucket_name = 'f-croc-capture' 
my_file_path = 'aws_croc_captures_to_datalake/Silver/part-00000-e5eb51b5-5bb4-43ba-a608-dfedc5af7e3a-c000.snappy.parquet' 

session = boto3.Session(aws_access_key_id=my_key,aws_secret_access_key=my_secret) 
s3Client = session.client('s3') 
f = s3Client.get_object(Bucket=my_bucket_name, Key=my_file_path) 
heart_disease_data = pd.read_parquet(io.BytesIO(f['Body'].read()))

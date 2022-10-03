import boto3, os, io
import pandas as pd 

my_key= 'AKIAVECH3E5NYVPEXZOP' 
my_secret= 'k+itlUDzMYSmF0eChkA9QdaRRtC/2LbcOsTnj6hL' 

my_bucket_name = 'meksichatlogs' 
my_file_path = 'bronze/samplemeksi.json' 

session = boto3.Session(aws_access_key_id=my_key,aws_secret_access_key=my_secret) 
s3Client = session.client('s3') 
f = s3Client.get_object(Bucket=my_bucket_name, Key=my_file_path) 
heart_disease_data = pd.read_json(io.BytesIO(f['Body'].read()))
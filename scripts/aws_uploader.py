import boto3
from pathlib import Path

def upload_file_to_s3(local_path: Path, bucket_name: str, s3_key: str):
    s3 = boto3.client("s3") # Conecta con S3 usando tus credenciales
    s3.upload_file(str(local_path), bucket_name, s3_key) # Sube el archivo

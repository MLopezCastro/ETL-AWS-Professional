import boto3
import pandas as pd

def upload_parquet_to_s3():
    # Ruta del archivo local
    local_file = 'data/output/orders_clean.snappy.parquet'

    # Configuración del bucket y key
    bucket_name = 'marcelo-orders-bucket'
    s3_key = 'data/bloque4/orders_clean.snappy.parquet'

    # Leer el archivo Parquet como binario
    with open(local_file, 'rb') as f:
        file_data = f.read()

    # Subir a S3
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=s3_key, Body=file_data)

    print(f'✅ Archivo subido: s3://{bucket_name}/{s3_key}')

if __name__ == '__main__':
    upload_parquet_to_s3()

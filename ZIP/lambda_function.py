from main import main
import os

def lambda_handler(event, context):
    orders_path = "data/raw/orders.csv"
    customers_path = "data/raw/customers.csv"
    output_path = "data/clean/orders_clean"
    output_format = "parquet"

    # Ejecuta tu pipeline completo
    main(orders_path, customers_path, output_path, output_format)

    return {
        'statusCode': 200,
        'body': 'ETL ejecutado correctamente desde Lambda'
    }

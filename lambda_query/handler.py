import boto3

def lambda_handler(event, context):
    athena = boto3.client("athena")
    bucket = event["bucket"]

    query = """
        SELECT status, SUM(total_amount) AS total_sales
        FROM default.orders_clean
        GROUP BY status
    """

    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={"Database": "default"},
        ResultConfiguration={"OutputLocation": f"s3://{bucket}/athena-results/"}
    )

    return {"QueryExecutionId": response["QueryExecutionId"]}

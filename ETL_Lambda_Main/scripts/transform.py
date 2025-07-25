import pandas as pd

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    return df

def add_total_amount(df: pd.DataFrame) -> pd.DataFrame:
    df["total_amount"] = df["quantity"] * df["unit_price"]
    return df

def merge_orders_customers(df_orders: pd.DataFrame, df_customers: pd.DataFrame) -> pd.DataFrame:
    return df_orders.merge(df_customers, on="customer_id", how="left")

def normalize_country(df: pd.DataFrame) -> pd.DataFrame:
    df["country"] = df["country"].str.strip().str.upper()
    return df

def categorize_vip(df: pd.DataFrame) -> pd.DataFrame:
    df["vip"] = df["total_amount"] > 1000
    return df

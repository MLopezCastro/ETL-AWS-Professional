import re
import pandas as pd

def unique_key(df: pd.DataFrame, column: str):
    if not df[column].is_unique:
        raise ValueError(f"La columna {column} tiene valores duplicados.")

def no_nulls(df: pd.DataFrame, columns: list):
    for col in columns:
        if df[col].isnull().any():
            raise ValueError(f"La columna {col} tiene valores nulos.")

def positive_values(df: pd.DataFrame, columns: list):
    for col in columns:
        if (df[col] <= 0).any():
            raise ValueError(f"La columna {col} tiene valores menores o iguales a 0.")

def valid_email(df: pd.DataFrame):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    if not df["email"].apply(lambda x: bool(re.match(pattern, str(x)))).all():
        raise ValueError("Hay emails inválidos en la columna 'email'.")

def allowed_status(df: pd.DataFrame):
    allowed = {"completed", "pending", "cancelled"}
    if not df["status"].isin(allowed).all():
        raise ValueError("Hay valores no permitidos en la columna 'status'.")

def date_not_future(df: pd.DataFrame, column: str):
    if (df[column] > pd.Timestamp.today()).any():
        raise ValueError(f"Hay fechas futuras en la columna {column}.")

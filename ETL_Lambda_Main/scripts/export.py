import pandas as pd
from pathlib import Path

def export_df(df, output_path, output_format="csv", compression=None):
    if output_format == "csv":
        df.to_csv(output_path, index=False)
    elif output_format == "parquet":
        df.to_parquet(output_path, index=False, compression=compression)
    else:
        raise ValueError("Formato de exportación no soportado.")


"""Crear una versión DVC didáctica: cambia una sola celda del CSV."""
import pandas as pd
from .common import RAW_PATH

if __name__ == "__main__":
    data = pd.read_csv(RAW_PATH)
    previous = float(data.loc[0, "MonthlyCharges"])
    data.loc[0, "MonthlyCharges"] = round(previous + 2, 2)
    data.to_csv(RAW_PATH, index=False)
    print(f"MonthlyCharges fila 1: {previous} -> {data.loc[0,'MonthlyCharges']}")

"""Validación determinista del CSV original."""
from .common import load_raw

def validate():
    frame = load_raw()
    assert len(frame) > 1000, "Dataset de tamaño inesperado"
    print(f"Dataset válido: {len(frame)} filas; TotalCharges vacíos: {frame['TotalCharges'].isna().sum()}")
    return True

if __name__ == "__main__":
    validate()

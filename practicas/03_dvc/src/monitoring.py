"""Evidently 0.7: Report/DataDriftPreset con exportación a HTML."""
import argparse
from pathlib import Path
import json
import pandas as pd
from .common import ROOT, FEATURES


def run_monitoring(source="simulated"):
    from evidently import Report
    from evidently.presets import DataDriftPreset
    ref = pd.read_csv(ROOT / "data" / "monitoring" / "reference.csv")
    if source == "simulated":
        current = pd.read_csv(ROOT / "data" / "monitoring" / "current_shifted.csv")
    else:
        log_file = ROOT / "runtime" / "predictions.jsonl"
        if not log_file.exists():
            raise RuntimeError("No hay logs de FastAPI; envía predicciones primero.")
        records = [json.loads(line) for line in log_file.read_text(encoding="utf-8").splitlines() if line.strip()]
        if len(records) < 5:
            raise RuntimeError("Se recomiendan al menos cinco predicciones para este ejercicio.")
        current = pd.DataFrame(records)[FEATURES + ["prediction_probability"]]
    columns = FEATURES + ["prediction_probability"]
    report = Report([DataDriftPreset(columns=columns)])
    snapshot = report.run(current[columns], ref[columns])
    reports = ROOT / "reports";reports.mkdir(exist_ok=True)
    output = reports / f"data_drift_{source}.html"
    snapshot.save_html(str(output))
    summary = {
        "source": source, "reference_rows": len(ref), "current_rows": len(current),
        "reference_probability_mean": float(ref["prediction_probability"].mean()),
        "current_probability_mean": float(current["prediction_probability"].mean()),
        "important": "Drift estadístico no demuestra por sí solo deterioro de rendimiento; para rendimiento hacen falta etiquetas reales.",
    }
    (reports / f"monitoring_{source}.json").write_text(json.dumps(summary, indent=2),encoding="utf-8")
    print(f"Reporte: {output}")
    print(json.dumps(summary, indent=2))
    return output

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--source", choices=["simulated", "api-logs"], default="simulated")
    args=parser.parse_args()
    run_monitoring(args.source)

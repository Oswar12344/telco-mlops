"""Validaciones de dataset real y consistencia de modelo."""
import joblib
from src.common import ROOT, FEATURES, load_raw, get_splits

def test_raw_data():
    frame = load_raw()
    assert len(frame) == 7043
    assert {"Churn", *FEATURES} <= set(frame.columns)
    assert frame["TotalCharges"].isna().sum() == 11

def test_split_and_model():
    Xt, Xv, Xs, yt, yv, ys = get_splits()
    assert len(Xt) + len(Xv) + len(Xs) == 7043
    assert len(Xt.columns) == 5
    model = joblib.load(ROOT / "models" / "champion.joblib")
    assert len(model.predict(Xs.head(4))) == 4

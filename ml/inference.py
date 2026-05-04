from ml.feature_pipeline import vectorize_payload


def predict_risk(payload):
    vector = vectorize_payload(payload)
    score = min(100, int(vector[0] * 8 + vector[1] * 6 + vector[2] * 5 + vector[3] * 30 + vector[4] * 4 + vector[5] * 3 + vector[6] * 20 + vector[7] * 20))
    return {"model": "heuristic_ml_adapter", "risk_score": score}

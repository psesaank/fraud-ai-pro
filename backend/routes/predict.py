
from fastapi import APIRouter
from services.model_loader import model, input_name
from services.metrics_engine import metrics
import numpy as np
import time

router = APIRouter()

@router.get("/predict")
def predict(amount: float):
    start = time.time()
    arr = np.array([[amount]], dtype=np.float32)
    out = model.run(None, {input_name: arr})
    pred = int(out[0][0][0])
    latency = (time.time() - start) * 1000

    metrics["requests"] += 1
    metrics["latencies"].append(latency)

    return {
        "fraud": bool(pred),
        "model": metrics.get("model_name", "GREEN"),
        "latency_ms": latency
    }

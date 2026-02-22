
from fastapi import APIRouter
from services.metrics_engine import metrics

router = APIRouter()

@router.get("/metrics")
def get_metrics():
    avg = None
    if metrics["latencies"]:
        avg = sum(metrics["latencies"]) / len(metrics["latencies"])
    return {
        "requests": metrics["requests"],
        "avg_latency_ms": avg,
        "model": metrics.get("model_name")
    }

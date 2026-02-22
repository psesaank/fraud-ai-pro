
from fastapi import FastAPI
from routes.predict import router as predict_router
from routes.metrics import router as metrics_router
from routes.health import router as health_router

app = FastAPI(title="Fraud AI Pro Backend")

app.include_router(predict_router)
app.include_router(metrics_router)
app.include_router(health_router)

@app.get("/")
def root():
    return {"service": "fraud-ai-pro"}

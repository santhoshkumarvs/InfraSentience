from fastapi import FastAPI, Request
import logging
import random
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import PlainTextResponse

logging.basicConfig(filename="inference_triton.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Prometheus metrics
inference_requests = Counter("inference_requests_total", "Total inference requests")
inference_latency = Histogram("inference_latency_seconds", "Inference response latency")

app = FastAPI()

@app.post("/simulate")
@inference_latency.time()
async def simulate_inference(request: Request):
    inference_requests.inc()
    data = await request.json()
    output = {"prediction": random.choice(["cat", "dog", "bird"]), "confidence": round(random.uniform(0.7, 0.99), 2)}
    logging.info(f"Triton Inference Request: {data} -> {output}")
    return output

@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest(), media_type="text/plain")

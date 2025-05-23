from fastapi import FastAPI
app = FastAPI()

@app.get("/detect")
def detect():
    return {"result": "anomalies_detected"}

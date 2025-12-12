from fastapi import FastAPI
from routes import router_health
from routes import router_analyze

app = FastAPI(title="STRACK")

@app.get("/")
def API_ON():
    return {"status": "OK", "version": "1.0"}

app.include_router(router_health.router, prefix="/health")
app.include_router(router_analyze.router, prefix="/analyze")


from fastapi import FastAPI
from routes import router_health
from routes import router_analyze

app = FastAPI(title="STRACK")

app.include_router(router_health.router, prefix="/health")
app.include_router(router_analyze.router, prefix="/analyze")


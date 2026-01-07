from fastapi import FastAPI
from app.routes.lead_routes import router as lead_router

app = FastAPI(title="Estudo com MongoDB (docker) + FastAPI")

app.include_router(lead_router)
from databricks import sql
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.client import router as client_router
from app.routers.entreprise import router as entreprise_router
from app.routers.ml import router as ml_router

from app.config import (
    DATABRICKS_SERVER_HOSTNAME,
    DATABRICKS_HTTP_PATH,
    DATABRICKS_TOKEN,
)

def get_connection():
    return sql.connect(
        server_hostname=DATABRICKS_SERVER_HOSTNAME,
        http_path=DATABRICKS_HTTP_PATH,
        access_token=DATABRICKS_TOKEN,
    )

app = FastAPI(
    title="SBDH API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Bienvenue sur l'API SBDH"
    }

app.include_router(client_router)
app.include_router(entreprise_router)
app.include_router(ml_router)
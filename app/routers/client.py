from fastapi import APIRouter, HTTPException
from app.services import client_service
from app.schemas.client import (
    RecommendationResponse,
    SimilarClientResponse,
    TrendingProductResponse
)
 
router = APIRouter(
    prefix="/client",
    tags=["Client"]
)
 
@router.get("/dashboard/{client_id}")
def dashboard(client_id: str):
    data = client_service.get_dashboard(client_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Client introuvable")
    return data
 
@router.get("/history/{client_id}")
def history(client_id: str):
    return client_service.get_history(client_id)
 
@router.get(
    "/recommendations/{client_id}",
    response_model=list[RecommendationResponse]
)
def recommendations(client_id: str):
    return client_service.get_recommendations(client_id)
 
@router.get(
    "/similar/{client_id}",
    response_model=list[SimilarClientResponse]
)
def similar_clients(client_id: str):
    return client_service.get_similar_clients(client_id)

router
@router.get(
    "/trending",
    response_model=list[TrendingProductResponse]
)
def trending_products(limit: int = 10):
    return client_service.get_trending_products(limit)
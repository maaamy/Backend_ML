from fastapi import APIRouter, HTTPException
from app.services import entreprise_service
from app.schemas.entreprise import TopProductResponse
 
router = APIRouter(
    prefix="/entreprise",
    tags=["Entreprise"]
)
 
@router.get("/dashboard/{entreprise_id}")
def dashboard(entreprise_id: str):
    data = entreprise_service.get_dashboard(entreprise_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Entreprise introuvable")
    return data
 
@router.get("/products/{entreprise_id}")
def products(entreprise_id: str):
    return entreprise_service.get_products(entreprise_id)
 
@router.get("/stock/{entreprise_id}")
def stock(entreprise_id: str):
    return entreprise_service.get_stock(entreprise_id)
 
@router.get("/clients/{entreprise_id}")
def clients(entreprise_id: str):
    return entreprise_service.get_clients(entreprise_id)
 
@router.get("/reviews/{entreprise_id}")
def reviews(entreprise_id: str):
    return entreprise_service.get_reviews(entreprise_id)
 
@router.get("/finance/{entreprise_id}")
def finance(entreprise_id: str):
    return entreprise_service.get_finance(entreprise_id)
 
@router.get(
    "/top-products/{entreprise_id}",
    response_model=list[TopProductResponse]
)
def top_products(entreprise_id: str):
    return entreprise_service.get_top_products(entreprise_id)
 
@router.get("/orders-status/{entreprise_id}")
def orders_status(entreprise_id: str):
    return entreprise_service.get_orders_status(entreprise_id)

@router.get("/daily-sales/{entreprise_id}")
def daily_sales(entreprise_id: str):
    return entreprise_service.get_daily_sales(entreprise_id)
 
@router.get("/sales-products/{entreprise_id}")
def sales_products(entreprise_id: str):
    return entreprise_service.get_sales_products(entreprise_id)



from fastapi import APIRouter
from app.services import ml_service
from app.schemas.ml import (
    XGBoostPredictionResponse,
    ProphetPredictionResponse,
    LSTMPredictionResponse,
    MetricResponse,
)
 
router = APIRouter(
    prefix="/ml",
    tags=["Machine Learning"]
)
 
@router.get(
    "/predictions/xgboost",
    response_model=list[XGBoostPredictionResponse]
)
def xgboost():
    return ml_service.get_xgboost_predictions()
 
@router.get(
    "/predictions/prophet",
    response_model=list[ProphetPredictionResponse]
)
def prophet():
    return ml_service.get_prophet_predictions()
 
@router.get(
    "/predictions/lstm",
    response_model=list[LSTMPredictionResponse]
)
def lstm():
    return ml_service.get_lstm_predictions()
 
@router.get(
    "/predictions/{entreprise_id}",
    response_model=list[XGBoostPredictionResponse]
)
def predictions(entreprise_id: str):
    return ml_service.get_predictions(entreprise_id)
 
@router.get(
    "/metrics/{entreprise_id}",
    response_model=list[MetricResponse]
)
def metrics(entreprise_id: str):
    return ml_service.get_metrics(entreprise_id)
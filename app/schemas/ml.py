from datetime import datetime
from pydantic import BaseModel
 
 
class MetricResponse(BaseModel):
    entreprise_id: str
    entreprise: str
    modele: str
 
    MAE: float
    RMSE: float
    MAPE: float
    R2: float
 
    nb_jours_train: int
    nb_jours_test: int
 
 
class XGBoostPredictionResponse(BaseModel):
    entreprise_id: str
    entreprise: str
    ds: datetime
    y: float | None
    yhat: float
 
 
class LSTMPredictionResponse(BaseModel):
    entreprise_id: str
    entreprise: str
    ds: datetime
    y: float | None
    yhat: float
 
 
class ProphetPredictionResponse(BaseModel):
    entreprise_id: str
    entreprise: str
    ds: datetime
    y: float | None
    yhat: float
    yhat_lower: float
    yhat_upper: float
from decimal import Decimal
from pydantic import BaseModel 
 
class RecommendationResponse(BaseModel):
    client_id: str
 
    produit_id: str
    produit: str
    description: str | None
 
    categorie: str
    marque: str
    entreprise: str
 
    image: str | None
    image_alt: str | None
 
    prix_min: Decimal
    prix_max: Decimal
    prix_moyen: Decimal
 
    stock_total: int
 
    score_final: float
    rang: int
 
    note_moyenne: float | None
    quantite_vendue: int
    nb_clients: int

class SimilarClientResponse(BaseModel):
    client_id: str
    voisin_id: str
    client: str
    email: str
    ville: str | None
    pays: str | None
    similarite: float

class TrendingProductResponse(BaseModel):
    produit_id: str
    produit: str
 
    categorie: str
    marque: str
    entreprise: str
 
    image: str | None
    prix_moyen: Decimal
 
    nb_commandes: int
    quantite_vendue: int
    chiffre_affaires: Decimal
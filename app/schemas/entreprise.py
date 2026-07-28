from pydantic import BaseModel
 
class TopProductResponse(BaseModel):
    produit_id: str
    produit: str
    entreprise_id: str
    entreprise: str
    chiffre_affaires: float
    quantite_vendue: int
    nb_commandes: int
    prix_moyen: float
    nb_clients: int
    rang_ca: int
    rang_quantite: int
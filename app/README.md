# E-Commerce Platform & Smart Business Decision Hub (SBDH)


SBDH est une plateforme e-commerce intelligente reposant sur une architecture Big Data et Machine Learning, capable de fournir des recommandations personnalisées, des analyses avancées et des prévisions financières fiables.

Backend de la plateforme E-Commerce Platform & Smart Business Decision Hub (SBDH).

Cette API développée avec FastAPI permet de récupérer les données e-commerce, les analyses clients/entreprises et les prédictions des modèles de Machine Learning.

##  Installation
```bash
# Cloner le repo
git clone git@github.com:maaamy/Backend_ML.git
cd backend_ML

# Activer l'environnement virtuel
& venv/Scripts/Activate.ps1

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'API
python -m uvicorn app.main:app --reload

L'API est disponible sur http://127.0.0.1:8000.
```

## Variables d’environnement

Le projet nécessite certaines variables d’environnement pour fonctionner correctement.

Créer un fichier .env à la racine du projet :

```bash
DATABRICKS_SERVER_HOSTNAME=server_hostname
DATABRICKS_HTTP_PATH=http_path 
DATABRICKS_TOKEN=token
```

## API

Les endpoints sont organisés en trois catégories :
```bash
/client — dashboards, historique, recommandations et clients similaires
/entreprise — produits, stocks, clients, finances et ventes
/ml — prédictions XGBoost et métriques
```

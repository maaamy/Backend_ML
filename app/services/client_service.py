from app.utils.db_utils import execute_query
 
def get_dashboard(client_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_client_dashboard
    WHERE client_id = ?
    """
    result = execute_query(query, (client_id,))
    return result[0] if result else None
 
def get_history(client_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_client_history
    WHERE client_id = ?
    ORDER BY date_commande DESC
    """
    return execute_query(query, (client_id,))
 
def get_recommendations(client_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_client_recommandations
    WHERE client_id = ?
    ORDER BY score_final DESC
    """
    return execute_query(query, (client_id,))
 
def get_similar_clients(client_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_client_similar
    WHERE client_id = ?
    ORDER BY similarite DESC
    """
    return execute_query(query, (client_id,))
 
def get_trending_products(limit: int = 10):
    query = """
    SELECT *
    FROM workspace.api.vw_trending_products
    ORDER BY
        nb_commandes DESC,
        chiffre_affaires DESC
    LIMIT ?
    """
    return execute_query(query, (limit,))
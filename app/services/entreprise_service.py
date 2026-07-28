from app.utils.db_utils import execute_query
 
def get_dashboard(entreprise_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_entreprise_dashboard
    WHERE entreprise_id = ?
    """
    result = execute_query(query, (entreprise_id,))
    return result[0] if result else None
 
def get_products(entreprise_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_entreprise_products
    WHERE entreprise_id = ?
    """
    return execute_query(query, (entreprise_id,))
 
def get_stock(entreprise_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_entreprise_stock
    WHERE entreprise_id = ?
    """
    return execute_query(query, (entreprise_id,))
 
def get_clients(entreprise_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_entreprise_clients
    WHERE entreprise_id = ?
    """
    return execute_query(query, (entreprise_id,))
 
def get_reviews(entreprise_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_entreprise_reviews
    WHERE entreprise_id = ?
    """
    return execute_query(query, (entreprise_id,))
 
def get_finance(entreprise_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_entreprise_finance
    WHERE entreprise_id = ?
    """
    return execute_query(query, (entreprise_id,))
 
def get_top_products(entreprise_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_top_products
    WHERE entreprise_id = ?
    ORDER BY chiffre_affaires DESC
    """
    return execute_query(query, (entreprise_id,))
 
def get_orders_status(entreprise_id: str):
    query = """
    SELECT *
    FROM api.vw_orders_status
    WHERE entreprise_id = ?
    """
    return execute_query(query, (entreprise_id,))

def get_daily_sales(entreprise_id: str):
    query = """
    SELECT *
    FROM api.vw_daily_sales
    WHERE entreprise_id = ?
    ORDER BY ds ASC
    """
    return execute_query(query, (entreprise_id,))
 
 
def get_sales_products(entreprise_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_sales_products
    WHERE entreprise_id = ?
    ORDER BY chiffre_affaires DESC
    """
    return execute_query(query, (entreprise_id,))
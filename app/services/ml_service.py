from app.utils.db_utils import execute_query
 
def get_xgboost_predictions():
    query = """
    SELECT *
    FROM workspace.api.vw_predictions_xgboost
    ORDER BY ds
    """
    return execute_query(query)
 
 
def get_prophet_predictions():
    query = """
    SELECT *
    FROM workspace.api.vw_predictions_prophet
    ORDER BY ds
    """
    return execute_query(query)
 
 
def get_lstm_predictions():
    query = """
    SELECT *
    FROM workspace.api.vw_predictions_lstm
    ORDER BY ds
    """
    return execute_query(query)
 
 
def get_predictions(entreprise_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_predictions
    WHERE entreprise_id = ?
    ORDER BY ds
    """
    return execute_query(query, (entreprise_id,))
 
 
def get_metrics(entreprise_id: str):
    query = """
    SELECT *
    FROM workspace.api.vw_metrics
    WHERE entreprise_id = ?
    ORDER BY RMSE
    """
    return execute_query(query, (entreprise_id,))
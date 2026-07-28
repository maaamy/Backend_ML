from app.database import get_connection
 
def execute_query(query: str, params: tuple = ()):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        result = [
            dict(zip(columns, row))
            for row in rows
        ]
        return result
    finally:
        cursor.close()
        conn.close()
from sql import ServerCredentials, ServerConnection, DatabaseConnection

def setup_my_sql_connection(credentials: ServerCredentials, database_name: str):
    _server:ServerConnection = ServerConnection()
    _server_con = _server.connect_to_server(credentials)

    _db_con:DatabaseConnection = DatabaseConnection()
    _db_con.connect_to_database(_server_con, database_name)
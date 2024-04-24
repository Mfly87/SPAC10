from sql import ServerCredentials, ServerConnection, DatabaseConnection

import json

def setup_my_sql_connection():
    
    _host = ""
    _user = ""
    _password = ""
    _port = ""
    
    _database_name = ""

    with open('config.json') as f:
        _config: dict[str,any] = json.load(f)

        _database_name = _config.get("mysql_database_name", _database_name)
        
        _dict: dict[str,str] = _config.get("mysql_credentials", dict())
        _host = _dict.get("host", _host)
        _user = _dict.get("user", _user)
        _password = _dict.get("password", _password)
        _port = _dict.get("port", _port)
        
    credentials = ServerCredentials(_host, _user, _password, _port)

    _server:ServerConnection = ServerConnection()
    _server_con = _server.connect_to_server(credentials)
    
    _db_con:DatabaseConnection = DatabaseConnection()
    _db_con.connect_to_database(_server_con, _database_name)
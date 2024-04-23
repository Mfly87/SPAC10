from designPatterns import Singleton
from mysql.connector import MySQLConnection, Error
from mysql import connector

from .sever_credentials import ServerCredentials


class ServerConnection(Singleton):

    _mysql_connection = None

    def connect_to_server(self, credentials: ServerCredentials) -> MySQLConnection:
        self.close_connection()

        try:
            mysql_connection = connector.connect(**credentials.get_credentials_dict())
            self._mysql_connection = mysql_connection
        except Error as e:
            print(f"Error connecting to the server: {e}")
            raise

        return self.mysql_connection

    def close_connection(self) -> None:
        if self.mysql_connection is None:
            return
        try:
            self.mysql_connection.close()
            self._mysql_connection = None
        except Error as e:
            print(f"An error occoured whilst closing the server connection: {e}")
            raise

    @property
    def mysql_connection(self) -> MySQLConnection:
        return self._mysql_connection
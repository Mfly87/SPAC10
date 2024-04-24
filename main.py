from sql import ServerCredentials
from setup import setup_table_books, setup_app, setup_my_sql_connection

print("\n\n\n")

_database_name = "spac10"
_credentials = ServerCredentials(
    "localhost",
    "root",
    "Kom12345",
    3306
)

setup_my_sql_connection(_credentials, _database_name)
setup_table_books(1000)
setup_app()
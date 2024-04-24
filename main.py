from sql import ServerCredentials
from setup import setup_table_books, setup_app, setup_my_sql_connection

if __name__ == "__main__":

    print("\n\n\n")

    setup_my_sql_connection()
    setup_table_books()
    setup_app()
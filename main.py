from dataClasses import AbsSQLObj, SQLDataUser, SQLDataFactory, SQLDataBook
from dataClasses.faker import FakerBook, FakerUser
from sql import ServerCredentials, ServerConnection, DatabaseConnection, DataQueries

print("\n\n\n")

_book_gen = FakerBook()
_books = []
for _ in range(10):
    for _book in _book_gen.create_random_book():
        _books.append(_book)

_credentials = ServerCredentials(
    "localhost",
    "root",
    "Kom12345",
    3306
)

_database_name = "spac10"

_server:ServerConnection = ServerConnection()
_server_con = _server.connect_to_server(_credentials)

_db_con:DatabaseConnection = DatabaseConnection()
_db_con.connect_to_database(_server_con, _database_name)

_dict = {
    "users": dict(zip(AbsSQLObj.get_build_headers(SQLDataUser), AbsSQLObj.get_build_types(SQLDataUser))),
    "books": dict(zip(AbsSQLObj.get_build_headers(SQLDataBook), AbsSQLObj.get_build_types(SQLDataBook))),
}

_dq = DataQueries()
for _type in [SQLDataUser, SQLDataBook]:
    _dq.create_table(_type)

_dq.insert_many(_books)
from dataClasses import AbsSQLObj, SQLDataUser, SQLDataFactory

from dataClasses.faker import FakerBook, FakerUser

print("\n\n\n")

_name_gen = FakerBook()
for _ in range(10):
    _name_list = _name_gen.create_random_book()
    for _name in _name_list:
        print(_name)
        
print("\n\n\n")

_name_gen = FakerUser()
for _ in range(10):
    _name_list = _name_gen.create_random_user()
    for _name in _name_list:
        print(_name)

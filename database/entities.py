from .db_connection import db
from pony.orm import PrimaryKey, Required, Optional, Set

class User(db.Entity):
    __table__ = "user"
    id = PrimaryKey(int, auto= True)
    name = Required(str, unique= True)
    phone = Optional(int)
    company = Required(str, default= "pony_test")
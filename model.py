from peewee import *

db = SqliteDatabase("data.db")

class BaseClass(Model):
    class Meta:
        database = db

class Enuz(BaseClass):
    inglizcha = TextField()
    uzbekcha = TextField()

class Uzen(BaseClass):
    uzb = TextField()
    eng = TextField()

class Kouz(BaseClass):
    uz = TextField()
    kor  =TextField()

class Uzko(BaseClass):
    koreys  =TextField()
    uzbekk = TextField()

db.connect()
db.create_tables([Enuz, Uzen, Kouz, Uzko])
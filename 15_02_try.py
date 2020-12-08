# http://zetcode.com/python/peewee/
"""
Peewee mapping

A Model = database table
A Field = table column
An Instance = table row

Peewee uses MySQLDatabase for MySQL, PostgresqlDatabase for PostgreSQL, and SqliteDatabase for SQLite.
In this tutorial, we work with SQLite database.

"""
import peewee
import datetime

# Make a new DATABASE = test.db file in system gets created
db = peewee.SqliteDatabase('test.db')

# DB Model = Note
class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        """
        we define the reference to the database and
        the database table name

        """
        database = db
        db_table = 'notes'

# table is created and saved
Note.create_table()
# create and save a multiple instance(ROW)
# We define the data in a list of dictionaries
# one bulk create operation

data = [
    { 'text': 'Tai chi in the morning', 'created': datetime.date(2018, 10, 20) },
    { 'text': 'Visited friend', 'created': datetime.date(2018, 10, 12) },
    { 'text': 'Went to cinema', 'created': datetime.date(2018, 10, 5) },
    { 'text': 'Listened to music', 'created': datetime.date(2018, 10, 28) },
    { 'text': 'Watched TV all day', 'created': datetime.date(2018, 10, 14) },
    { 'text': 'Worked in the garden', 'created': datetime.date(2018, 10, 22) },
    { 'text': 'Walked for a hour', 'created': datetime.date(2018, 10, 28) }
]

# The atomic() method puts the bulk operation in a transaction
with db.atomic():

    query = Note.insert_many(data)
    query.execute()

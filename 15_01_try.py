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
# create and save a new instance(ROW)
note1 = Note.create(text='Went to the cinema')
note1.save()

note2 = Note.create(text='Exercised in the morning',
        created=datetime.date(2018, 10, 20))
note2.save()

note3 = Note.create(text='Worked in the garden',
        created=datetime.date(2018, 10, 22))
note3.save()

note4 = Note.create(text='Listened to music')
note4.save()

import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'notes'

# The generated SQL statements can be shown with the sql() method.
note3 = Note.select().where(Note.id == 3)
print(note3.sql())

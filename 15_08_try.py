import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'notes'


# Selsecting Specific columns
notes = Note.select(Note.text, Note.created).limit(2)

output = [e for e in notes.tuples()]
print(output)

import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'notes'

# where() method can filter data based on a given condition
notes = Note.select().where(Note.id > 3)

for note in notes:
    print('{} {} on {}'.format(note.id, note.text, note.created))

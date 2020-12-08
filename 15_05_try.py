import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'notes'

# We use two where expressions combined with the & operator.
# retrieves all rows whose id is greater than two and lower than six
notes = Note.select().where((Note.id > 2) & (Note.id < 6))

for note in notes:
    print('{} {} on {}'.format(note.id, note.text, note.created))

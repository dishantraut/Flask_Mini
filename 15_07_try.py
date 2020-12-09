import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'notes'


# There are two ways to select a single instance; each of them uses a get() method.
# First
note1 = Note.select().where(Note.text == 'Went to cinema').get()

print(note1.id)
print(note1.text)
print(note1.created)

# Second
note2 = Note.get(Note.text == 'Listened to music')

print(note2.id)
print(note2.text)
print(note2.created)

import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = 'notes'

# The update() method updates an instance. It returns the number of successfully updated instances.

query = Note.update(text='Visited Friend Updated',id=1).where(Note.id == 2)
n = query.execute()
print('# of rows updated: {}'.format(n))
query = Note.update(created=datetime.date(2018, 10, 27)).where(Note.id == 1)
n = query.execute()
print('# of rows updated: {}'.format(n))

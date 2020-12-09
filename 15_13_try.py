import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = 'notes'

# To delete more instances, we call the delete() method. It returns the number of successfully deleted instances.
query = Note.delete().where(Note.id > 3)
n = query.execute()

print('{} instances deleted'.format(n))

import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'notes'

# To calculate the number of model instances in the table, we can use the count() method.
n = Note.select().count()
print(n)

n2 = Note.select().where(Note.created >= datetime.date(2018, 10, 20)).count()
print(n2)

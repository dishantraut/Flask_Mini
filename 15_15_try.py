"""
# Got DB Browser And Fire This Query\
# Below Query will create 2 new tables called as 'customers' & 'reservations'

BEGIN TRANSACTION;
DROP TABLE IF EXISTS reservations;
DROP TABLE IF EXISTS customers;

CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO customers(Name) VALUES('Paul Novak');
INSERT INTO customers(Name) VALUES('Terry Neils');
INSERT INTO customers(Name) VALUES('Jack Fonda');
INSERT INTO customers(Name) VALUES('Tom Willis');

CREATE TABLE IF NOT EXISTS reservations(id INTEGER PRIMARY KEY,
    customer_id INTEGER, created DATE,
    FOREIGN KEY(customer_id) REFERENCES customers(id));
INSERT INTO reservations(customer_id, created) VALUES(1, '2018-22-11');
INSERT INTO reservations(customer_id, created) VALUES(2, '2018-28-11');
INSERT INTO reservations(customer_id, created) VALUES(2, '2018-29-11');
INSERT INTO reservations(customer_id, created) VALUES(1, '2018-29-11');
INSERT INTO reservations(customer_id, created) VALUES(3, '2018-02-12');
COMMIT;

"""

import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Customers(peewee.Model):

    name = peewee.TextField()

    class Meta:

        database = db
        db_table = 'customers'

class Reservations(peewee.Model):
    # A relationship between Customer and Reservation models is created with ForeignKeyField.
    # The backref attribute sets how we can refer to reservations from a customer.
    customer = peewee.ForeignKeyField(Customers, backref='reservations')
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'reservations'

customer = Customers.select().where(Customers.name == 'Paul Novak').get()

# The customer instance has a property reservations, which contains the corresponding reservations.
for reservation in customer.reservations:

    print(reservation.id)
    print(reservation.created)

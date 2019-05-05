from model import Event,Items,Sales,db
from peewee import *
from peewee import IntegrityError
from dataclasses import dataclass,field


# To add events info
def add_event(event):
    try:
        event.save()
    except IntegrityError as e:
        raise SalesError('Duplicate event name')from e


# to add items info
def add_item(item):
    try:
        item.save()
    except IntegrityError as e:
        raise SalesError("Duplicate item's info") from e


# add a sales record
def add_sales_record(sale):
    try:
        sale.save()
    except IntegrityError as e:
        raise SalesError("either event doesn't exist or item is not listed")


# get all records info
def get_all_records():
    query=(Sales
           .select(Sales.quantity.alias('quantity'), Event.eventName.alias('event'), Event.date.alias('date'),Items.itemType.alias('item'))
           .join(Event,on=(Sales.event == Event.eventId)).switch(Sales)
           .join(Items,on=(Sales.itemSold == Items.itemId))).dicts()
    # for rows in Sales.select(Sales.quantity, Event.eventName, Event.date).join(Event).dict():
    #     print(rows)
    return query


# to show quantities sold of each item and sort by rank
def get_quantity_sold():
    # rank = fn.rank().over(order_by=[fn.SUM(Sales.quantity).desc()])
    query = (Sales
             .select(fn.sum(Sales.quantity).alias('total'), Items.itemType.alias('item'))
                     # ,fn.rank().over(order_by=[fn.sum(Sales.quantity).desc()]).alias('rank'))
             .join(Items, on=Sales.itemSold==Items.itemId)
             .group_by(Items.itemType)
             .order_by(fn.sum(Sales.quantity).desc())
             ).dicts()
    # query = (Select(columns=[subq.c.item,subq.c.total])
    #     .from_(subq)
    #          .where(subq.c.rank ==1)

    # ).bind(db)
    return query

def get_all_events():
    query = Event.select()
    return list(query)

def get_all_items():
    query = Items.select()
    return list(query)

class SalesError(Exception):
    """ For BookStore errors. """
    pass

# database_file = 'sales.sqlite'
#
# class SalesStore:
#     instance = None
#
#     class __SalesStore:
#         def __init__(self):
#             self._db = sqlite3.connect(database_file)
#             self._db.row_factory = sqlite3.Row
#
#             with self._db as db:
#                 cur = db.cursor()
#                 cur.execute(
#                         'CREATE TABLE IF NOT EXISTS Events (eventId int PRIMARY KEY, eventName TEXT, eventDate date )')
#                 cur.execute(
#                     'CREATE TABLE IF NOT EXISTS Items (itemID int PRIMARY KEY, itemType TEXT, price float )')
#                 cur.execute(
#                     'CREATE TABLE IF NOT EXISTS Sales (saleID int PRIMARY KEY , quantity int , eventId INT, itemSold int, FOREIGN KEY (eventID) REFERENCES Events(eventID), FOREIGN KEY (itemSold) REFERENCES Items(itemId))')
#
 #
    # def __new__(cls):
    #     if not SalesStore.instance:
    #         SalesStore.instance = SalesStore.__SalesStore()
    #     return SalesStore.instance
    #
    #
    # def __getattr__(self, name):
    #     return getattr(self.instance, name)
    #
    #
    # def __setattr__(self, name, value):
    #     return setattr(self.instance, name, value)

# from dataclasses import dataclass, field
# import datetime
from peewee import *
db = SqliteDatabase('sales.sqlite',pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = db


# represent an event in the database
class Event(BaseModel):

    eventId=IntegerField(primary_key=True)
    eventName=CharField(unique=True)
    date= CharField()
    # class Meta:
    #     indexes = (
    #         (('eventName', 'date'), True)
    #     )
    def __str__(self):
        return f'ID {self.eventId}, Event Name: {self.eventName}, Date: {self.date}'


# represent an item in the database
class Items(BaseModel):

    itemId=IntegerField(primary_key=True)
    itemType=CharField(unique=True)
    price= FloatField()

    def __str__(self):
        return f'ID {self.itemId}, Type: {self.itemType}, Price: {self.price}'

    # class Meta:
    #     database = db
    # class Meta:
    #     indexes = (
    #         (('itemType', 'price'), True)
    #     )

# represent a sales record in the database
class Sales(BaseModel):

    saleID=IntegerField(primary_key=True)
    itemSold = ForeignKeyField(Items,field=Items.itemId)
    event=ForeignKeyField(Event, field=Event.eventId)
    quantity=IntegerField(null=False)
    # def __str__(self):
    #     return f'ID {self.itemId}, Type: {self.itemType}, Price: {self.price}'


    # class Meta:
    #     database = db



db.connect()
db.create_tables([Event,Items,Sales])
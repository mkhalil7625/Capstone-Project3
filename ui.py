from model import Event, Sales, Items
import datetime
import sales_store as store

def display_menu_get_choice(menu):
    """ Displays all of the menu options, checks that the user enters a valid choice and returns the choice.
     :param menu: the menu to display
     :returns: the user's choice """
    while True:
        print(menu)
        choice = input('Enter choice? ')
        if menu.is_valid(choice):
            return choice
        else:
            print('Not a valid choice, try again.')

def get_event_info():
    eventName = input('Enter the location of the event: ')
    eventDate = input("Enter Event's date in YYYY-MM-DD format")

    # eventDay =int(input("Enter Event's date as int: "))
    # eventMonth = int(input("Enter Event's Month as int: "))
    # eventYear = int(input("Enter Event's Year as int: "))
    # eventDate = datetime.date(eventYear,eventMonth,eventDay)
    return Event(eventName=eventName,date=eventDate)

def get_item_info():
    type = input('Enter the Type of the Item: ')
    price=float(input('Enter Price Each: '))
    return Items(itemType=type, price=price)
#
# def get_event_id():
#
# def get_item_id():
def get_sales_record_info():
    print(store.get_all_events())
    event = int(input("Choose the applicable event's id: "))
    print(store.get_all_items())
    item = int(input("Choose the sold item: "))
    quantity = int(input("Enter Quantity Sold as numbers: "))
    return Sales(itemSold=item, event=event, quantity=quantity)


def show_sales_records(query):
    for record in query:
        print(f"For the {record['date']} event at {record['event']}, {record['quantity']} {record['item']} were sold" )


def show_quantity_sold(query):
    rank = 1
    for record in query:

        print(f"{record['item']} is ranked # {rank} and we sold {record['total']} of it")
        rank+=1
def show_records(x):
    if x:
        for y in x:
            print(y)
    else:
        print('No Record to Display')
def message(msg):
    """ Prints a message for the user
     :param msg: the message to print"""
    print(msg)


def ask_question(question):
    """ Ask user question
    :param: the question to ask
    :returns: user's response """
    return input(question)

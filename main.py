from menu import Menu
import sales_store as store
from sales_store import SalesError
import ui


# store = SalesStore()
#
QUIT = 'Q'


def main():

    menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == QUIT:
            break


def create_menu():
    menu = Menu()
    menu.add_option('1', 'Add an Event',add_event)
    menu.add_option('2', 'Add Merchandise Info', add_item )
    menu.add_option('3', 'Add a Sales Record', add_sales_record)
    menu.add_option('4', 'Show all Sales Records', get_sales_records)
    menu.add_option('5', 'find quantity sold per item', quantity_sold)
    return menu


def add_event():
    new_event = ui.get_event_info()
    try:
        store.add_event(new_event)
        ui.message('Event Added')
    except SalesError as e:
        ui.message(e)

def add_item():
    new_item_info = ui.get_item_info()
    try:
        store.add_item(new_item_info)
        ui.message('Item Added')
    except SalesError as e:
        ui.message(e)

def add_sales_record():
    new_sales_record=ui.get_sales_record_info()
    try:
        store.add_sales_record(new_sales_record)
        ui.message('Record Saved')
    except SalesError as e:
        ui.message(e)

def quantity_sold():
    quantity_sold_item=store.get_quantity_sold()
    ui.show_quantity_sold(quantity_sold_item)

def get_sales_records():
    sales=store.get_all_records()
    ui.show_sales_records(sales)

def show_all_events():
    events=store.get_all_events()
    ui.show_records(events)

def show_all_items():
    items=store.get_all_items()
    ui.show_records(items)



def quit_program():
    # store.close()
    ui.message('Thanks and bye!')


if __name__ == '__main__':
    main()
import psycopg2
import pandas as pd
import pandas.io.sql as psql
from restaurant_menu_manager import MenuItem

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'first'
DATABASE = 'W6D5'



def show_user_menu():
    """Display the program menu to the user,
    ask to choose an option,
    call the next funtion according to the choice"""
    the_choice = ''
    while the_choice != 'a' or the_choice != 'd' or the_choice != 'v' or the_choice != 'x':
        the_choice = input("""Welcome to Menu_manager_v0.09b!\nPlease choose an option\n(a) Add an item to the menu\n(d) Delete an item\n(v) View the menu\n(x) Exit\n:  """)
        
        if the_choice == 'a':
            add_item()
    
        elif the_choice == 'd':
            
            delete_item()

        elif the_choice == 'v':
            show_menu()
    
        elif the_choice == 'x':
            print("See you later")
            quit() 
        return the_choice

    
def add_item():
    """creates MenuItem instance and calls save method"""
    dish_name = input("Please type the name of the dish: ")
    price = input("Please set the price of the dish: ")
    MenuItem.save(MenuItem(dish_name, price))
    print("Item was added successfully")


def delete_item():
    """creates MenuItem instance and calls delete method"""
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    menu = pd.read_sql('select dish_name from menu', connection)
    print(menu)
    dish_name = input("Please type the NAME of the dish that you want to delete: ")
    MenuItem.delete(MenuItem(dish_name, 1))


def show_menu():
    """Shows the menu"""
    MenuItem.all()


show_user_menu()


# TO-DO list:
# Make all the functions and class not case sensitive 
# Figure out how to print the table without indexes
# 
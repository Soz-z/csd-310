import sys
import mysql.connector
from mysql.connector import errorcode

# Config Data
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    print('-    Main Menu   -')
    menu_selection = int(input(' 1. View Books\n 2. Store Locations\n 3. My Account\n 4. Exit'))
    if menu_selection > 4 or menu_selection == 0:
        print("Choose a number between 1 - 4.")
        sys.exit(0)
    else:
        return menu_selection

def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")


def show_locations(_cursor):
    pass
def validate_user():
    pass
def show_account_menu():
    pass
def show_wishlist(_cursor, _user_id):
    pass
def show_books_to_add(_cursor, _user_id):
    pass
def add_book_to_wishlist(_cursor,_user_id,_book_id):
    pass



try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    user_selection = show_menu()
    









except mysql.connector.Error as err: 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    db.close()
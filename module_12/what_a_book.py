"""
    Title: what_a_book.py
    Author: Daniel Clark
    Date: 26 September 22
    Description: Whatabook database manipulation
"""



# import Statements
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

# Show menu method for displaying a menu
def show_menu():
    print('\n-    MAIN MENU    -\n')
    menu_selection = int(input(' 1. View Books\n 2. Store Locations\n 3. My Account\n 4. Exit\n\nSelection: '))
    if menu_selection > 4 or menu_selection == 0:
        print("Choose a number between 1 - 4.")
        sys.exit(0)
    else:
        return menu_selection

# Show books method for displaying all available books
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")
    books = _cursor.fetchall()
    print('-    DISPLAYING BOOKS MENU    -')
    for book in books:
        print("Book Name: {}\nAuthor: {}\n Details: {}\n".format(book[0], book[1], book[2]))

# Show locations method for displaying all locations
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")
    locations = _cursor.fetchall()
    print('\n-    DISPLAYING STORE LOCATIONS   -\n')
    for location in locations:
        print("Location: {}\n".format(location[1]))

# Validate User, checks input from user to make sure it matches a active user
def validate_user():
    user_id = int(input('\nEnter Customer ID: \n'))
    if user_id > 0 or user_id <4:
        return user_id
    else: 
        print("Invalid Customer ID, please try again\n")
        sys.exit(0)

# Shows the account menu of the user...includes try/except
def show_account_menu():
    try:
        print('\n-    CUSTOMER MENU    -\n')
        amenu_selection = int(input(' 1. Wishlist\n 2. Add Book\n 3. Main Menu\n'))
        if amenu_selection < 4 or amenu_selection > 0:
            return amenu_selection
        else:
            print("Incorrect input, please try again.")
            sys.exit(0)

    except ValueError:
        print("Invalid Menu Selection, please try again")
        sys.exit(0)

# Show wishlist that displays existing books on user wishlist, inner join
def show_wishlist(_cursor, user_id):
    # Referenced github for this function, specifically the query. I tried joining queries in the same quote.
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))
    wishlist = _cursor.fetchall()
    print('\n-    DISPLAYING WISHLIST ITEMS   -\n')
    for book in wishlist:
        print('Book Name: {}\nAuthor: {}\n'.format(book[4], book[5]))

# Add books to wishlist method
def show_books_to_add(_cursor, user_id):
    initial_query = ("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))
    print(initial_query)
    _cursor.execute(initial_query)
    books_to_add = _cursor.fetchall()
    print('\n-    DISPLAYING BOOKS AVAILABLE    -\n')
    for books in books_to_add:
        print("Book Id: {}\n Book Name: {}\n".format(books[0], books[1]))

def add_book_to_wishlist(_cursor,user_id,book_id):
    # Issues with this query as the format wasn't working
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(user_id, book_id))

def choice_3():
    user_continue = True
    while user_continue == True:
        user = validate_user()
        amenu = show_account_menu()
        # 1 for wishlist
        # 2 for add book
        # 3 for main menu
        if amenu == 1:
            show_wishlist(cursor, user)
            continuing = input("Would you like to continue? (y or n):   ")
            if continuing == 'y' or continuing == 'Y':
                pass
            else:
                user_continue = False
        elif amenu == 2:
            show_books_to_add(cursor, user)
            # user must enter book id
            try:
                book_id = int(input("Enter the id of the book to add to your wishlist: \n"))
                if book_id:
                    add_book_to_wishlist(cursor, user, book_id)
                    db.commit()
                    # Feedback for user
                    print('Book id: {} was successfully added to wishlist.\n'.format(book_id))
                    continuing = input("Would you like to continue? (y or n):   ")
                    if continuing == 'y' or continuing == 'Y':
                        pass
                    else:
                        user_continue = False
            except ValueError:
                print("Input must contain all integers, please try again")
                sys.exit(0)
        else:
            user_continue = False




try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    print("Welcome to Whatabook")
    def main():
        user_continued = True
        while user_continued is True:
            choice = show_menu()

            # 1 for show books
            # 2 for show locations
            # 3 for my account
            # 4 for exit
            if choice == 1:
                show_books(cursor)
            elif choice == 2:
                show_locations(cursor)
            elif choice == 3:
                choice_3()
            else:
                user_continued = False
            continuing = input("Exit? (y or n):   ")
            if continuing == 'n' or continuing == 'N':
                continue
            else:
                print('Program ended, goodbye')
                user_continued = False

    
    main()

except mysql.connector.Error as err: 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    db.close()
# whatabook_console_app.py
# written by Charles Jones
# https://github.com/CSkipJ/csd-310
# 10 August 2023
# This app will allow customers to access and change their wishlists with whatabook as well
# as see information relating to the store locations and hours.

# REVIEW INSTRUCTIONS #
# - command to populate database
# - command to delete database

# Requirements #
# View Books - 1
# View Store locations - 2
# my account - 3
    # Prompt for valid user_id
    # wishlist menu - 1
        # view wishlist - 1
        # add book - 2 (view books not in wishlist)
        # main menu -> back to main - 0
    # main menu -> back to main - 0


import mysql.connector
from mysql.connector import errorcode


# Basic config options for db connection
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}


"""Authenticates user by user_id."""
def user_login(_db):
    user_input = int(input("Please enter user_id: "))
    if user_input == 0:
        main_menu(_db)

    cursor = _db.cursor()
    cursor.execute('SELECT * FROM user')
    users = cursor.fetchall()

    for user in users:
        if user[0] == user_input:
            print(f'\nUser identified! Logging in as {user[2]} {user[1]}'
                  '---------------------------------------------------------------')
            my_account(_db, user)
    print("User authentication failed. PLease try again!")
    main_menu(_db)


"""View the wishlist of the user provided."""
def view_wishlist(_db, user):
    cursor = _db.cursor()
    cursor.execute('SELECT wishlist.book_id, book.book_name, user.user_id '
                   'FROM wishlist '
                   'INNER JOIN user ON wishlist.user_id = user.user_id '
                   'INNER JOIN book ON wishlist.book_id = book.book_id '
                   f'WHERE user.user_id = {user[0]}')
    wishlist = cursor.fetchall()
    print(f'\nWishlist for {user[2]}'
          '-----------------------------')
    for book in wishlist:
        print(f'Book ID: {book[0]} \t'
              f'Book Name: {book[1]}\n')

    wishlist_menu(_db, user)


"""Allows you to add a book to the user wishlist."""
def add_book(_db, user):
    cursor = _db.cursor()
    cursor.execute('SELECT book.book_id, book.book_name '
                   'FROM book '
                   'WHERE book.book_id NOT IN '
                   f'(SELECT book_id FROM wishlist WHERE user_id = {user[0]})\n')
    books_to_add = cursor.fetchall()
    print(f"\nDisplaying books available to {user[2]}\n"
          "----------------------------------------")
    for book in books_to_add:
        print(f'Book ID: {book[0]} \t'
              f'Book Name: {book[1]} \n')

    user_input = int(input('Enter book ID you would like to add to your wishlist.\n'))

    try: 
        cursor.execute('INSERT INTO wishlist (user_id, book_id) '
                       f'VALUES ({user[0]}, {user_input})')
    except:
        print('Failed to add book. Please try again.')

    wishlist_menu(_db, user)
    

"""Wishlist menu where you can view wishlist and add books to it."""
def wishlist_menu(_db, user):
    user_input = int(input('\nWishlist Menu:\n'
                           '\t 1 - View Wishlist\n'
                           '\t 2 - Add Book\n'
                           '\t 0 - Return to Main Menu\n'
                           'Enter number to choose menu option: '))
    match user_input:
        case 0: main_menu(_db)
        case 1: view_wishlist(_db, user)
        case 2: add_book(_db, user)
        case _: view_wishlist(_db, user)


"""My Account menu where wishlist can be accessed after user logged in."""
def my_account(_db, user):
    user_input = int(input('\nMy Account: \n'
                           '\t 1 - Wishlist Menu\n'
                           '\t 0 - Return to Main Menu\n'
                           'Enter number to choose menu option: '))
    match user_input:
        case 0: main_menu(_db)
        case 1: wishlist_menu(_db, user)
        case _: my_account(_db, user)


"""View store locations."""
def view_locations(_db):
    cursor = _db.cursor()
    cursor.execute('SELECT * FROM store')
    stores = cursor.fetchall()
    print('\nDisplaying store locations!\n'
          '-----------------------------')
    for store in stores:
        print(f'{store[1]}\n')
    main_menu(_db)


"""View available books in store database."""
def view_books(_db):
    cursor = _db.cursor()
    cursor.execute('SELECT * FROM book')
    books = cursor.fetchall()
    print('\nDisplaying books available at Whatabook!\n'
          '-----------------------------------------')
    for book in books:
        print(f'Book ID: {book[0]} \t'
              f'Book Name: {book[1]} - {book[2]} \n')
    main_menu(_db)


"""Main CLI menu interface.""" 
def main_menu(_db):
    user_input = int(input('\nWhatabook Book Store!\n'
                        'Main Menu: \n'
                        '\t 1 - View Books \n'
                        '\t 2 - View Store Locations \n'
                        '\t 3 - My Account \n'
                        't\ 9 - Exit\n'
                        '\t Press 0 to return to this menu at any time. \n'
                        'Enter number to choose menu option: '))
        
    match user_input:
        case 0: main_menu(_db)
        case 1: view_books(_db)
        case 2: view_locations(_db)
        case 3: user_login(_db)
        case 9: _db.close()
        case _: main_menu(_db)


# mysql user authenication and beginning of program logic
def main(_config):
    # unpack config options in connect or fail out
    try:
        db = mysql.connector.connect(**_config)
        print(f"\n Database user {_config['user']} connected to MySQL on host {_config['host']} with database {_config['database']}")

        main_menu(db)     
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("The supplied username or password is invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The specified database does not exist")
        else:
            print(err)
    finally:
        db.close()

if __name__ == "__main__":
    main(config)
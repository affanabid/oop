# import sqlite3 as dbms

# con = dbms.connect('library.db')

# cur = con.cursor()



# def add(accno, title, subtitle, author, coauthors, pages, price, category):
#     query = "INSERT INTO book (accno, title, subtitle, author, coauthors, pages, price, category) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
#     cur.execute(query, (accno, title, subtitle, author, coauthors, int(pages), float(price), category))
#     con.commit()  # Commit the changes

# import sqlite3 as dbms

# def search_book(title):
#     con = dbms.connect('library.db')
#     cur = con.cursor()

#     # Execute the query to search for a book by its title
#     cur.execute("SELECT * FROM book WHERE title LIKE ?", ('%' + title + '%',))
    
#     # Fetch all matching rows
#     rows = cur.fetchall()

#     if not rows:
#         print("No books found with that title.")
#     else:
#         print("Books found:")
#         for row in rows:
#             print(row)  # Display each matching row
    
#     con.close()

# # Example usage:
# search_title = input("Enter the title of the book to search: ")
# search_book(search_title)


# # accno = input('accno: ')
# # title = input('title: ')
# # subtitle = input('subtitle: ')
# # author = input('author: ')
# # coauthors = input('coathors: ')
# # pages = input('pages: ')
# # price = input('price: ')
# # category = input('category: ')


# # add('01', 'title', 'subtitle', 'author', 'coauthors', 10, 100, 0)

import sqlite3 
valid_options={'a','s','d','e','l','q'}
while True:
    user_input=input('Enter Operation :')
    if user_input in valid_options:
        break
    else:
      print('Choose from valid option')
      print(f'a)Add\ts)search\td)Delete\tl)List All\te)Edit\tq)Quit')   

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        accno TEXT PRIMARY KEY,
        title TEXT,
        subtitle TEXT,
        author TEXT,
        coauthors TEXT,
        pages INTEGER,
        price REAL,
        category TEXT CHECK(category IN ('issuable', 'not issuable'))
    )
''')

def insert_book(accno, title, subtitle, author, coauthors, pages, price, category):
    cursor.execute('''
        INSERT INTO books (accno, title, subtitle, author, coauthors, pages, price, category)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (accno, title, subtitle, author, coauthors, pages, price, category))
    conn.commit()

def update_book_price(accno, new_price):
    cursor.execute('''
        UPDATE books
        SET price = ?
        WHERE accno = ?
    ''', (new_price, accno))
    conn.commit()

def delete_book(accno):
    cursor.execute('''
        DELETE FROM books
        WHERE accno = ?
    ''', (accno,))
    conn.commit()

def query_all_books():
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    for rows in books:
        for row in rows:
            print(row, end=' ')
        print()

def query_books_by_name(name):
    cursor.execute('SELECT * FROM books WHERE title = ?', (name,))
    books = cursor.fetchall()
    for row in books:
        print(row)

if user_input=='s':
    print("\nEntered Book:")
    print(query_books_by_name('A Brave New World'))


if user_input=='a':
   insert_book('002', 'book2', 'sub2', 'Author2', 'coauth2', 1300, 1229.99, 'issuable')

if user_input=='l':
    print("All Books:")
    print(query_all_books())

if user_input=='e':
    update_book_price('001', 34.99)

if user_input=='d':
    delete_book('ISBN58')

if user_input=='q':
    print('The Database has been quit')

conn.close()
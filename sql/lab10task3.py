import sqlite3 

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS circulation (
        serial_no TEXT PRIMARY KEY,
        member_no TEXT,
        assc_no TEXT,
        issue_date DATE DEFAULT NULL,
        return_date DATE DEFAULT NULL
    )
''')

def issue_book(serial_no, member_no, assc_no, issue_date):
    cursor.execute('''
        INSERT INTO circulation (serial_no, member_no, assc_no, issue_date)
        VALUES (?, ?, ?, ?)
    ''', (serial_no, member_no, assc_no, issue_date))
    conn.commit()

def return_book(serial_no, return_date):
    cursor.execute('''
        UPDATE circulation
        SET return_date = ?
        WHERE serial_no = ?
    ''', (return_date, serial_no))
    conn.commit()

issue_book('0003', 'M003', '003', '2023-01-01')

conn.close()
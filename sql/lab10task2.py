import sqlite3 as dbms

def create_members_table():
    con = dbms.connect('library.db')
    cur = con.cursor()

    # Create the members table if it doesn't exist
    cur.execute('''CREATE TABLE IF NOT EXISTS members (
                    membership_number TEXT PRIMARY KEY,
                    full_name TEXT,
                    address TEXT,
                    contact_number TEXT,
                    category TEXT,
                    start_date DATE,
                    expiry_date DATE,
                    closing_date DATE,
                    fine_paid REAL
                )''')

    con.commit()
    con.close()

# Create the members table if it doesn't exist yet
# create_members_table()

import datetime

# Function to add a member
def add_member(membership_number, full_name, address, contact_number, category, start_date, expiry_date, closing_date=None, fine_paid=0.0):
    con = dbms.connect('library.db')
    cur = con.cursor()

    cur.execute('''INSERT INTO members (membership_number, full_name, address, contact_number, category, start_date, expiry_date, closing_date, fine_paid)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (membership_number, full_name, address, contact_number, category, start_date, expiry_date, closing_date, fine_paid))

    con.commit()
    con.close()

# Function to update the closing date for a member who left the library
def update_closing_date(membership_number, closing_date):
    con = dbms.connect('library.db')
    cur = con.cursor()

    cur.execute('''UPDATE members SET closing_date = ? WHERE membership_number = ?''', (closing_date, membership_number))

    con.commit()
    con.close()

# Function to extend the expiry date for a member
def extend_expiry_date(membership_number, new_expiry_date):
    con = dbms.connect('library.db')
    cur = con.cursor()

    cur.execute('''UPDATE members SET expiry_date = ? WHERE membership_number = ?''', (new_expiry_date, membership_number))

    con.commit()
    con.close()

# Example usage:
# Add a member
add_member("M005", "cram", "123 Main St", "1234567890", "M", "2023-01-01", "2024-10-10", fine_paid=100)

# # Update closing date for a leaving member
update_closing_date("M002", "2023-12-31")

# # Extend expiry date for a member
# extend_expiry_date("M001", "2024-02-01")

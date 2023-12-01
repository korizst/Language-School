import sqlite3

connection = sqlite3.connect('school.db')
connection.row_factory = sqlite3.Row

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS school (id INTEGER, first_name TEXT,"
                        "surname TEXT, username TEXT, password TEXT, permission TEXT, language TEXT"
                        "fee_paid INTEGER);")

def add_entry(id, first_name, surname, username, password, permission, language, fee_paid):
    with connection:
        connection.execute("INSERT INTO school VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
                            (id, first_name, surname, username, password, permission, language, fee_paid))

def get_entries():
    cursor = connection.execute('SELECT * FROM school')
    return cursor
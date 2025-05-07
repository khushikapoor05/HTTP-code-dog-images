import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create the users table
conn.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    registration_date TEXT NOT NULL
)''')

# Create the lists table
conn.execute('''CREATE TABLE IF NOT EXISTS lists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)''')

# Create the list_items table
conn.execute('''CREATE TABLE IF NOT EXISTS list_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    list_id INTEGER NOT NULL,
    response_code TEXT NOT NULL,
    FOREIGN KEY (list_id) REFERENCES lists(id)
)''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database initialized and tables created.")

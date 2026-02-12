import sqlite3

DB_NAME = "inventory.db"

def get_connection():
    """Create and return a database connection"""
    return sqlite3.connect(DB_NAME)

def create_tables():
    """Create all necessary tables for the inventory system"""
    conn = get_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('Admin', 'Staff'))
    )
    """)

    # Products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        category TEXT,
        price REAL NOT NULL CHECK(price >= 0),
        quantity_in_stock INTEGER NOT NULL DEFAULT 0 CHECK(quantity_in_stock >= 0),
        supplier_name TEXT,
        minimum_stock_level INTEGER NOT NULL DEFAULT 0 CHECK(minimum_stock_level >= 0)
    )
    """)

    # Inventory transactions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory_transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        transaction_type TEXT NOT NULL CHECK(transaction_type IN ('IN', 'OUT')),
        user_id INTEGER NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    """)

    conn.commit()
    conn.close()
    print("Database tables created successfully.")
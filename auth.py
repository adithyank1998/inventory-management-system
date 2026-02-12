import sqlite3
from database import get_connection

def create_default_admin():
    """Create a default admin user if none exists"""
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE role='Admin'")
        admin = cursor.fetchone()

        if not admin:
            cursor.execute("""
            INSERT INTO users (username, password, role)
            VALUES ('admin', 'admin123', 'Admin')
            """)
            conn.commit()
            print("Default admin account created (username: admin, password: admin123)")
    except Exception as e:
        print(f"Error creating default admin: {e}")
    finally:
        conn.close()

def login():
    """Handle user login and return user details"""
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT user_id, username, role FROM users
        WHERE username=? AND password=?
        """, (username, password))

        user = cursor.fetchone()

        if user:
            print(f"\n✓ Login successful! Welcome, {user[1]} ({user[2]})")
            return user  # Returns (user_id, username, role)
        else:
            print("\n✗ Invalid credentials. Please try again.")
            return None
    except Exception as e:
        print(f"Error during login: {e}")
        return None
    finally:
        conn.close()

def create_staff():
    """Create a new staff user account"""
    username = input("Enter staff username: ").strip()
    password = input("Enter staff password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO users (username, password, role)
        VALUES (?, ?, 'Staff')
        """, (username, password))

        conn.commit()
        print(f"✓ Staff user '{username}' created successfully.")
    except sqlite3.IntegrityError:
        print(f"✗ Username '{username}' already exists. Please choose a different username.")
    except Exception as e:
        print(f"Error creating staff user: {e}")
    finally:
        conn.close()
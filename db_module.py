import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        return mysql.connector.connect(
            host="yourHost",
            user="yourUserName",
            password="yourPassword",
            database="yourDatabase" #Use PHPMYADMIN for this database.

        )
    except Error as e:
        print(f"Error: {e}")
        return None

def insert_user(role, username, password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        if role.lower() == "admin":
            query = "INSERT INTO admins (username, password) VALUES (%s, %s)"
            cursor.execute(query, (username, password))
        else:
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (username.strip(), f"{username.strip()}@mail.com", password.strip()))
        conn.commit()
    except Error as e:
        print(f"Insert error: {e}")
    finally:
        cursor.close()
        conn.close()

def validate_login(role, username, password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        if role.lower() == "admin":
            query = "SELECT * FROM admins WHERE username=%s AND password=%s"
        else:
            query = "SELECT * FROM users WHERE name=%s AND password=%s"
        cursor.execute(query, (username, password))
        return cursor.fetchone() is not None
    except Error as e:
        print(f"Login error: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def save_order(user_id, name, phone, email, order_summary, total_price):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO orders (user_id, name, phone, email, order_summary, total_price)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (user_id, name, phone, email, order_summary, total_price))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print("Error saving order:", e)
        return None
    finally:
        cursor.close()
        conn.close()

def fetch_orders():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM orders")
        return cursor.fetchall()
    except Error as e:
        print(f"Fetch error: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_user_id(name):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        query = "SELECT id FROM users WHERE name=%s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        return result[0] if result else None
    except Error as e:
        print(f"User ID fetch error: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def fetch_menu_items():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, name, price FROM menu_items ORDER BY id")
        return cursor.fetchall()
    except Error as e:
        print(f"Error fetching menu items: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def add_menu_item(name, price):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO menu_items (name, price) VALUES (%s, %s)", (name, price))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error adding menu item: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def delete_menu_item(item_id):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM menu_items WHERE id = %s", (item_id,))
        conn.commit()
    except Error as e:
        print(f"Error deleting menu item: {e}")
    finally:
        cursor.close()
        conn.close()

def delete_order_from_db(order_id):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
        conn.commit()
    except Error as e:
        print(f"Error deleting order: {e}")
    finally:
        cursor.close()
        conn.close()

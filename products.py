from database import get_connection
from transactions import stock_in, stock_out
from reports import (
    view_all_transactions,
    view_my_transactions,
    export_transactions_to_csv,
    low_stock_alert,
    generate_inventory_report
)
from auth import create_staff


# ADMIN MENU

def admin_menu(user_id, username):
    """Admin menu with full access to all features"""
    while True:
        print(f"""
{'='*50}
ADMIN MENU - {username}
{'='*50}
1. Add Product
2. View All Products
3. Update Product
4. Delete Product
5. View All Transactions
6. Export Transactions to CSV
7. Low Stock Alerts
8. Inventory Summary Report
9. Create Staff User
10. Logout
{'='*50}
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            update_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            view_all_transactions()

        elif choice == "6":
            export_transactions_to_csv()

        elif choice == "7":
            low_stock_alert()

        elif choice == "8":
            generate_inventory_report()

        elif choice == "9":
            create_staff()

        elif choice == "10":
            print("\nLogging out... Goodbye!")
            break

        else:
            print("✗ Invalid choice. Please try again.")


# STAFF MENU

def staff_menu(user_id, username):
    """Staff menu with limited access"""
    while True:
        print(f"""
{'='*50}
STAFF MENU - {username}
{'='*50}
1. View Products
2. Stock IN (Add Stock)
3. Stock OUT (Remove Stock)
4. View My Transactions
5. Low Stock Alerts
6. Logout
{'='*50}
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_products()

        elif choice == "2":
            try:
                product_id = int(input("Enter Product ID: "))
                qty = int(input("Enter quantity to add: "))
                stock_in(product_id, qty, user_id)
            except ValueError:
                print("✗ Invalid input. Please enter valid numbers.")

        elif choice == "3":
            try:
                product_id = int(input("Enter Product ID: "))
                qty = int(input("Enter quantity to remove: "))
                stock_out(product_id, qty, user_id)
            except ValueError:
                print("✗ Invalid input. Please enter valid numbers.")

        elif choice == "4":
            view_my_transactions(user_id)

        elif choice == "5":
            low_stock_alert()

        elif choice == "6":
            print("\nLogging out... Goodbye!")
            break

        else:
            print("✗ Invalid choice. Please try again.")


# PRODUCT FUNCTIONS

def add_product():
    """Add a new product to the inventory"""
    print("\n--- Add New Product ---")
    
    try:
        name = input("Product name: ").strip()
        if not name:
            print("✗ Product name cannot be empty.")
            return

        category = input("Category: ").strip()
        price = float(input("Price: "))
        
        if price < 0:
            print("✗ Price cannot be negative.")
            return

        quantity = int(input("Initial quantity: "))
        if quantity < 0:
            print("✗ Quantity cannot be negative.")
            return

        supplier = input("Supplier name: ").strip()
        min_stock = int(input("Minimum stock level: "))
        
        if min_stock < 0:
            print("✗ Minimum stock level cannot be negative.")
            return

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO products
        (product_name, category, price, quantity_in_stock, supplier_name, minimum_stock_level)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, category, price, quantity, supplier, min_stock))

        conn.commit()
        product_id = cursor.lastrowid
        conn.close()

        print(f"\n✓ Product added successfully!")
        print(f"  Product ID: {product_id}")
        print(f"  Name: {name}")
        print(f"  Category: {category}")
        print(f"  Price: ₹{price:.2f}")
        print(f"  Initial Stock: {quantity}")

    except ValueError:
        print("✗ Invalid input. Please enter correct data types.")
    except Exception as e:
        print(f"✗ Error adding product: {e}")


def view_products():
    """Display all products in the inventory"""
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT product_id, product_name, category, price, quantity_in_stock, 
               supplier_name, minimum_stock_level
        FROM products
        ORDER BY product_id
        """)
        products = cursor.fetchall()

        if not products:
            print("\n No products found in inventory.")
            return

        print("\n" + "="*100)
        print("PRODUCT INVENTORY")
        print("="*100)
        print(f"{'ID':<6} {'Name':<20} {'Category':<15} {'Price':<10} {'Stock':<8} {'Supplier':<15} {'Min Stock':<10}")
        print("-"*100)
        
        for p in products:
            stock_status = "⚠ LOW" if p[4] <= p[6] else ""
            print(f"{p[0]:<6} {p[1]:<20} {p[2]:<15} ₹{p[3]:<9.2f} {p[4]:<8} {p[5]:<15} {p[6]:<10} {stock_status}")
        
        print("="*100)
        print(f"Total Products: {len(products)}")

    except Exception as e:
        print(f"Error viewing products: {e}")
    finally:
        conn.close()


def update_product():
    """Update product details"""
    print("\n--- Update Product ---")
    
    try:
        product_id = int(input("Enter Product ID to update: "))

        conn = get_connection()
        cursor = conn.cursor()

        # Check if product exists
        cursor.execute("SELECT product_name FROM products WHERE product_id = ?", (product_id,))
        product = cursor.fetchone()

        if not product:
            print(f"✗ Product ID {product_id} not found.")
            conn.close()
            return

        print(f"Updating: {product[0]}")
        print("\nWhat would you like to update?")
        print("1. Product Name")
        print("2. Category")
        print("3. Price")
        print("4. Quantity in Stock")
        print("5. Supplier Name")
        print("6. Minimum Stock Level")
        print("7. Cancel")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            new_value = input("Enter new product name: ").strip()
            cursor.execute("UPDATE products SET product_name = ? WHERE product_id = ?", 
                         (new_value, product_id))
        elif choice == "2":
            new_value = input("Enter new category: ").strip()
            cursor.execute("UPDATE products SET category = ? WHERE product_id = ?", 
                         (new_value, product_id))
        elif choice == "3":
            new_value = float(input("Enter new price: "))
            cursor.execute("UPDATE products SET price = ? WHERE product_id = ?", 
                         (new_value, product_id))
        elif choice == "4":
            new_value = int(input("Enter new quantity: "))
            cursor.execute("UPDATE products SET quantity_in_stock = ? WHERE product_id = ?", 
                         (new_value, product_id))
        elif choice == "5":
            new_value = input("Enter new supplier name: ").strip()
            cursor.execute("UPDATE products SET supplier_name = ? WHERE product_id = ?", 
                         (new_value, product_id))
        elif choice == "6":
            new_value = int(input("Enter new minimum stock level: "))
            cursor.execute("UPDATE products SET minimum_stock_level = ? WHERE product_id = ?", 
                         (new_value, product_id))
        elif choice == "7":
            print("Update cancelled.")
            conn.close()
            return
        else:
            print("✗ Invalid choice.")
            conn.close()
            return

        conn.commit()
        print("✓ Product updated successfully.")

    except ValueError:
        print("✗ Invalid input.")
    except Exception as e:
        print(f"✗ Error updating product: {e}")
    finally:
        conn.close()


def delete_product():
    """Delete a product from inventory"""
    print("\n--- Delete Product ---")
    
    try:
        product_id = int(input("Enter Product ID to delete: "))

        conn = get_connection()
        cursor = conn.cursor()

        # Check if product exists
        cursor.execute("SELECT product_name FROM products WHERE product_id = ?", (product_id,))
        product = cursor.fetchone()

        if not product:
            print(f"✗ Product ID {product_id} not found.")
            conn.close()
            return

        confirm = input(f"Are you sure you want to delete '{product[0]}'? (yes/no): ").strip().lower()

        if confirm == "yes":
            cursor.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
            conn.commit()
            print(f"✓ Product '{product[0]}' deleted successfully.")
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("✗ Invalid input.")
    except Exception as e:
        print(f"✗ Error deleting product: {e}")
    finally:
        conn.close()
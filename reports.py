import csv
from database import get_connection


def view_all_transactions():
    """View all transactions in the system (Admin only)"""
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT t.transaction_id, p.product_name, t.quantity,
               t.transaction_type, u.username, t.date
        FROM inventory_transactions t
        JOIN products p ON t.product_id = p.product_id
        JOIN users u ON t.user_id = u.user_id
        ORDER BY t.date DESC
        """)

        rows = cursor.fetchall()

        if not rows:
            print("\n No transactions found.")
            return

        print("\n" + "="*80)
        print("ALL INVENTORY TRANSACTIONS")
        print("="*80)
        print(f"{'ID':<6} {'Product':<20} {'Qty':<6} {'Type':<6} {'User':<15} {'Date':<20}")
        print("-"*80)
        for r in rows:
            print(f"{r[0]:<6} {r[1]:<20} {r[2]:<6} {r[3]:<6} {r[4]:<15} {r[5]:<20}")
        print("="*80)
        print(f"Total Transactions: {len(rows)}")

    except Exception as e:
        print(f"Error viewing transactions: {e}")
    finally:
        conn.close()


def view_my_transactions(user_id):
    """View transactions for a specific user"""
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT t.transaction_id, p.product_name, t.quantity,
               t.transaction_type, t.date
        FROM inventory_transactions t
        JOIN products p ON t.product_id = p.product_id
        WHERE t.user_id = ?
        ORDER BY t.date DESC
        """, (user_id,))

        rows = cursor.fetchall()

        if not rows:
            print("\n You haven't made any transactions yet.")
            return

        print("\n" + "="*75)
        print("MY INVENTORY TRANSACTIONS")
        print("="*75)
        print(f"{'ID':<6} {'Product':<20} {'Qty':<6} {'Type':<6} {'Date':<20}")
        print("-"*75)
        for r in rows:
            print(f"{r[0]:<6} {r[1]:<20} {r[2]:<6} {r[3]:<6} {r[4]:<20}")
        print("="*75)
        print(f"Total Transactions: {len(rows)}")

    except Exception as e:
        print(f"Error viewing your transactions: {e}")
    finally:
        conn.close()


def export_transactions_to_csv():
    """Export all transactions to a CSV file"""
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT t.transaction_id,
               p.product_name,
               t.quantity,
               t.transaction_type,
               u.username,
               t.date
        FROM inventory_transactions t
        JOIN products p ON t.product_id = p.product_id
        JOIN users u ON t.user_id = u.user_id
        ORDER BY t.date DESC
        """)

        rows = cursor.fetchall()

        if not rows:
            print("\n No transactions available to export.")
            return

        filename = "inventory_transactions.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            # CSV header
            writer.writerow([
                "Transaction ID",
                "Product Name",
                "Quantity",
                "Transaction Type",
                "User",
                "Date"
            ])

            # CSV rows
            writer.writerows(rows)

        print(f"\n✓ {len(rows)} transactions exported to '{filename}'")

    except Exception as e:
        print(f"Error exporting transactions: {e}")
    finally:
        conn.close()


def low_stock_alert():
    """Display products that are at or below minimum stock level"""
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT product_id, product_name, category, quantity_in_stock, minimum_stock_level
        FROM products
        WHERE quantity_in_stock <= minimum_stock_level
        ORDER BY quantity_in_stock ASC
        """)

        products = cursor.fetchall()

        if not products:
            print("\n✓ All products have sufficient stock.")
            return

        print("\n" + "="*80)
        print("⚠ LOW STOCK ALERTS")
        print("="*80)
        print(f"{'ID':<6} {'Product':<25} {'Category':<15} {'Stock':<8} {'Min Required':<12}")
        print("-"*80)
        for p in products:
            print(f"{p[0]:<6} {p[1]:<25} {p[2]:<15} {p[3]:<8} {p[4]:<12}")
        print("="*80)
        print(f"Total Low Stock Items: {len(products)}")

    except Exception as e:
        print(f"Error checking stock levels: {e}")
    finally:
        conn.close()


def generate_inventory_report():
    """Generate a comprehensive inventory report"""
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Get total products
        cursor.execute("SELECT COUNT(*) FROM products")
        total_products = cursor.fetchone()[0]

        # Get total inventory value
        cursor.execute("SELECT SUM(price * quantity_in_stock) FROM products")
        total_value = cursor.fetchone()[0] or 0

        # Get low stock count
        cursor.execute("""
        SELECT COUNT(*) FROM products 
        WHERE quantity_in_stock <= minimum_stock_level
        """)
        low_stock_count = cursor.fetchone()[0]

        # Get transaction summary
        cursor.execute("""
        SELECT transaction_type, COUNT(*), SUM(quantity)
        FROM inventory_transactions
        GROUP BY transaction_type
        """)
        transaction_summary = cursor.fetchall()

        print("\n" + "="*60)
        print("INVENTORY SUMMARY REPORT")
        print("="*60)
        print(f"Total Products: {total_products}")
        print(f"Total Inventory Value: ₹{total_value:.2f}")
        print(f"Low Stock Items: {low_stock_count}")
        print("\nTransaction Summary:")
        for trans in transaction_summary:
            print(f"  {trans[0]}: {trans[1]} transactions, {trans[2]} total units")
        print("="*60)

    except Exception as e:
        print(f"Error generating report: {e}")
    finally:
        conn.close()
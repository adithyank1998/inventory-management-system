from database import get_connection


def stock_in(product_id, qty, user_id):
    """Add stock to inventory (Stock IN transaction)"""
    if qty <= 0:
        print("✗ Quantity must be greater than 0.")
        return

    conn = get_connection()
    cur = conn.cursor()

    try:
        # Check if product exists
        cur.execute(
            "SELECT product_name, quantity_in_stock FROM products WHERE product_id = ?",
            (product_id,)
        )
        product = cur.fetchone()

        if not product:
            print(f"✗ Invalid product ID: {product_id}")
            conn.close()
            return

        product_name, current_stock = product

        # Update stock
        cur.execute(
            "UPDATE products SET quantity_in_stock = quantity_in_stock + ? WHERE product_id = ?",
            (qty, product_id)
        )

        # Insert transaction record
        cur.execute("""
            INSERT INTO inventory_transactions (product_id, quantity, transaction_type, user_id)
            VALUES (?, ?, 'IN', ?)
        """, (product_id, qty, user_id))

        conn.commit()
        new_stock = current_stock + qty
        print(f"✓ Stock added successfully!")
        print(f"  Product: {product_name}")
        print(f"  Quantity Added: {qty}")
        print(f"  Previous Stock: {current_stock}")
        print(f"  New Stock: {new_stock}")

    except Exception as e:
        conn.rollback()
        print(f"✗ Error adding stock: {e}")
    finally:
        conn.close()


def stock_out(product_id, qty, user_id):
    """Remove stock from inventory (Stock OUT transaction)"""
    if qty <= 0:
        print("✗ Quantity must be greater than 0.")
        return

    conn = get_connection()
    cur = conn.cursor()

    try:
        # Get product details
        cur.execute(
            "SELECT product_name, price, quantity_in_stock FROM products WHERE product_id = ?",
            (product_id,)
        )
        product = cur.fetchone()

        if not product:
            print(f"✗ Invalid product ID: {product_id}")
            conn.close()
            return

        name, price, stock = product

        if qty > stock:
            print(f"✗ Insufficient stock!")
            print(f"  Available: {stock}")
            print(f"  Requested: {qty}")
            conn.close()
            return

        total = price * qty

        # Update stock
        cur.execute(
            "UPDATE products SET quantity_in_stock = quantity_in_stock - ? WHERE product_id = ?",
            (qty, product_id)
        )

        # Insert transaction
        cur.execute("""
            INSERT INTO inventory_transactions (product_id, quantity, transaction_type, user_id)
            VALUES (?, ?, 'OUT', ?)
        """, (product_id, qty, user_id))

        conn.commit()
        new_stock = stock - qty
        print(f"✓ Stock removed successfully!")
        print(f"  Product: {name}")
        print(f"  Quantity Removed: {qty}")
        print(f"  Total Value: ₹{total:.2f}")
        print(f"  Previous Stock: {stock}")
        print(f"  New Stock: {new_stock}")

    except Exception as e:
        conn.rollback()
        print(f"✗ Error removing stock: {e}")
    finally:
        conn.close()
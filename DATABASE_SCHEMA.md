# Database Schema Documentation

## Overview
The Inventory Management System uses **SQLite3** as its database engine. The database consists of three main tables with proper relationships and constraints.

**Database File:** `inventory.db` (auto-created on first run)

---

## Entity Relationship Diagram (ERD)

```
┌─────────────────┐
│     USERS       │
├─────────────────┤
│ user_id (PK)    │──┐
│ username        │  │
│ password        │  │
│ role            │  │
└─────────────────┘  │
                     │
                     │ (Foreign Key)
                     │
┌─────────────────┐  │     ┌──────────────────────────┐
│    PRODUCTS     │  │     │  INVENTORY_TRANSACTIONS  │
├─────────────────┤  │     ├──────────────────────────┤
│ product_id (PK) │──┼────→│ transaction_id (PK)      │
│ product_name    │  │     │ product_id (FK)          │
│ category        │  │     │ quantity                 │
│ price           │  │     │ transaction_type         │
│ quantity_in_stock│ │     │ user_id (FK)             │←──┘
│ supplier_name   │  │     │ date                     │
│ minimum_stock   │  │     └──────────────────────────┘
└─────────────────┘  │
```

---

## Table 1: USERS

Stores user account information for authentication and authorization.

### Schema

```sql
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('Admin', 'Staff'))
);
```

### Column Details

| Column    | Data Type | Constraints                      | Description                          |
|-----------|-----------|----------------------------------|--------------------------------------|
| user_id   | INTEGER   | PRIMARY KEY, AUTOINCREMENT       | Unique identifier for each user      |
| username  | TEXT      | UNIQUE, NOT NULL                 | Login username (must be unique)      |
| password  | TEXT      | NOT NULL                         | User password (plain text)*          |
| role      | TEXT      | NOT NULL, CHECK(Admin/Staff)     | User role for access control         |

**Note:** *Passwords are currently stored in plain text. For production use, implement password hashing (bcrypt, argon2, etc.).*

### Sample Data

```sql
INSERT INTO users (username, password, role) VALUES 
('admin', 'admin123', 'Admin'),
('staff1', 'staff123', 'Staff'),
('staff2', 'pass456', 'Staff');
```

### Indexes
- Primary Key Index on `user_id` (automatic)
- Unique Index on `username` (automatic due to UNIQUE constraint)

---

## Table 2: PRODUCTS

Stores product inventory information.

### Schema

```sql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category TEXT,
    price REAL NOT NULL CHECK(price >= 0),
    quantity_in_stock INTEGER NOT NULL DEFAULT 0 CHECK(quantity_in_stock >= 0),
    supplier_name TEXT,
    minimum_stock_level INTEGER NOT NULL DEFAULT 0 CHECK(minimum_stock_level >= 0)
);
```

### Column Details

| Column               | Data Type | Constraints                    | Description                              |
|----------------------|-----------|--------------------------------|------------------------------------------|
| product_id           | INTEGER   | PRIMARY KEY, AUTOINCREMENT     | Unique product identifier                |
| product_name         | TEXT      | NOT NULL                       | Name of the product                      |
| category             | TEXT      | NULL allowed                   | Product category (Electronics, etc.)     |
| price                | REAL      | NOT NULL, >= 0                 | Unit price in INR                        |
| quantity_in_stock    | INTEGER   | NOT NULL, >= 0, DEFAULT 0      | Current available stock quantity         |
| supplier_name        | TEXT      | NULL allowed                   | Name of the supplier                     |
| minimum_stock_level  | INTEGER   | NOT NULL, >= 0, DEFAULT 0      | Threshold for low stock alerts           |

### Sample Data

```sql
INSERT INTO products 
(product_name, category, price, quantity_in_stock, supplier_name, minimum_stock_level) 
VALUES 
('Laptop', 'Electronics', 45000.00, 50, 'TechSupply Inc', 10),
('Mouse', 'Electronics', 500.00, 200, 'TechSupply Inc', 50),
('Keyboard', 'Electronics', 1500.00, 100, 'TechSupply Inc', 30),
('Monitor', 'Electronics', 12000.00, 25, 'DisplayCo', 5);
```

### Business Rules
- Price cannot be negative
- Stock quantity cannot be negative
- Minimum stock level triggers low-stock alerts
- When `quantity_in_stock <= minimum_stock_level`, product appears in alerts

---

## Table 3: INVENTORY_TRANSACTIONS

Records all stock movements (IN and OUT operations).

### Schema

```sql
CREATE TABLE inventory_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    transaction_type TEXT NOT NULL CHECK(transaction_type IN ('IN', 'OUT')),
    user_id INTEGER NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

### Column Details

| Column           | Data Type | Constraints                           | Description                          |
|------------------|-----------|---------------------------------------|--------------------------------------|
| transaction_id   | INTEGER   | PRIMARY KEY, AUTOINCREMENT            | Unique transaction identifier        |
| product_id       | INTEGER   | NOT NULL, FOREIGN KEY → products      | Reference to product involved        |
| quantity         | INTEGER   | NOT NULL                              | Quantity moved (positive number)     |
| transaction_type | TEXT      | NOT NULL, CHECK(IN/OUT)               | Type: 'IN' (add) or 'OUT' (remove)   |
| user_id          | INTEGER   | NOT NULL, FOREIGN KEY → users         | User who performed transaction       |
| date             | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP             | Auto-generated timestamp             |

### Sample Data

```sql
INSERT INTO inventory_transactions 
(product_id, quantity, transaction_type, user_id) 
VALUES 
(1, 20, 'IN', 2),   -- Staff added 20 laptops
(1, 5, 'OUT', 2),   -- Staff removed 5 laptops
(2, 100, 'IN', 2),  -- Staff added 100 mice
(3, 10, 'OUT', 2);  -- Staff removed 10 keyboards
```

### Transaction Types

| Type | Description                | Effect on Stock           |
|------|----------------------------|---------------------------|
| IN   | Stock addition/receiving   | Increases quantity_in_stock |
| OUT  | Stock removal/sale         | Decreases quantity_in_stock |

### Foreign Key Relationships

1. **product_id → products(product_id)**
   - Links transaction to specific product
   - Enables joining to get product details

2. **user_id → users(user_id)**
   - Links transaction to user who performed it
   - Enables audit trail

---

## Database Queries

### Common Query Patterns

#### 1. View All Transactions with Details
```sql
SELECT 
    t.transaction_id,
    p.product_name,
    t.quantity,
    t.transaction_type,
    u.username,
    t.date
FROM inventory_transactions t
JOIN products p ON t.product_id = p.product_id
JOIN users u ON t.user_id = u.user_id
ORDER BY t.date DESC;
```

#### 2. Check Low Stock Products
```sql
SELECT 
    product_id,
    product_name,
    category,
    quantity_in_stock,
    minimum_stock_level
FROM products
WHERE quantity_in_stock <= minimum_stock_level
ORDER BY quantity_in_stock ASC;
```

#### 3. Calculate Total Inventory Value
```sql
SELECT SUM(price * quantity_in_stock) AS total_value
FROM products;
```

#### 4. User Transaction History
```sql
SELECT 
    t.transaction_id,
    p.product_name,
    t.quantity,
    t.transaction_type,
    t.date
FROM inventory_transactions t
JOIN products p ON t.product_id = p.product_id
WHERE t.user_id = ?
ORDER BY t.date DESC;
```

#### 5. Product Transaction History
```sql
SELECT 
    t.transaction_id,
    u.username,
    t.quantity,
    t.transaction_type,
    t.date
FROM inventory_transactions t
JOIN users u ON t.user_id = u.user_id
WHERE t.product_id = ?
ORDER BY t.date DESC;
```

---

## Database Constraints & Validation

### Primary Key Constraints
- Ensures each record has a unique identifier
- Auto-incrementing for easy insertion

### Foreign Key Constraints
- Maintains referential integrity
- Prevents orphaned transactions
- Ensures valid product and user references

### Check Constraints
1. **Price validation**: `price >= 0`
2. **Stock validation**: `quantity_in_stock >= 0`
3. **Minimum stock validation**: `minimum_stock_level >= 0`
4. **Role validation**: `role IN ('Admin', 'Staff')`
5. **Transaction type validation**: `transaction_type IN ('IN', 'OUT')`

### NOT NULL Constraints
- Critical fields cannot be empty
- Ensures data completeness

### UNIQUE Constraints
- Username must be unique
- Prevents duplicate accounts

---

## Database Initialization

The database is automatically created on first run via `database.py`:

```python
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Creates all three tables
    # Sets up constraints
    # Establishes foreign keys
    
    conn.commit()
    conn.close()
```

### Default Data
- **Admin account** is auto-created on first run
  - Username: `admin`
  - Password: `admin123`
  - Role: `Admin`

---

## Database Maintenance

### Backup
```bash
# Create backup
cp inventory.db inventory_backup_$(date +%Y%m%d).db
```

### Reset Database
```bash
# Delete and recreate
rm inventory.db
python main.py
```

### View Database
```bash
# Using SQLite command line
sqlite3 inventory.db
.tables
.schema users
SELECT * FROM users;
.exit
```

---

## Performance Considerations

### Indexes
- Primary keys are automatically indexed
- Consider adding indexes for frequently queried columns:
  ```sql
  CREATE INDEX idx_product_category ON products(category);
  CREATE INDEX idx_transaction_date ON inventory_transactions(date);
  CREATE INDEX idx_transaction_type ON inventory_transactions(transaction_type);
  ```

### Query Optimization
- Use JOINs instead of multiple queries
- Filter early with WHERE clauses
- Limit result sets when appropriate

---

## Security Considerations

### Current Implementation
**Warning**: Current security measures are basic and suitable only for learning/demo purposes.

### Recommendations for Production
1. **Password Hashing**: Implement bcrypt or argon2
2. **SQL Injection Prevention**: Use parameterized queries (already implemented)
3. **Access Control**: Implement session management
4. **Encryption**: Encrypt sensitive data at rest
5. **Audit Logging**: Log all security-relevant events
6. **Backup Strategy**: Regular automated backups

---

## Future Enhancements

1. **Add Indexes** for better query performance
2. **Soft Deletes** instead of hard deletes
3. **Audit Trail** table for tracking all changes
4. **Product Categories** as separate table (normalization)
5. **Suppliers** as separate table with relationships
6. **Transaction Details** table for additional metadata
7. **User Sessions** table for login tracking
8. **Product Images** blob storage or file paths

---

## Database Size Estimates

| Records        | Approximate Size |
|----------------|------------------|
| 100 products   | ~50 KB           |
| 1,000 trans.   | ~200 KB          |
| 10,000 trans.  | ~2 MB            |
| 100,000 trans. | ~20 MB           |

SQLite can handle databases up to 281 TB, making it suitable for small to medium inventory systems.

---

**Last Updated:** February 2026  
**Database Version:** 1.0  
**Compatible SQLite Version:** 3.x
# Inventory Management System (Python + SQLite)

## Project Overview

This is a **Command-Line Inventory Management System** built with **Python** and **SQLite3**.  
The system features role-based access control (Admin & Staff), product management, stock tracking, transaction logging, low-stock alerts, and CSV export functionality.

---

## Features

### Admin Capabilities
- Add, update, and delete products
- View all products in inventory
- View all system transactions
- Export transaction history to CSV
- Monitor low-stock alerts
- Generate inventory summary reports
- Create new staff accounts

### Staff Capabilities
- View product inventory
- Perform Stock IN operations (add inventory)
- Perform Stock OUT operations (remove inventory)
- View personal transaction history
- Check low-stock alerts

---

## Project Structure

```
Inventory-Management/
│
├── main.py                  # Application entry point
├── database.py              # Database initialization and connection
├── auth.py                  # User authentication and account management
├── products.py              # Product CRUD operations and menu systems
├── transactions.py          # Stock IN/OUT transaction handling
├── reports.py               # Reporting and analytics functions
├── inventory.db             # SQLite database (auto-created)
├── inventory_transactions.csv  # Transaction export file (auto-created)
└── README.md                # Project documentation
```

---

## Technologies Used

- **Python 3.x**
- **SQLite3** - Embedded database
- **CSV Module** - Data export functionality
- **Command Line Interface (CLI)**

---

## Database Schema

### 1. Users Table
| Column   | Type    | Constraints                     |
|----------|---------|----------------------------------|
| user_id  | INTEGER | PRIMARY KEY, AUTOINCREMENT       |
| username | TEXT    | UNIQUE, NOT NULL                 |
| password | TEXT    | NOT NULL                         |
| role     | TEXT    | NOT NULL (Admin / Staff)         |

### 2. Products Table
| Column               | Type    | Constraints                |
|----------------------|---------|----------------------------|
| product_id           | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| product_name         | TEXT    | NOT NULL                   |
| category             | TEXT    |                            |
| price                | REAL    | NOT NULL, >= 0             |
| quantity_in_stock    | INTEGER | NOT NULL, >= 0, DEFAULT 0  |
| supplier_name        | TEXT    |                            |
| minimum_stock_level  | INTEGER | NOT NULL, >= 0, DEFAULT 0  |

### 3. Inventory Transactions Table
| Column           | Type      | Constraints                      |
|------------------|-----------|----------------------------------|
| transaction_id   | INTEGER   | PRIMARY KEY, AUTOINCREMENT       |
| product_id       | INTEGER   | FOREIGN KEY → products           |
| quantity         | INTEGER   | NOT NULL                         |
| transaction_type | TEXT      | NOT NULL (IN / OUT)              |
| user_id          | INTEGER   | FOREIGN KEY → users              |
| date             | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP        |

---

## Installation & Setup

### Prerequisites
- Python 3.6 or higher installed on your system

### Step 1: Clone or Download the Project
```bash
git clone <your-repository-url>
cd Inventory-Management
```

### Step 2: Verify Python Installation
```bash
python --version
# or
python3 --version
```

### Step 3: Run the Application
```bash
python main.py
# or
python3 main.py
```

The database (`inventory.db`) will be created automatically on first run.

---

## Default Login Credentials

### Admin Account
- **Username:** `admin`
- **Password:** `admin123`

### Staff Account
You can create staff accounts through the Admin menu (Option 9).

---

## Usage Guide

### Admin Workflow
1. Login with admin credentials
2. Add products to inventory
3. Create staff user accounts
4. Monitor all transactions
5. Check low-stock alerts
6. Export data to CSV for analysis

### Staff Workflow
1. Login with staff credentials
2. View available products
3. Perform Stock IN when receiving inventory
4. Perform Stock OUT when selling/issuing items
5. Track personal transaction history
6. Monitor low-stock items

---

## Sample Operations

### Adding a Product (Admin)
```
Product name: Laptop
Category: Electronics
Price: 899.99
Initial quantity: 50
Supplier name: TechSupply Inc
Minimum stock level: 10
```

### Stock IN Operation (Staff)
```
Enter Product ID: 1
Enter quantity to add: 20

✓ Stock added successfully!
  Product: Laptop
  Quantity Added: 20
  Previous Stock: 50
  New Stock: 70
```

### Stock OUT Operation (Staff)
```
Enter Product ID: 1
Enter quantity to remove: 5

✓ Stock removed successfully!
  Product: Laptop
  Quantity Removed: 5
  Total Value: ₹4499.95
  Previous Stock: 70
  New Stock: 65
```

---

## Export Functionality

Transactions can be exported to CSV format:
- File name: `inventory_transactions.csv`
- Includes: Transaction ID, Product Name, Quantity, Type, User, Date
- Accessible from Admin menu (Option 6)

---

## Future Enhancements

- [ ] Password hashing for security
- [ ] Advanced search and filter options
- [ ] Barcode scanning integration
- [ ] Email notifications for low stock
- [ ] Multi-location inventory support
- [ ] Graphical user interface (GUI)
- [ ] Sales analytics and reporting
- [ ] Supplier management module

---
# Inventory Management System - Usage Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Login & Authentication](#login--authentication)
3. [Admin Features](#admin-features)
4. [Staff Features](#staff-features)
5. [Common Operations](#common-operations)
6. [Troubleshooting](#troubleshooting)
7. [Best Practices](#best-practices)

---

## Getting Started

### Prerequisites
- Python 3.6 or higher installed
- Terminal/Command Prompt access
- Basic command-line knowledge

### Installation Steps

1. **Download/Clone the Project**
   ```bash
   git clone <repository-url>
   cd inventory-management-system
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   # or
   python3 --version
   ```

3. **Run the Application**
   ```bash
   python main.py
   # or
   python3 main.py
   ```

4. **First Run**
   - Database `inventory.db` will be created automatically
   - Default admin account is created
   - You'll see the login prompt

---

## Login & Authentication

### Default Credentials

**Admin Account:**
- Username: `admin`
- Password: `admin123`

**Staff Accounts:**
- Created by admin users through the admin menu

### Login Process

1. Run the application
2. Enter username when prompted
3. Enter password when prompted
4. System validates credentials
5. Access granted based on role (Admin/Staff)

### Login Attempts
- Maximum 3 failed login attempts allowed
- After 3 failures, system exits
- Counter resets after successful login

### Example Login Session
```
============================================================
                INVENTORY MANAGEMENT SYSTEM
============================================================

Welcome! Please login to continue.

Username: admin
Password: admin123

✓ Login successful! Welcome, admin (Admin)

Redirecting to Admin menu...
```

---

## Admin Features

### Main Menu Overview
```
==================================================
ADMIN MENU - admin
==================================================
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
==================================================
```

### 1. Add Product

**Steps:**
1. Select option `1` from admin menu
2. Enter product details:
   - Product name (required)
   - Category
   - Price in INR (must be ≥ 0)
   - Initial quantity (must be ≥ 0)
   - Supplier name
   - Minimum stock level (for alerts)

**Example:**
```
--- Add New Product ---
Product name: Laptop
Category: Electronics
Price: 45000
Initial quantity: 50
Supplier name: TechSupply Inc
Minimum stock level: 10

✓ Product added successfully!
  Product ID: 1
  Name: Laptop
  Category: Electronics
  Price: ₹45000.00
  Initial Stock: 50
```

**Validation:**
- Product name cannot be empty
- Price cannot be negative
- Quantity cannot be negative
- Minimum stock level cannot be negative

---

### 2. View All Products

**Purpose:** Display complete inventory list

**Output Format:**
```
====================================================================================================
PRODUCT INVENTORY
====================================================================================================
ID     Name                 Category        Price      Stock    Supplier        Min Stock  
----------------------------------------------------------------------------------------------------
1      Laptop               Electronics     ₹45000.00  50       TechSupply Inc  10         
2      Mouse                Electronics     ₹500.00    200      TechSupply Inc  50         ⚠ LOW
====================================================================================================
Total Products: 2
```

**Features:**
- Shows all product details
- Displays low stock warnings (⚠ LOW)
- Sorted by product ID

---

### 3. Update Product

**Steps:**
1. Select option `3` from admin menu
2. Enter product ID to update
3. Choose which field to update:
   - Product Name
   - Category
   - Price
   - Quantity in Stock
   - Supplier Name
   - Minimum Stock Level
4. Enter new value
5. Confirmation displayed

**Example:**
```
--- Update Product ---
Enter Product ID to update: 1
Updating: Laptop

What would you like to update?
1. Product Name
2. Category
3. Price
4. Quantity in Stock
5. Supplier Name
6. Minimum Stock Level
7. Cancel

Enter choice: 3
Enter new price: 42000
✓ Product updated successfully.
```

**Use Cases:**
- Price adjustments
- Correct data entry errors
- Update supplier information
- Adjust minimum stock levels

---

### 4. Delete Product

**Steps:**
1. Select option `4` from admin menu
2. Enter product ID to delete
3. System shows product name
4. Confirm deletion (type 'yes')
5. Product removed from database

**Example:**
```
--- Delete Product ---
Enter Product ID to delete: 5
Are you sure you want to delete 'Old Product'? (yes/no): yes
✓ Product 'Old Product' deleted successfully.
```

**Warning:**
- This action cannot be undone
- All transaction history for this product remains
- Use with caution

---

### 5. View All Transactions

**Purpose:** Monitor all inventory movements system-wide

**Output Format:**
```
================================================================================
ALL INVENTORY TRANSACTIONS
================================================================================
ID     Product              Qty    Type   User            Date                
--------------------------------------------------------------------------------
3      Laptop               5      OUT    staff1          2026-02-12 10:30:45 
2      Mouse                100    IN     staff1          2026-02-12 09:15:20 
1      Laptop               20     IN     staff2          2026-02-12 08:00:10 
================================================================================
Total Transactions: 3
```

**Information Displayed:**
- Transaction ID
- Product name
- Quantity moved
- Transaction type (IN/OUT)
- User who performed it
- Date and time

---

### 6. Export Transactions to CSV

**Purpose:** Generate reports for external analysis

**Steps:**
1. Select option `6`
2. System generates CSV file
3. File saved as `inventory_transactions.csv`

**Output:**
```
✓ 45 transactions exported to 'inventory_transactions.csv'
```

**CSV Format:**
```csv
Transaction ID,Product Name,Quantity,Transaction Type,User,Date
1,Laptop,20,IN,staff1,2026-02-12 08:00:10
2,Mouse,100,IN,staff1,2026-02-12 09:15:20
3,Laptop,5,OUT,staff1,2026-02-12 10:30:45
```

**Use Cases:**
- Import into Excel/Google Sheets
- Create custom reports
- Data analysis
- Audit purposes

---

### 7. Low Stock Alerts

**Purpose:** Identify products needing restock

**Output Format:**
```
================================================================================
⚠ LOW STOCK ALERTS
================================================================================
ID     Product                   Category        Stock    Min Required
--------------------------------------------------------------------------------
2      Mouse                     Electronics     45       50          
5      Keyboard                  Electronics     8        30          
================================================================================
Total Low Stock Items: 2
```

**When Alerts Trigger:**
- When `current stock ≤ minimum stock level`
- Sorted by current stock (lowest first)

**Action Items:**
- Place orders with suppliers
- Perform stock IN operations
- Adjust minimum stock levels if needed

---

### 8. Inventory Summary Report

**Purpose:** Get quick overview of inventory status

**Output Format:**
```
============================================================
INVENTORY SUMMARY REPORT
============================================================
Total Products: 15
Total Inventory Value: ₹1,250,000.00
Low Stock Items: 3

Transaction Summary:
  IN: 45 transactions, 2,350 total units
  OUT: 38 transactions, 1,890 total units
============================================================
```

**Metrics Provided:**
- Total number of products
- Total value of inventory (price × quantity)
- Count of low stock items
- Transaction statistics

---

### 9. Create Staff User

**Purpose:** Add new staff members to the system

**Steps:**
1. Select option `9`
2. Enter new staff username
3. Enter password
4. Account created with 'Staff' role

**Example:**
```
Enter staff username: john_doe
Enter staff password: secure123
✓ Staff user 'john_doe' created successfully.
```

**Validation:**
- Username must be unique
- Username and password cannot be empty
- Username must not already exist

**Error Example:**
```
Enter staff username: staff1
Enter staff password: pass123
✗ Username 'staff1' already exists. Please choose a different username.
```

---

## Staff Features

### Main Menu Overview
```
==================================================
STAFF MENU - staff1
==================================================
1. View Products
2. Stock IN (Add Stock)
3. Stock OUT (Remove Stock)
4. View My Transactions
5. Low Stock Alerts
6. Logout
==================================================
```

### 1. View Products

**Same as Admin "View All Products"**
- Staff can see complete inventory
- Cannot modify product details
- Read-only access

---

### 2. Stock IN (Add Stock)

**Purpose:** Add inventory when receiving stock

**Steps:**
1. Select option `2`
2. Enter Product ID
3. Enter quantity to add
4. Stock updated, transaction logged

**Example:**
```
Enter Product ID: 1
Enter quantity to add: 25

✓ Stock added successfully!
  Product: Laptop
  Quantity Added: 25
  Previous Stock: 50
  New Stock: 75
```

**Use Cases:**
- Receiving shipments from suppliers
- Returning items to inventory
- Stock adjustments (increase)

**Validation:**
- Product ID must exist
- Quantity must be positive number
- Transaction logged automatically

---

### 3. Stock OUT (Remove Stock)

**Purpose:** Remove inventory for sales or issues

**Steps:**
1. Select option `3`
2. Enter Product ID
3. Enter quantity to remove
4. System checks available stock
5. Stock updated, transaction logged

**Example:**
```
Enter Product ID: 1
Enter quantity to remove: 10

✓ Stock removed successfully!
  Product: Laptop
  Quantity Removed: 10
  Total Value: ₹450,000.00
  Previous Stock: 75
  New Stock: 65
```

**Validation:**
- Product ID must exist
- Quantity must be positive
- Sufficient stock must be available

**Insufficient Stock Example:**
```
Enter Product ID: 2
Enter quantity to remove: 300

✗ Insufficient stock!
  Available: 200
  Requested: 300
```

---

### 4. View My Transactions

**Purpose:** Track personal transaction history

**Output Format:**
```
===========================================================================
MY INVENTORY TRANSACTIONS
===========================================================================
ID     Product              Qty    Type   Date                
---------------------------------------------------------------------------
5      Laptop               10     OUT    2026-02-12 11:45:30 
4      Mouse                50     IN     2026-02-12 10:20:15 
3      Laptop               25     IN     2026-02-12 09:05:00 
===========================================================================
Total Transactions: 3
```

**Features:**
- Shows only transactions by logged-in user
- Sorted by date (newest first)
- Useful for personal audit trail

---

### 5. Low Stock Alerts

**Same as Admin "Low Stock Alerts"**
- Staff can monitor low stock items
- Helps coordinate with admin for reordering
- No action required, informational only

---

## Common Operations

### Daily Opening Procedure
1. Login to system
2. Check low stock alerts
3. View inventory status
4. Ready to process transactions

### Receiving Stock Shipment
1. Login as staff
2. View products (confirm IDs)
3. For each item received:
   - Select "Stock IN"
   - Enter product ID
   - Enter received quantity
4. Verify new stock levels

### Processing Sales/Issues
1. Login as staff
2. For each item sold/issued:
   - Select "Stock OUT"
   - Enter product ID
   - Enter quantity
3. Review total value
4. Verify stock reduction

### Weekly Reporting
1. Login as admin
2. View inventory summary
3. Export transactions to CSV
4. Analyze in spreadsheet software
5. Identify trends and issues

### Monthly Maintenance
1. Review low stock alerts
2. Update minimum stock levels if needed
3. Remove discontinued products
4. Update prices if necessary
5. Create backup of database

---

## Troubleshooting

### Login Issues

**Problem:** Cannot login with correct credentials
```
✗ Invalid credentials. Please try again.
```
**Solutions:**
- Check for typos
- Verify caps lock is off
- Ensure username exists
- Contact admin if password forgotten

---

**Problem:** Maximum login attempts reached
```
Maximum login attempts reached. Exiting system.
```
**Solutions:**
- Restart the application
- Get help from admin
- Check if account is correct

---

### Transaction Errors

**Problem:** Product ID not found
```
✗ Invalid product ID: 999
```
**Solutions:**
- View products list first
- Use correct product ID
- Product may have been deleted

---

**Problem:** Cannot remove stock
```
✗ Insufficient stock!
  Available: 5
  Requested: 10
```
**Solutions:**
- Check available quantity first
- Reduce quantity requested
- Perform Stock IN if receiving more

---

**Problem:** Invalid input
```
✗ Invalid input. Please enter valid numbers.
```
**Solutions:**
- Enter numbers only for ID and quantity
- No letters or special characters
- No decimal points for quantity

---

### Database Issues

**Problem:** Database locked or corrupted
**Solutions:**
1. Close all instances of the application
2. Restart the program
3. If persists, restore from backup
4. As last resort, delete `inventory.db` and restart (loses all data)

---

**Problem:** Permission denied
**Solutions:**
1. Check file permissions
2. Run from writable directory
3. Close database viewers (SQLite Browser, etc.)

---

### Export Issues

**Problem:** CSV file not created
**Solutions:**
1. Check write permissions in directory
2. Close CSV file if open in Excel
3. Check disk space

---

## Best Practices

### For Admins

1. **Regular Backups**
   - Backup `inventory.db` weekly
   - Keep multiple backup copies
   - Test restore procedure

2. **User Management**
   - Create unique staff accounts
   - Don't share admin password
   - Review user activity periodically

3. **Data Integrity**
   - Review transactions regularly
   - Verify stock counts periodically
   - Update product information promptly

4. **Security**
   - Change default admin password
   - Use strong passwords for staff
   - Limit admin access

5. **Reporting**
   - Export data monthly
   - Analyze trends
   - Adjust minimum stock levels based on usage

---

### For Staff

1. **Accuracy**
   - Double-check product IDs
   - Verify quantities before confirming
   - Review transaction summary

2. **Timeliness**
   - Log transactions immediately
   - Don't batch transactions from memory
   - Update stock as items move

3. **Communication**
   - Report low stock to admin
   - Note any discrepancies
   - Ask questions when unsure

4. **Organization**
   - View products before transactions
   - Use consistent naming
   - Keep workspace organized

---

### General Guidelines

1. **Data Entry**
   - Be consistent with naming
   - Use proper capitalization
   - Include relevant details

2. **Stock Management**
   - Count carefully
   - Investigate discrepancies
   - Perform regular audits

3. **System Usage**
   - Logout when finished
   - Don't leave system unattended
   - Report issues promptly

4. **Documentation**
   - Keep this guide accessible
   - Note custom procedures
   - Document special cases

---

## Keyboard Shortcuts & Tips

### Navigation
- Type number + Enter to select menu option
- Type 'yes' or 'no' for confirmations
- Menu navigation is sequential

### Quick Operations
- View products before any transaction
- Keep product IDs reference handy
- Use CSV export for bulk analysis

### Efficiency Tips
1. Learn common product IDs
2. Keep supplier contact info separate
3. Batch similar transactions together
4. Review before confirming

---

## Support & Help

### Getting Help
1. Review this usage guide
2. Check troubleshooting section
3. Review database schema documentation
4. Contact system administrator

### Reporting Issues
When reporting problems, include:
- Error message (exact text)
- Steps to reproduce
- Expected vs actual behavior
- Your user role (Admin/Staff)

---

## Appendix: Quick Reference

### Admin Menu Options
| # | Feature | Purpose |
|---|---------|---------|
| 1 | Add Product | Create new inventory item |
| 2 | View Products | See all inventory |
| 3 | Update Product | Modify product details |
| 4 | Delete Product | Remove product |
| 5 | View Transactions | See all activity |
| 6 | Export CSV | Generate report file |
| 7 | Low Stock Alerts | Check reorder needs |
| 8 | Summary Report | Overview dashboard |
| 9 | Create Staff | Add user account |
| 10 | Logout | Exit session |

### Staff Menu Options
| # | Feature | Purpose |
|---|---------|---------|
| 1 | View Products | See inventory |
| 2 | Stock IN | Add stock |
| 3 | Stock OUT | Remove stock |
| 4 | My Transactions | Personal history |
| 5 | Low Stock Alerts | Check alerts |
| 6 | Logout | Exit session |

---

**Document Version:** 1.0  
**Last Updated:** February 2026  
**For System Version:** 2.0
# Inventory Management System - Complete Project Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features & Functionality](#features--functionality)
3. [System Requirements](#system-requirements)
4. [Installation & Setup](#installation--setup)
5. [Architecture & Design](#architecture--design)
6. [Database Schema](#database-schema)
7. [User Roles & Permissions](#user-roles--permissions)
8. [Screenshots & Demo](#screenshots--demo)
9. [Testing & Validation](#testing--validation)
10. [Future Enhancements](#future-enhancements)
11. [Contributors](#contributors)
12. [License](#license)

---

## Project Overview

### Description
The **Inventory Management System** is a command-line application built with Python and SQLite3 that enables businesses to efficiently manage their product inventory, track stock movements, and generate reports. The system implements role-based access control with separate functionalities for administrators and staff members.

### Objectives
- Provide a simple, efficient inventory tracking solution
- Implement secure role-based access control
- Enable real-time stock monitoring and alerts
- Generate comprehensive transaction reports
- Maintain accurate audit trails for all operations

### Project Type
**Academic/Learning Project** - Command-Line Interface (CLI) Application

### Technologies Used
| Technology | Purpose | Version |
|------------|---------|---------|
| Python | Core programming language | 3.6+ |
| SQLite3 | Embedded database | 3.x |
| CSV Module | Data export functionality | Built-in |

### Development Period
February 2026

---

## Features & Functionality

### Admin Features
1. **Product Management**
   - Add new products with detailed information
   - View complete product inventory
   - Update product details (name, price, category, etc.)
   - Delete products from inventory

2. **Transaction Management**
   - View all system transactions
   - Export transaction history to CSV
   - Track stock movements (IN/OUT)

3. **Reporting & Analytics**
   - Low stock alerts and monitoring
   - Inventory summary reports
   - Total inventory valuation

4. **User Management**
   - Create staff user accounts
   - Manage access controls

### Staff Features
1. **Inventory Operations**
   - View product catalog
   - Stock IN (receive inventory)
   - Stock OUT (issue/sell items)

2. **Personal Tracking**
   - View personal transaction history
   - Monitor low stock items

3. **Stock Management**
   - Real-time stock validation
   - Automatic transaction logging

### Security Features
- Role-based access control (Admin/Staff)
- Login authentication
- Maximum login attempt limits
- SQL injection prevention (parameterized queries)
- Data validation and constraints

### Reporting Features
- CSV export for external analysis
- Comprehensive transaction logging
- Inventory valuation reports
- Low stock alerts
- User activity tracking

---

## System Requirements

### Hardware Requirements
- **Processor:** Any modern CPU (1 GHz or higher)
- **RAM:** Minimum 512 MB
- **Storage:** 50 MB free space (for application and data)
- **Display:** Any terminal/command prompt interface

### Software Requirements
- **Operating System:** 
  - Windows 7/8/10/11
  - macOS 10.12+
  - Linux (any modern distribution)
  
- **Python:** Version 3.6 or higher
- **Terminal/Command Prompt:** Standard system terminal

### Dependencies
**None** - Uses only Python standard library modules:
- `sqlite3` - Database operations
- `csv` - Data export
- `datetime` - Timestamp handling

---

## Installation & Setup

### Step 1: Install Python

**Windows:**
1. Download Python from [python.org](https://python.org)
2. Run installer
3. Check "Add Python to PATH"
4. Complete installation

**macOS:**
```bash
# Using Homebrew
brew install python3
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3

# Fedora
sudo dnf install python3
```

### Step 2: Verify Installation
```bash
python --version
# or
python3 --version
```

Expected output: `Python 3.x.x`

### Step 3: Download Project

**Option A: Git Clone**
```bash
git clone https://github.com/yourusername/inventory-management-system.git
cd inventory-management-system
```

**Option B: Direct Download**
1. Download ZIP from GitHub
2. Extract to desired location
3. Open terminal in project directory

### Step 4: Run Application
```bash
python main.py
# or
python3 main.py
```

### Step 5: First Login
- **Username:** `admin`
- **Password:** `admin123`

---

## Architecture & Design

### Project Structure
```
inventory-management-system/
│
├── main.py                      # Application entry point
├── database.py                  # Database setup and connection
├── auth.py                      # Authentication & user management
├── products.py                  # Product CRUD & menu systems
├── transactions.py              # Stock IN/OUT operations
├── reports.py                   # Reporting & analytics
│
├── inventory.db                 # SQLite database (auto-created)
├── inventory_transactions.csv   # Export file (auto-generated)
│
├── README.md                    # Project overview
├── REQUIREMENTS.txt             # System requirements
├── DATABASE_SCHEMA.md           # Database documentation
├── USAGE_GUIDE.md               # User manual
├── PROJECT_DOCUMENTATION.md     # This file
└── BUG_REPORT.md               # Issue tracking & fixes

```

### Module Descriptions

#### 1. main.py
- **Purpose:** Application entry point and flow control
- **Responsibilities:**
  - Initialize database
  - Handle login loop
  - Route to appropriate menu (Admin/Staff)
  - Manage session lifecycle

#### 2. database.py
- **Purpose:** Database operations and schema management
- **Responsibilities:**
  - Create database connection
  - Initialize tables
  - Define schema with constraints
  - Set up foreign keys

#### 3. auth.py
- **Purpose:** Authentication and authorization
- **Responsibilities:**
  - User login validation
  - Create default admin account
  - Create staff accounts
  - Handle login attempts

#### 4. products.py
- **Purpose:** Product management and menu systems
- **Responsibilities:**
  - Admin menu interface
  - Staff menu interface
  - Product CRUD operations
  - User interaction handling

#### 5. transactions.py
- **Purpose:** Inventory transaction operations
- **Responsibilities:**
  - Stock IN functionality
  - Stock OUT functionality
  - Quantity validation
  - Transaction logging

#### 6. reports.py
- **Purpose:** Reporting and analytics
- **Responsibilities:**
  - View all transactions
  - View user transactions
  - Export to CSV
  - Low stock alerts
  - Summary reports

### Data Flow Diagram

```
┌─────────┐
│  User   │
└────┬────┘
     │
     ▼
┌─────────────┐
│   main.py   │  ◄─── Entry Point
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   auth.py   │  ◄─── Authentication
└──────┬──────┘
       │
       ├──► Admin? ──┐
       │             │
       └──► Staff? ──┤
                     │
       ┌─────────────┴──────────────┐
       ▼                            ▼
┌──────────────┐            ┌──────────────┐
│ products.py  │            │ products.py  │
│ (Admin Menu) │            │ (Staff Menu) │
└──────┬───────┘            └──────┬───────┘
       │                           │
       ├───► database.py ◄─────────┤
       │                           │
       ├───► transactions.py ◄─────┤
       │                           │
       └───► reports.py ◄──────────┘
              │
              ▼
       ┌──────────────┐
       │ inventory.db │  ◄─── SQLite Database
       └──────────────┘
```

### Design Patterns Used

1. **Modular Design**
   - Separation of concerns
   - Each module has specific responsibility
   - Easy to maintain and extend

2. **Database Connection Pattern**
   - Centralized connection management
   - Consistent database access
   - Proper resource cleanup

3. **Menu-Driven Interface**
   - User-friendly navigation
   - Clear option presentation
   - Input validation

4. **Transaction Pattern**
   - Atomic operations
   - Rollback on errors
   - Data consistency

---

## Database Schema

### Entity Relationship Diagram

```
┌──────────────────┐
│      USERS       │
├──────────────────┤
│ user_id (PK)     │───┐
│ username (UNIQUE)│   │
│ password         │   │
│ role             │   │
└──────────────────┘   │
                       │
                       │ Foreign Key
                       │
┌──────────────────┐   │   ┌─────────────────────────────┐
│    PRODUCTS      │   │   │  INVENTORY_TRANSACTIONS     │
├──────────────────┤   │   ├─────────────────────────────┤
│ product_id (PK)  │───┼──→│ transaction_id (PK)         │
│ product_name     │   │   │ product_id (FK)             │
│ category         │   │   │ quantity                    │
│ price            │   │   │ transaction_type (IN/OUT)   │
│ quantity_in_stock│   │   │ user_id (FK)                │←─┘
│ supplier_name    │   │   │ date (TIMESTAMP)            │
│ minimum_stock    │   │   └─────────────────────────────┘
└──────────────────┘   │
```

### Table Specifications

#### USERS Table
```sql
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('Admin', 'Staff'))
);
```

#### PRODUCTS Table
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

#### INVENTORY_TRANSACTIONS Table
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

**For detailed database documentation, see:** [DATABASE_SCHEMA.md](DATABASE_SCHEMA.md)

---

## User Roles & Permissions

### Role Matrix

| Feature | Admin | Staff |
|---------|-------|-------|
| **Product Management** |
| Add Product | Yes | No |
| View Products | Yes | Yes |
| Update Product | Yes | No |
| Delete Product | Yes | No |
| **Stock Operations** |
| Stock IN | Yes | Yes |
| Stock OUT | Yes | Yes |
| **Transactions** |
| View All Transactions | Yes | No |
| View My Transactions | Yes | Yes |
| Export to CSV | Yes | No |
| **Reports** |
| Low Stock Alerts | Yes | Yes |
| Inventory Summary | Yes | No |
| **User Management** |
| Create Staff Users | Yes | No |

### Role Descriptions

**Admin (Administrator)**
- Full system access
- Manages products and users
- Views all system activity
- Generates reports
- Strategic oversight

**Staff (Staff Member)**
- Operational access
- Performs daily stock operations
- Views personal activity
- Limited reporting access
- Tactical execution

---

## Screenshots & Demo

### Login Screen
```
============================================================
                INVENTORY MANAGEMENT SYSTEM
============================================================

Welcome! Please login to continue.

Username: admin
Password: ********

✓ Login successful! Welcome, admin (Admin)
```

### Admin Menu
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
Enter your choice: 
```

### Product List View
```
====================================================================================================
PRODUCT INVENTORY
====================================================================================================
ID     Name                 Category        Price      Stock    Supplier        Min Stock  
----------------------------------------------------------------------------------------------------
1      Laptop               Electronics     ₹45000.00  50       TechSupply Inc  10         
2      Mouse                Electronics     ₹500.00    200      TechSupply Inc  50         
3      Keyboard             Electronics     ₹1500.00   95       TechSupply Inc  30         
4      Monitor              Electronics     ₹12000.00  25       DisplayCo       5          
====================================================================================================
Total Products: 4
```

### Stock IN Operation
```
Enter Product ID: 1
Enter quantity to add: 25

✓ Stock added successfully!
  Product: Laptop
  Quantity Added: 25
  Previous Stock: 50
  New Stock: 75
```

### Low Stock Alert
```
================================================================================
⚠ LOW STOCK ALERTS
================================================================================
ID     Product                   Category        Stock    Min Required
--------------------------------------------------------------------------------
5      Keyboard                  Electronics     8        30          
2      Mouse                     Electronics     45       50          
================================================================================
Total Low Stock Items: 2
```

### Inventory Summary Report
```
============================================================
INVENTORY SUMMARY REPORT
============================================================
Total Products: 15
Total Inventory Value: ₹1,250,000.00
Low Stock Items: 2

Transaction Summary:
  IN: 45 transactions, 2,350 total units
  OUT: 38 transactions, 1,890 total units
============================================================
```

### How to Create Demo Video

**Recommended Tools:**
- **Windows:** OBS Studio, Xbox Game Bar
- **macOS:** QuickTime Player, Screen Recording
- **Linux:** SimpleScreenRecorder, OBS Studio

**Demo Script (5-7 minutes):**

1. **Introduction (30 sec)**
   - Project name and purpose
   - Show project structure

2. **Installation (1 min)**
   - Show Python version check
   - Run application
   - First-time setup

3. **Admin Features Demo (3 min)**
   - Login as admin
   - Add a product
   - View products
   - Check low stock alerts
   - View all transactions
   - Export to CSV
   - Create staff user

4. **Staff Features Demo (2 min)**
   - Logout and login as staff
   - Perform Stock IN
   - Perform Stock OUT
   - View personal transactions

5. **Closing (30 sec)**
   - Show generated files
   - Summary of features
   - Thank you

**Video Format:**
- **Resolution:** 1920x1080 (1080p) or 1280x720 (720p)
- **Length:** 5-7 minutes
- **Format:** MP4, AVI, or MOV
- **Upload:** YouTube (unlisted), Google Drive, or institution platform

---

## Testing & Validation

### Test Cases Executed

#### Authentication Tests
| Test Case | Expected Result | Status |
|-----------|----------------|--------|
| Admin login with correct credentials | Login successful | Pass |
| Staff login with correct credentials | Login successful | Pass |
| Login with invalid credentials | Login denied | Pass |
| Maximum login attempts (3) | System exit | Pass |
| Create duplicate staff username | Error message | Pass |

#### Product Management Tests
| Test Case | Expected Result | Status |
|-----------|----------------|--------|
| Add product with valid data | Product created | Pass |
| Add product with negative price | Error message | Pass |
| Add product with empty name | Error message | Pass |
| Update product details | Changes saved | Pass |
| Delete product with confirmation | Product removed | Pass |
| View all products | Complete list displayed | Pass |

#### Stock Operation Tests
| Test Case | Expected Result | Status |
|-----------|----------------|--------|
| Stock IN with valid quantity | Stock increased | Pass |
| Stock IN with negative quantity | Error message | Pass |
| Stock OUT with sufficient stock | Stock decreased | Pass |
| Stock OUT exceeding available | Error message | Pass |
| Transaction logged correctly | Record in database | Pass |

#### Reporting Tests
| Test Case | Expected Result | Status |
|-----------|----------------|--------|
| View all transactions | Complete history | Pass |
| View user transactions only | Filtered list | Pass |
| Export to CSV | File created | Pass |
| Low stock alerts | Correct items shown | Pass |
| Inventory summary | Accurate calculations | Pass |

### Validation Checks

- **Input Validation**
- Non-negative prices
- Non-negative quantities
- Required fields not empty
- Valid data types

- **Business Logic Validation**
- Sufficient stock for OUT operations
- Unique usernames
- Valid product references
- Proper role restrictions

- **Database Integrity**
- Foreign key constraints
- Check constraints
- Primary key uniqueness
- NOT NULL enforcement


---

## Future Enhancements

### Short-term Improvements
1. **Security**
   - Password hashing (bcrypt/argon2)
   - Password strength requirements
   - Session timeout implementation
   - Audit log for admin actions

2. **User Experience**
   - Search/filter products
   - Pagination for large lists
   - Batch operations
   - Confirmation for all destructive actions

3. **Reporting**
   - Date range filters
   - Product-wise sales reports
   - User activity reports
   - Custom report builder

### Medium-term Enhancements
1. **Features**
   - Product categories as separate table
   - Supplier management module
   - Barcode/SKU support
   - Multi-location inventory
   - Email notifications for low stock

2. **Technical**
   - Database migrations
   - Automated backups
   - Configuration file (config.ini)
   - Logging framework
   - Unit tests

### Long-term Vision
1. **Architecture**
   - Web-based interface (Flask/Django)
   - REST API
   - Mobile application
   - Real-time dashboard
   - Multi-user concurrent access

2. **Advanced Features**
   - Predictive stock alerts (ML)
   - Sales analytics and trends
   - Integration with accounting software
   - Purchase order management
   - Customer management

---

## Contributors

**Developer:** Adithya Krihsnan 
**Role:** Aspiring Python Developer
**GitHub:** https://github.com/adithyank1998

---

## License

This project is developed for academic purposes.

**Usage Terms:**
- Free to use for learning
- Attribution required for modifications
- Not for commercial use without permission
- No warranty provided

---

## Support & Contact

### Getting Help
1. Review [USAGE_GUIDE.md](USAGE_GUIDE.md)
2. Check [DATABASE_SCHEMA.md](DATABASE_SCHEMA.md)
3. Contact project maintainer

### Reporting Issues
Please include:
- Python version
- Operating system
- Error messages (complete text)
- Steps to reproduce
- Expected vs actual behavior

### Feedback
We welcome feedback on:
- Feature suggestions
- Bug reports
- Documentation improvements
- User experience
- Code quality

---

## Additional Resources

### Documentation Files
- `README.md` - Quick start guide
- `USAGE_GUIDE.md` - Detailed user manual
- `DATABASE_SCHEMA.md` - Database documentation
- `REQUIREMENTS.txt` - System requirements
- `PROJECT_DOCUMENTATION.md` - This file

### External Resources
- [Python Documentation](https://docs.python.org/3/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Git Documentation](https://git-scm.com/doc)

---

## Learning Outcomes

This project demonstrates:
1. **Python Programming**
   - Functions and modules
   - File I/O operations
   - Error handling
   - Data structures

2. **Database Management**
   - SQL queries (CRUD)
   - Database design
   - Relationships and constraints
   - Data integrity

3. **Software Engineering**
   - Modular design
   - Version control (Git)
   - Documentation
   - Testing and debugging

4. **Problem Solving**
   - Requirements analysis
   - System design
   - Implementation
   - Validation

---

**Document Version:** 1.0  
**Last Updated:** February 12, 2026  
**Project Version:** 2.0  

---

**END OF PROJECT DOCUMENTATION**
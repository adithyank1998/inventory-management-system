from database import create_tables
from auth import create_default_admin, login
from products import admin_menu, staff_menu


def main():
    """Main entry point for the Inventory Management System"""
    
    # Initialize database
    create_tables()
    create_default_admin()

    print("\n" + "="*60)
    print(" "*15 + "INVENTORY MANAGEMENT SYSTEM")
    print("="*60)
    print("\nWelcome! Please login to continue.\n")

    # Login loop
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        user = login()

        if user:
            user_id, username, role = user

            print(f"\nRedirecting to {role} menu...")
            
            if role == "Admin":
                admin_menu(user_id, username)
            else:
                staff_menu(user_id, username)
            
            # After logout, ask if user wants to login again
            print("\n" + "="*60)
            retry = input("Do you want to login again? (yes/no): ").strip().lower()
            if retry != "yes":
                print("\nThank you for using the Inventory Management System!")
                print("Goodbye!")
                break
            else:
                print("\n" + "="*60)
                attempts = 0  # Reset attempts for new login session
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Attempts remaining: {remaining}\n")
            else:
                print("\nMaximum login attempts reached. Exiting system.")
                break


if __name__ == "__main__":
    main()
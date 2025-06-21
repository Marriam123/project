# main.py
from restaurant_main import admin_portal, client_portal

def main():
    while True:
        print("\n--- Welcome to Restaurant Management System ---")
        print("1. Admin Portal")
        print("2. Client Portal")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            admin_portal()
        elif choice == '2':
            client_portal()
        elif choice == '3':
            print("Thank you! Exiting.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()

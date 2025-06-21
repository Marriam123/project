from getpass import getpass
from db_module import insert_user, validate_login


def signup(role):
    username = input("Choose a username: ").strip()
    password = getpass("Choose a password: ").strip()
    insert_user(role, username, password)
    print(f"{role} signup successful. You can now log in.")
    return True

def login(role):
    username = input("Username: ").strip()
    password = getpass("Password: ").strip()
    if validate_login(role, username, password):
        uName= username.upper()
        print(f"{uName}'s login successful.")
        print(f"Welcome {uName}!")
        
        return True
    else:
        print("Invalid credentials.")
        return False

def authenticate(role):
    print(f"\n--- {role} Authentication ---")
    while True:
        print("1. Login")
        if role.lower() != "admin":
            print("2. Signup")
        print("3. Cancel")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            return login(role)
        elif choice == '2' and role.lower() != "admin":
            signup(role)
        elif choice == '3':
            return False
        else:
            print("Invalid input.")



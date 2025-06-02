from getpass import getpass

def get_filename(role):
    return "admin.txt" if role.lower() == "admin" else "users.txt"

def load_users(role):
    filename = get_filename(role)
    try:
        with open(filename, "r") as f:
            users = {}
            for line in f:
                line = line.strip().replace('\r', '')  # Handle CR characters
                if ',' in line:
                    username, password = map(str.strip, line.split(",", 1))
                    users[username] = password
            return users
    except FileNotFoundError:
        return {}

def save_user(role, username, password):
    filename = get_filename(role)
    with open(filename, "a") as f:
        f.write(f"{username},{password}\n")

def signup(role):
    users = load_users(role)
    username = input("Choose a username: ").strip()
    if username in users:
        print("Username already exists.")
        return False
    password = getpass("Choose a password: ").strip()
    save_user(role, username, password)
    print(f"{role} signup successful. You can now log in.")
    return True

def login(role):
    users = load_users(role)
    username = input("Username: ").strip()
    password = getpass("Password: ").strip()
    if users.get(username) == password:
        print(f"{role} login successful.")
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

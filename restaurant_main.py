# restaurant_main.py
from order import take_order, show_summary, get_next_order_id
from billing import Order, billing_summary
from notification import NotificationManager
import random

menu_items = {
    1: ("Chicken Wings", 300),
    2: ("Fries", 150),
    3: ("Soup", 200),
    4: ("Biryani", 250),
    5: ("Chicken Karahi", 800),
    6: ("Naan", 30),
    7: ("BBQ Platter", 1200),
    8: ("Kheer", 120),
    9: ("Gulab Jamun", 100),
    10: ("Ice Cream", 150),
    11: ("Soft Drink", 50),
    12: ("Lassi", 100),
    13: ("Tea", 40),
    14: ("Coffee", 70)
}

orders_db = []

def show_menu():
    print("\n            OUR MENU")
    for item_id in sorted(menu_items):
        name, price = menu_items[item_id]
        print(f"{item_id}. {name} - Rs. {price}")

def admin_portal():
    def load_orders_from_file():
        try:
            with open("bills.txt", "r") as f:
                content = f.read().strip()
                return content.split("\n\n") if content else []
        except FileNotFoundError:
            return []

    def save_orders_to_file(all_orders):
        with open("bills.txt", "w") as f:
            f.write("\n\n".join(all_orders))

    while True:
        print("\n--- Admin Portal ---")
        print("1. Add Item to Menu")
        print("2. Delete Item from Menu")
        print("3. View All Orders")
        print("4. Delete an Order")
        print("5. View Sales Analytics")
        print("6. Return to Main Menu")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            price = int(input("Enter item price: "))
            item_id = max(menu_items.keys()) + 1
            menu_items[item_id] = (name, price)
            print(f"Added {name} with ID {item_id}.")

        elif choice == '2':
            item_id = int(input("Enter item ID to delete: "))
            if item_id in menu_items:
                del menu_items[item_id]
                print("Item deleted.")
            else:
                print("Invalid item ID.")

        elif choice == '3':
            orders = load_orders_from_file()
            if not orders:
                print("No orders found in file.")
            else:
                for i, order in enumerate(orders, 1):
                    print(f"\nOrder #{i}\n{order}")

        elif choice == '4':
            orders = load_orders_from_file()
            if not orders:
                print("No orders to delete.")
            else:
                for i, order in enumerate(orders, 1):
                    print(f"\nOrder #{i}\n{order}")
                try:
                    idx = int(input("Enter order number to delete: ")) - 1
                    if 0 <= idx < len(orders):
                        del orders[idx]
                        save_orders_to_file(orders)
                        print("Order deleted successfully.")
                    else:
                        print("Invalid order number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == '5':
            orders = load_orders_from_file()
            total_sales = 0.0
            for order in orders:
                lines = order.splitlines()
                for line in lines:
                    if "Total Payable:" in line:
                        try:
                            amount = float(line.split("Total Payable: Rs.")[1].strip())
                            total_sales += amount
                        except (IndexError, ValueError):
                            pass
            print(f"\nTotal Sales: Rs. {total_sales:.2f}")

        elif choice == '6':
            break
        else:
            print("Invalid input.")

def client_portal():
    while True:
        print("\n--- Client Portal ---")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_menu()
        elif choice == '2':
            order_list = take_order(menu_items)
            show_summary(order_list, menu_items)
            orders = []

            for item_no, qty in order_list:
                if item_no in menu_items:
                    name, price = menu_items[item_no]
                    orders.append(Order(name, qty, price))

            order_id = get_next_order_id()
            email = input("Enter your email address for order confirmation: ")
            phone = input("Enter your WhatsApp number (with country code): ")
            billing_summary(orders, email, phone, order_id)

            orders_db.append(orders)

            notifier = NotificationManager(email, phone)
            notifier.send_email(order_id)
            notifier.send_whatsapp(order_id)

        elif choice == '3':
            break
        else:
            print("Invalid input.")



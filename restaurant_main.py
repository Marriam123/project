# restaurant_main.py
from order import take_order, show_summary, get_next_order_id
from billing import Order,billing_summary
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
    while True:
        print("\n--- Admin Portal ---")
        print("1. Add Item to Menu")
        print("2. Delete Item from Menu")
        print("3. Update Item Price")
        print("4. View All Orders")
        print("5. Delete an Order")
        print("6. View Sales Analytics")
        print("7. Return to Main Menu")

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
            item_id = int(input("Enter item ID to update: "))
            if item_id in menu_items:
                new_price = int(input("Enter new price: "))
                name = menu_items[item_id][0]
                menu_items[item_id] = (name, new_price)
                print("Price updated.")
            else:
                print("Invalid item ID.")
        elif choice == '4':
            if not orders_db:
                print("No orders yet.")
            else:
                for i, order_set in enumerate(orders_db, 1):
                    print(f"\nOrder #{i}")
                    for order in order_set:
                        print(order)
        elif choice == '5':
            idx = int(input("Enter order number to delete: ")) - 1
            if 0 <= idx < len(orders_db):
                del orders_db[idx]
                print("Order deleted.")
            else:
                print("Invalid order number.")
        elif choice == '6':
            total_sales = sum(sum(order.total for order in order_set) for order_set in orders_db)
            print(f"Total Sales: Rs. {total_sales:.2f}")
        elif choice == '7':
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
            show_summary(order_list,menu_items)
            orders = []

            for item_no, qty in order_list:
                if item_no in menu_items:
                    name, price = menu_items[item_no]
                    orders.append(Order(name, qty, price))
            order_id = get_next_order_id()



            email = input("Enter your email address for order confirmation: ")
            phone = input("Enter your WhatsApp number (with country code): ")
            billing_summary(orders, email, phone,order_id)

            orders_db.append(orders)

            

            notifier = NotificationManager(email, phone)
            notifier.send_email(order_id)
            notifier.send_whatsapp(order_id)

        elif choice == '3':
            break
        else:
            print("Invalid input.")

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

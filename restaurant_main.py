from order import take_order, show_summary
from billing import Order, billing_summary, calculate_final_price
from notification import NotificationManager
from auth_system import authenticate
from db_module import (
    connect_db, save_order, fetch_orders, get_user_id, fetch_menu_items,
    add_menu_item, delete_menu_item, delete_order_from_db
)

def show_menu():
    menu_items = fetch_menu_items()  # Fetch menu items from the database
    print("\n            OUR MENU")
    for item in menu_items:
        print(f"{item['id']}. {item['name']} - Rs. {item['price']}")
    return menu_items

def admin_portal():
    if not authenticate("Admin"):
        print("Authentication failed. Returning to main menu.")
        return

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
            try:
                price = float(input("Enter item price: "))
            except ValueError:
                print("Invalid price input.")
                continue
            add_menu_item(name, price)
            print(f"Added {name} to the menu.")

        elif choice == '2':
            menu_items = fetch_menu_items()
            if not menu_items:
                print("No menu items to delete.")
                continue
            print("Menu Items:")
            for item in menu_items:
                print(f"{item['id']}. {item['name']} - Rs. {item['price']}")
            try:
                item_id = int(input("Enter item ID to delete: "))
            except ValueError:
                print("Invalid input.")
                continue
            delete_menu_item(item_id)
            print("Item deleted if existed.")

        elif choice == '3':
            orders = fetch_orders()
            if not orders:
                print("No orders found.")
            else:
                for order in orders:
                    print(f"Order ID: {order['id']}")
                    print(f"Customer Name: {order['name']}")
                    print(f"Phone: {order['phone']}")
                    print(f"Email: {order['email']}")
                    print(f"Items: {order['order_summary']}")
                    print(f"Total: Rs. {order['total_price']}")
                    print(f"Order Time: {order.get('order_time', 'N/A')}")
                    print("-" * 30)

        elif choice == '4':
            orders = fetch_orders()
            if not orders:
                print("No orders to delete.")
                continue
            for order in orders:
                print(f"Order ID: {order['id']} | Total: Rs. {order['total_price']}")
            try:
                order_id = int(input("Enter Order ID to delete: "))
                delete_order_from_db(order_id)
                print("Order deleted.")
            except ValueError:
                print("Invalid input.")

        elif choice == '5':
            orders = fetch_orders()
            total_sales = sum(order['total_price'] for order in orders)
            print(f"\nTotal Sales: Rs. {total_sales:.2f}")

        elif choice == '6':
            break

        else:
            print("Invalid input.")

def client_portal():
    if not authenticate("Client"):
        print("Authentication failed. Returning to main menu.")
        return

    name = input("Enter your name (used during signup): ").strip()
    user_id = get_user_id(name)
    if not user_id:
        print("User not found. Please ensure the correct name is used.")
        return

    while True:
        print("\n--- Client Portal ---")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_menu()

        elif choice == '2':
            menu_items = fetch_menu_items()
            order_list = take_order({item['id']: (item['name'], item['price']) for item in menu_items})
            show_summary(order_list, {item['id']: (item['name'], item['price']) for item in menu_items})

            orders = []
            for item_no, qty in order_list:
                item = next((item for item in menu_items if item['id'] == item_no), None)
                if item:
                    orders.append(Order(item['name'], qty, item['price']))

            phone = input("Enter your phone number: ")
            email = input("Enter your email: ")

            order_summary = ", ".join([f"{o.quantity}x {o.item_name}" for o in orders])

            final_price, discount, tax = calculate_final_price(orders)

            order_id = save_order(user_id, name, phone, email, order_summary, final_price)

            if order_id:
                billing_summary(orders, email, phone, order_id)
                notification = NotificationManager(email, phone)
                notification.send_email(order_id)
                notification.send_whatsapp(order_id)
                print(f"Order placed successfully! Your Order ID is: {order_id}")
            else:
                print("Failed to place order. Please try again.")

        elif choice == '3':
            break
        else:
            print("Invalid input.")

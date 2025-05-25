from order import take_order, show_summary
from billing import Order, billing_summary, add_bills
from notification import NotificationManager  
import random 

# Function to display the restaurant menu
def show_menu(): 
    print("    \n            OUR MENU\n")      # starters section
    print("Starters:")
    print("1. Chicken Wings - Rs. 300")
    print("2. Fries - Rs. 150")
    print("3. Soup - Rs. 200")
    print("Main Course:")                       # main course section
    print("4. Biryani - Rs. 250")
    print("5. Chicken Karahi - Rs. 800")
    print("6. Naan - Rs. 30")
    print("7. BBQ Platter - Rs. 1200")
    print("Desserts:")                          # desserts section
    print("8. Kheer - Rs. 120")
    print("9. Gulab Jamun - Rs. 100")
    print("10. Ice Cream - Rs. 150")
    print("Beverages:")                         # beverages section
    print("11. Soft Drink - Rs. 50")
    print("12. Lassi - Rs. 100")
    print("13. Tea - Rs. 40")
    print("14. Coffee - Rs. 70")

# Dictionary to hold menu items
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

while True:
    print("\nWelcome to Restaurant Management System")
    print("    1. View Menu")
    print("    2. Make the order and View Order Summary")
    print("    3. Exit")
    choice = input("Choose an option (1, 2 or 3): ")
    
    if choice == '1':
        show_menu()

    elif choice == '2':
        order_list = take_order()
        show_summary(order_list)
        
        orders = []
        for item_no, qty in order_list:
            if item_no in menu_items:
                name, price = menu_items[item_no]
                orders.append(Order(name, qty, price))

        billing_summary(orders)

        #to Send Notifications
        order_id = random.randint(1000, 9999)
        customer_email = "customer@example.com"
        customer_phone = "+1234567890"
        notifier = NotificationManager(customer_email, customer_phone)
        notifier.send_email(order_id)
        notifier.send_whatsapp(order_id)

    elif choice == '3':
        print("Thank you for visiting! Goodbye!")
        break

    else:
        print("\nInvalid option. Please try again.\n")

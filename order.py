
def order():
    order_list=[]       #empty list to store the order
    while True:
        choice = input("Enter your order (or 'done' to finish): ")
        if choice == 'done':
            break
        else:
  
            if 1 <= int(choice) <= 14:   # Checking if the choice is a valid menu item
                # Asking for the quantity
                quantity = int(input("Enter the quantity: "))
                if quantity > 0:
                    order_list.append((choice, quantity))
                else:
                    print("Invalid quantity. Please enter a positive number.")
            else:
                print("Invalid choice. Please select a valid item number.")
    return order_list

def show_summary(order_list):    #function to display the order summary
    print("\nOrder Summary:")
    for item, quantity in order_list:    #iterating through the order list
        if item == '1':
            item = "Chicken Wings"
        elif item == '2':
            item = "Fries"
        elif item == '3':
            item = "Soup"
        elif item == '4':
            item = "Biryani"
        elif item == '5':
            item = "Chicken Karahi"
        elif item == '6':
            item = "Naan"
        elif item == '7':
            item = "BBQ Platter"
        elif item == '8':
            item = "Kheer"
        elif item == '9':
            item = "Gulab Jamun"
        elif item == '10':
            item = "Ice Cream"
        elif item == '11':
            item = "Soft Drink"
        elif item == '12':
            item = "Lassi"
        elif item == '13':
            item = "Tea"
        elif item == '14':
            item = "Coffee"
        print(f"You chose {item} from menu : quantity {quantity}")
    print("Thank you for your order!")


def take_order():
    order_list = []
    while True:
        choice = input("Enter your order (1-14) or 'done' to finish: ")
        if choice.lower() == 'done':
            break
        try:
            item_no = int(choice)
            if 1 <= item_no <= 14:
                quantity = int(input("Enter quantity: "))
                if quantity > 0:
                    order_list.append((item_no, quantity))
                else:
                    print("Please enter a positive quantity.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Invalid input. Enter a number or 'done'.")
    return order_list


def show_summary(order_list):
    item_names = {
        1: "Chicken Wings",
        2: "Fries",
        3: "Soup",
        4: "Biryani",
        5: "Chicken Karahi",
        6: "Naan",
        7: "BBQ Platter",
        8: "Kheer",
        9: "Gulab Jamun",
        10: "Ice Cream",
        11: "Soft Drink",
        12: "Lassi",
        13: "Tea",
        14: "Coffee"
    }

    print("\nOrder Summary:")
    for item_no, quantity in order_list:
        item = item_names.get(item_no, "Unknown Item")
        print(f"You chose {item} from menu : quantity {quantity}")
    

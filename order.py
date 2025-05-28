# order.py

def take_order(menu_items):
    order_list = []
    while True:
        choice = input("Enter your order or 'done' to finish: ")
        if choice.lower() == 'done':
            break
        try:
            item_no = int(choice)
            if item_no in menu_items:
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


def show_summary(order_list, menu_items):
    print("\nOrder Summary:")
    for item_no, quantity in order_list:
        item = menu_items.get(item_no, ("Unknown Item",))[0]
        print(f"You chose {item} from menu : quantity {quantity}")

def get_next_order_id():
    try:
        with open("order_counter.txt", "r") as f:
            last_id = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        last_id = 1000  # Starting order number

    next_id = last_id + 1

    with open("order_counter.txt", "w") as f:
        f.write(str(next_id))

    return next_id


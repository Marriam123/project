import datetime
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
menu = {
    '1': "Chicken Wings",
    '2': "Fries",
    '3': "Soup",
    '4': "Biryani",
    '5': "Chicken Karahi",
    '6': "Naan",
    '7': "BBQ Platter",
    '8': "Kheer",
    '9': "Gulab Jamun",
    '10': "Ice Cream",
    '11': "Soft Drink",
    '12': "Lassi",
    '13': "Tea",
    '14': "Coffee"
}

items = []
quantities = []
prices = []
totals = []

print("Menu:")
for num, name in menu.items():
    print(num + ".", name)

while True:
    item_num = input("Choose item number: ")
    if item_num not in menu:
        print("Wrong choice, try again.")
        continue

    item_name = menu[item_num]
    quantity = int(input("How many " + item_name + "?: "))
    price = float(input("Price of one " + item_name + ": "))

    items.append(item_name)
    quantities.append(quantity)
    prices.append(price)
    totals.append(quantity * price)

    more = input("Add more items? (yes/no): ")
    if more.lower() != "yes":
        break

discount = float(input("Discount % (0 if none): "))
tax = float(input("Tax % (0 if none): "))

print("\nBill:")
total = 0
for i in range(len(items)):
    print(items[i], "x", quantities[i], "=", totals[i])
    total += totals[i]

if discount > 0:
    disc = total * discount / 100
    total -= disc
    print("Discount:", disc)
else:
    disc = 0

if tax > 0:
    t = total * tax / 100
    total += t
    print("Tax:", t)
else:
    t = 0

print("Total:", total)

f = open("bills.txt", "a")
f.write("\nBill\n")
f.write("Date: " + str(datetime.datetime.now()) + "\n")
for i in range(len(items)):
    f.write(items[i] + " x " + str(quantities[i]) + " = " + str(totals[i]) + "\n")
if disc > 0:
    f.write("Discount: " + str(disc) + "\n")
if t > 0:
    f.write("Tax: " + str(t) + "\n")
f.write("Total: " + str(total) + "\n")
f.write("---------\n")
f.close()
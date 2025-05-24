import datetime

class Order:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.total = quantity * price

class Bill:
    def __init__(self):
        self.menu = {
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
        self.orders = []

    def take_order(self):
        print("Menu:")
        for num, name in self.menu.items():
            print(num + ".", name)

        while True:
            item_num = input("Choose item number: ")
            if item_num not in self.menu:
                print("Wrong choice, try again.")
                continue

            item_name = self.menu[item_num]
            quantity = int(input(f"How many {item_name}?: "))
            price = float(input(f"Price of one {item_name}: "))

            self.orders.append(Order(item_name, quantity, price))

            more = input("Add more items? (yes/no): ")
            if more.lower() != "yes":
                break

    def calculate_total(self, discount_percent, tax_percent):
        print("\nBill:")
        subtotal = 0
        for order in self.orders:
            print(f"{order.item_name} x {order.quantity} = {order.total}")
            subtotal += order.total

        discount = subtotal * discount_percent / 100
        subtotal -= discount

        tax = subtotal * tax_percent / 100
        total = subtotal + tax

        if discount_percent > 0:
            print(f"Discount: {discount}")
        if tax_percent > 0:
            print(f"Tax: {tax}")
        print(f"Total: {total}")

        self.save_to_file(discount, tax, total)

    def save_to_file(self, discount, tax, total):
        with open("bills.txt", "a") as f:
            f.write("\nBill\n")
            f.write("Date: " + str(datetime.datetime.now()) + "\n")
            for order in self.orders:
                f.write(f"{order.item_name} x {order.quantity} = {order.total}\n")
            if discount > 0:
                f.write("Discount: " + str(discount) + "\n")
            if tax > 0:
                f.write("Tax: " + str(tax) + "\n")
            f.write("Total: " + str(total) + "\n")
            f.write("---------\n")


my_bill = Bill()
my_bill.take_order()
discount = float(input("Discount % (0 if none): "))
tax = float(input("Tax % (0 if none): "))
my_bill.calculate_total(discount, tax)

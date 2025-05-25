import datetime

class Order:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = int(quantity)
        self.price = int(price)
        self.total= self.calculate_total()

    def calculate_total(self):
        return self.quantity * self.price
    
    def __str__(self):
        return f"Item: {self.item_name}, Quantity: {self.quantity}, Price: {self.price}, Total: {self.total}"
    
def add_bills(orders, subtotal, discount_amount, tax_amount, final_total):
    with open("bills.txt", "a") as file:
        file.write(f"Order Date: {datetime.datetime.now()}\n")
        for order in orders:
            file.write(str(order) + "\n")
        file.write(f"Subtotal: Rs. {subtotal}\n")
        file.write(f"Discount: -Rs. {discount_amount}\n")
        file.write(f"Tax: +Rs. {tax_amount}\n")
        file.write(f"Total Payable: Rs. {final_total:.2f}\n\n")


def billing_summary(orders):
    subtotal = 0
    print("\n" + "="*40)
    print("              BILLING SUMMARY")
    print("="*40)
    
    for order in orders:
        print(order)
        subtotal += order.total

    print(f"\nSubtotal: Rs. {subtotal:.2f}")

    # Apply discount if subtotal > 1000
    discount_percentage = 10
    discount_amount = 0

    if subtotal > 1000:
        discount_amount = (subtotal * discount_percentage) / 100
        print(f"Discount ({discount_percentage}%): -Rs. {discount_amount:.2f}")
    else:
        print("No discount applied (subtotal must be over Rs. 1000).")

    subtotal_after_discount = subtotal - discount_amount

    # Apply tax
    tax_percentage = 5
    tax_amount = (subtotal_after_discount * tax_percentage) / 100
    print(f"Tax ({tax_percentage}%): +Rs. {tax_amount:.2f}")

    final_total = subtotal_after_discount + tax_amount

    print(f"\nTotal Payable Amount: Rs. {final_total:.2f}")
    print("Thank you for your order!")

    add_bills(orders, subtotal, discount_amount, tax_amount, final_total)


# billing.py

class Order:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.total = self.quantity * self.price

def calculate_final_price(orders):
    subtotal = sum(o.total for o in orders)
    subtotal = float(subtotal)  # Converting to float here

    discount = 0.10 * subtotal if subtotal >= 1000 else 0
    tax = 0.05 * (subtotal - discount)
    final_price = subtotal - discount + tax
    return round(final_price, 2), round(discount, 2), round(tax, 2)


def billing_summary(orders, email, phone, order_id=None):
    print("\n===== BILL SUMMARY =====")
    for order in orders:
        print(f"{order.quantity} x {order.item_name} @ Rs. {order.price} = Rs. {order.total}")

    subtotal = sum(o.total for o in orders)
    subtotal = float(subtotal)  # Convert here too

    discount = 0.10 * subtotal if subtotal >= 1000 else 0
    tax = 0.13 * (subtotal - discount)
    final_price = subtotal - discount + tax

    print(f"\nSubtotal: Rs. {subtotal}")
    if discount > 0:
        print(f"Discount (10%): -Rs. {round(discount, 2)}")
    print(f"Tax (13%): Rs. {round(tax, 2)}")
    print(f"Final Amount: Rs. {round(final_price, 2)}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")
    if order_id:
        print(f"Order ID: {order_id}")
    print("=========================\n")


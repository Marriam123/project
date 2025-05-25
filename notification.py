# notification.py

from datetime import datetime
import random  # for generating order IDs in simulation

class NotificationManager:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

    def send_email(self, order_id):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[Email Notification at {time}]")
        print(f"Email sent to {self.email} - Your order #{order_id} has been confirmed.")

    def send_whatsapp(self, order_id):
        time = datetime.now().strftime("%I:%M %p")
        print(f"\n[WhatsApp Notification at {time}]")
        print(f"Message sent to {self.phone} - Your order #{order_id} will be delivered soon.")
 

# 6) Delivery Address Manager
# Create class Delivery
class Delivery:
    def __init__(self, customer_name, address):
        self.customer_name = customer_name
        self.address = address

    def show(self):
        print("Delivery Details")
        print("Customer:", self.customer_name)
        print("Address:", self.address)
customer_name = input("Customer Name: ")
address = input("Address: ")

d = Delivery(customer_name, address)
d.show()
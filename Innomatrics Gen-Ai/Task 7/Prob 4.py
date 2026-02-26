# 4) Product Price Tag Generator
# Create class Product

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def show(self):
        print("Product:", self.name)
        print("Price: ₹" + str(self.price))
name = input("Product Name: ")
price = int(input("Price: "))

p = Product(name, price)
p.show()
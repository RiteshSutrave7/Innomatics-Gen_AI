# 3) Mobile Contact Record
# Create class Contact
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def show(self):
        print("Contact Saved")
        print("Name:", self.name)
        print("Phone:", self.phone)
name = input("Contact Name: ")
phone = input("Phone Number: ")
con1 = Contact(name, phone)
con1.show()
# 2) Employee ID Card System
# Create class Employee 
class Employee:
    def __init__(self, emp_name, emp_id, department):
        self.name = emp_name
        self.emp_id = emp_id
        self.department = department

    def show(self):
        print("Employee ID Card")
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Department:", self.department)

emp_name = input("Employee Name: ")
emp_id = input("Employee ID: ")
department = input("Department: ")

emp = Employee(emp_name, emp_id, department)
emp.show()
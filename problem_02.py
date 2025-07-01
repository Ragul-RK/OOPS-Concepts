class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class manager(employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info() # Calls the parent method to carry forward existing values into the overridden method
        print(f"Department: {self.department}") 
        

tl = manager("ragul",12500,"td")
tl.display_info()


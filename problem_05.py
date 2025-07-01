"""
    Q2: Employee Management System
        Create a base class Employee with the following
            A constructor that accepts name and salary.
            A method display() that prints the employee name and salary.
            Make the salary attribute private.
            Add getter and setter methods for salary.

    Create a derived class Manager that:
        Inherits from Employee.
        Has an additional attribute department.
        Overrides the display() method to also print the department.
        
    🎯 What You Will Practice:
        Class inheritance
        Encapsulation using private variables
        Method overriding
        Constructor chaining using super()

🧪 Sample Output:
        Name: Alice
        Salary: 90000
        Department: HR

"""

# class Employee: 
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary  # Private attribute

#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.__salary)

#     @property
#     def salary(self):  # Getter
#         return self.__salary

#     @salary.setter
#     def salary(self, value):  # Setter
#         self.__salary = value


# # Create object
# emp = Employee("Ragul", 15000)

# # Call display (already prints values inside)
# emp.display()

# # Use the getter
# print("Getting Salary using getter:", emp.salary)

# # Use the setter
# emp.salary = 20000  # No need to wrap in print

# # Confirm updated salary
# print("Updated Salary using getter:", emp.salary)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.__salary)
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value):
        self.__salary = value


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department=department
    def display(self):
        self.salary=self.salary+100
        super().display()
        print("Department:", self.department)


m1 = Manager("Alice", 90200, "HR")
m1.display()
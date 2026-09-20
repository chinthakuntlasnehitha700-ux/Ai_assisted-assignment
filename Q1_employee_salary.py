# Employee Salary Calculator

class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    # Calculate bonus based on salary
    def calculate_bonus(self):
        if self.basic_salary >= 50000:
            return self.basic_salary * 0.10
        else:
            return self.basic_salary * 0.05

    # Calculate total salary
    def calculate_total_salary(self):
        return self.basic_salary + self.calculate_bonus()

    # Display employee details
    def display_details(self):
        bonus = self.calculate_bonus()
        total_salary = self.calculate_total_salary()

        print("Employee Name:", self.name)
        print("Basic Salary: ₹", self.basic_salary)
        print("Bonus: ₹", bonus)
        print("Total Salary: ₹", total_salary)
        print("-" * 30)


# Create two employee objects
employee1 = Employee("Rahul", 60000)
employee2 = Employee("Priya", 40000)

# Display details
employee1.display_details()
employee2.display_details()
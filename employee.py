class Employee:

    emp_count = 0
    increment_rate = 1.10

    def __init__(self, emp_id, first_name, last_name, salary):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"

        Employee.emp_count += 1

    def full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def apply_increment(self):
        self.salary = int(self.salary * Employee.increment_rate)

    def display(self):
        print("\nEmployee Details")
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.full_name()}")
        print(f"Email: {self.email}")
        print(f"Salary: ₹{self.salary}")
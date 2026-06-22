class EmployeeManagement:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_all_employees(self):

        if not self.employees:
            print("No employees found.")
            return

        for emp in self.employees:
            print("-" * 30)
            emp.display()

    def search_employee(self, emp_id):

        for emp in self.employees:

            if emp.emp_id == emp_id:
                emp.display()
                return

        print("Employee not found.")

    def delete_employee(self, emp_id):

        for emp in self.employees:

            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print("Employee deleted successfully.")
                return

        print("Employee not found.")
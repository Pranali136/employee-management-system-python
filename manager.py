from employee import Employee


class Manager(Employee):

    def __init__(self, emp_id, first_name, last_name, salary):
        super().__init__(emp_id, first_name, last_name, salary)
        self.team = []

    def add_employee(self, employee):

        if employee not in self.team:
            self.team.append(employee)

    def remove_employee(self, employee):

        if employee in self.team:
            self.team.remove(employee)

    def show_team(self):

        print("\nTeam Members")

        if not self.team:
            print("No employees assigned.")
            return

        for emp in self.team:
            print(emp.full_name())
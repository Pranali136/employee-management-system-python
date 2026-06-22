from employee import Employee


class Developer(Employee):

    def __init__(self, emp_id, first_name, last_name, salary, language):
        super().__init__(emp_id, first_name, last_name, salary)
        self.language = language

    def display(self):
        super().display()
        print(f"Programming Language: {self.language}")
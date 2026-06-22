from employee import Employee
from developer import Developer
from manager import Manager
from employee_management import EmployeeManagement


system = EmployeeManagement()

while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Add Developer")
    print("3. Display Employees")
    print("4. Search Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        emp_id = int(input("Employee ID: "))
        first = input("First Name: ")
        last = input("Last Name: ")
        salary = int(input("Salary: "))

        emp = Employee(emp_id, first, last, salary)
        system.add_employee(emp)

        print("Employee Added Successfully")

    elif choice == "2":

        emp_id = int(input("Employee ID: "))
        first = input("First Name: ")
        last = input("Last Name: ")
        salary = int(input("Salary: "))
        language = input("Programming Language: ")

        dev = Developer(
            emp_id,
            first,
            last,
            salary,
            language
        )

        system.add_employee(dev)

        print("Developer Added Successfully")

    elif choice == "3":

        system.show_all_employees()

    elif choice == "4":

        emp_id = int(input("Enter Employee ID: "))
        system.search_employee(emp_id)

    elif choice == "5":

        emp_id = int(input("Enter Employee ID: "))
        system.delete_employee(emp_id)

    elif choice == "6":

        print("Thank You")
        break

    else:

        print("Invalid Choice")
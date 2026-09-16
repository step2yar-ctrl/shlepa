class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name} — {self.position}, зарплата: {self.salary} грн"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                return True
        return False

    def total_salary(self):
        return sum(employee.salary for employee in self.employees)

    def show_employees(self):
        print(f"\nВідділ: {self.name}")
        for employee in self.employees:
            print(employee)



department = Department("IT")


while True:
    name = input("\nведіть імя співробітника (або стоп): ")

    if name.lower() == "стоп":
        break

    position = input("ведіть посаду: ")
    salary = float(input("ведіть зарплату: "))

    employee = Employee(name, position, salary)
    department.add_employee(employee)


department.show_employees()


print(f"\nзагальна зарплата відділу: {department.total_salary()} грн")


name = input("\nведіть імя співробітника для видалення: ")

if department.remove_employee(name):
    print("співробітника видалено.")
else:
    print("співробітника не знайдено.")


print(f"зарплата після видалення: {department.total_salary()} грн")
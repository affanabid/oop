class Department:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Employee:

    def __init__(self, employee_number, name, cnic, phone, address, department):
        self.emp_no = employee_number
        self.name = name
        self.cnic = cnic
        self.phone = phone
        self.address = address
        self.department = department
    
    def __str__(self) -> str:
        return f'Address: {self.address}\nPhone: {self.phone}\nCNIC: {self.cnic}\nDepartment {self.department.name}'

class SalariedEmployees(Employee):

    def __init__(self, employee_number, name, cnic, phone, address, weekly_salary, department):
        super().__init__(employee_number, name, cnic, phone, address, department)
        self.weekly_salary = weekly_salary
    
    def __str__(self) -> str:
        return super().__str__()
        
class HourlyEmployees(Employee):

    def __init__(self, employee_number, name, cnic, phone, address, department, hours_worked, rate_per_hour) -> None:
        super().__init__(employee_number, name, cnic, phone, address, department)
        self.hours_worked = hours_worked
        self.rph = rate_per_hour
        self.weekly_salary = self.hours_worked * self.rph

    def __str__(self) -> str:
        return super().__str__()

class Payroll:

    sales_department = Department("Sales", "Lahore")
    accounting_department = Department("Accounting", "Kasur")
    manufacturing_department = Department("Manufacturing", "Faisalabad")
    employees = [
        SalariedEmployees(1, 'Musa', '12345-6789123-0', '0310-4976543', 'tajbagh', 10, sales_department),
        HourlyEmployees(2, 'ali', '00000-000000-0', '0310-9845678', 'JoharTown', accounting_department , 10, 20),
        HourlyEmployees(2, 'amir', '00000-000000-0', '0310-9845678', 'JoharTown', manufacturing_department, 10, 20)
    ]

    for employee in employees:
        print(f'{employee.emp_no}. Employee: {employee.name}\nSalary: {employee.weekly_salary}')
        print(f'{employee}\n')
p = Payroll()

        

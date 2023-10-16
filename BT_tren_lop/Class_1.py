class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def emp_assign_department(self, department):
        self.emp_department = department

    def print_employee_detail(self):
        print(f"{self.emp_id} {self.emp_name} {self.emp_salary} {self.emp_department}")

    def calculate_emp_salary(self, salary, hour_worked):
        if(hour_worked > 50):
            return salary + (hour_worked-50)*(salary/50)
        else:
            return salary


nv1 = Employee("E7868", "ADAM", 50000, "ACCOUNTING")
nv1.print_employee_detail()
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method")
    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, base_salary):
        super().__init__(emp_id, name)
        self.base_salary = base_salary

    def calculate_salary(self):
        hra = 0.2 * self.base_salary
        da = 0.1 * self.base_salary
        pf = 0.12 * self.base_salary
        return self.base_salary + hra + da - pf
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Deparment:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employee = []
    
    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError("Only Employee objects can be added")
        self.employee.append(employee)
    def total_salary(self):
        return sum(emp.calculate_salary() for emp in self.employee)
    
    def highest_paid_employee(self):
        if not self.employee:
            return None
        return max(self.employee, key=lambda emp: emp.calculate_salary())
    

# Example Usage
# create employees
ft_emp1 = FullTimeEmployee(1, "Alice", 50000)
pt_emp1 = PartTimeEmployee(2, "Bob", 200, 80)
ft_emp2 = FullTimeEmployee(3, "Charlie", 60000)
pt_emp2 = PartTimeEmployee(4, "David", 250, 60)

# create department and add employees
dept = Deparment("Engineering")

dept.add_employee(ft_emp1)
dept.add_employee(pt_emp1)
dept.add_employee(ft_emp2)
dept.add_employee(pt_emp2)

# calculate total salary
print(f"Total Salary Expense: {dept.total_salary()}")
# find highest paid employee
highest_paid = dept.highest_paid_employee()
print(f"Highest Paid Employee: {highest_paid}, Salary: {highest_paid.calculate_salary()}")
print(f"The details of employee: Employee ID is {highest_paid.emp_id}, Name is {highest_paid.name}")
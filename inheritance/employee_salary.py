class Employee:
    def __init__(self,emp_id, name):
        self.emp_id = emp_id
        self.name = name
    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method")    
 
class PermanentEmployee(Employee):
    def __init__(self, emp_id, name, basic_salary):
        super().__init__(emp_id, name)
        self.basic_salary = basic_salary
  
    def calculate_salary(self):
        hra = 0.20 * self.basic_salary
        da = 0.10 * self.basic_salary
        pf = 0.05 * self.basic_salary
        return self.basic_salary + hra + da - pf
    
    def __str__(self):
        return f"PermanentEmployee[ID: {self.emp_id} | Name: {self.name} | Basic Salary: {self.basic_salary}  | Net Salary: {self.calculate_salary()}]"
    
class ContractEmployee(Employee):
    def __init__(self, emp_id, name, daily_rate, days_worked):
        super().__init__(emp_id, name)
        self.daily_rate = daily_rate
        self.days_worked = days_worked

    def calculate_salary(self):
        return self.daily_rate * self.days_worked
    
    def __str__(self):
        return f"ContractEmployee[ID: {self.emp_id} | Name: {self.name} | Daily Rate: {self.daily_rate} | Days Worked: {self.days_worked} | Net Salary: {self.calculate_salary()}]"
# Example usage:
employees= [
    PermanentEmployee(1, "Alice", 50000),
    ContractEmployee(2, "Bob", 2000, 22)
]

for emp in employees:
    print(emp)
    # print(f"Calculated Salary: {emp.calculate_salary()}")

class Employee:
    def __init__(self,emp_id, name, department, basic_salary):
        self.emp_id = emp_id,
        self.name = name
        self.department = department
        self.basic_salary = basic_salary

    def annual_salary(self):
        return self.basic_salary * 12
    
    def display(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"Annual Salary: {self.annual_salary()}")

        print(f"The details of employee: Employee Id is {self.emp_id}, Name is {self.name}, Department is {self.department}, Basic Salary is {self.basic_salary}, Annual Salary is {self.annual_salary()}")
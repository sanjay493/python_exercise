class BankAccount:
    def __init__(self, accoun_no, holder_name, balance):
        self.account_no = accoun_no
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance
    def get_balance(self):
        return self.balance
    
    def display(self):
        print(f"Account Number: {self.account_no}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: {self.balance}")

        print(f"The details of bank account: Account Number is {self.account_no}, Holder Name is {self.holder_name}, Balance is {self.balance}")
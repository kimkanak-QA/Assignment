# Difficulty: Beginner
# Scenario
# A bank needs to model a basic savings account that tracks an owner's balance and supports deposits and
# withdrawals with simple validation.
# Task
# Create a class called BankAccount with the following specification:
# - Attributes: owner (str) and balance (float, default 0.0)
# - Method deposit(amount): adds the amount to the balance
# - Method withdraw(amount): subtracts the amount from the balance. If the balance is insufficient, print
# "Insufficient funds!" and do not change the balance
# - Method get_balance(): returns the current balance
# Expected Usage
# acc = BankAccount("Kanak")
# acc.deposit(5000)
# acc.withdraw(2000)
# acc.get_balance() # Expected: 3000.0
# acc.withdraw(5000) # Expected: prints 'Insufficient funds!'

class BankAccount:

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


# Expected Usage
acc = BankAccount("Kanak")

acc.deposit(5000)
acc.withdraw(2000)

print(acc.get_balance())  # Expected: 3000.0

acc.withdraw(5000)  # Expected: Insufficient funds!
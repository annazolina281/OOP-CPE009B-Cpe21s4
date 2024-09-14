class ATM:
    def __init__(self, serial_number=0, user_account=None):
        self.serial_number = serial_number
        self.user_account = user_account
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.user_account.balance += amount
            self.transactions.append(f"Deposited ${amount}")
            print("Deposit Complete")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.user_account.balance:
            self.user_account.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            print("Withdrawal Complete")
        else:
            print("Insufficient funds or invalid amount.")

    def check_current_balance(self):
        return self.user_account.balance

    def view_transactions(self):
        if self.transactions:
            print("Transaction History:")
            for transaction in self.transactions:
                print(transaction)
        else:
            print("No transactions yet.")

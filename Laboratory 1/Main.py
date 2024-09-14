import random
import Accounts
import ATM

account1 = Accounts.Account(account_number=123456, first_name="Royce", last_name="Chua", 
                            balance=1000, address="Silver Street, Quezon City", 
                            email="roycechua123@gmail.com")

print("Account 1")
print(f"Name: {account1.first_name} {account1.last_name}")
print(f"Balance: ${account1.balance}")
print(f"Address: {account1.address}")
print(f"Email: {account1.email}")

print()

account2 = Accounts.Account(account_number=654321, first_name="John", last_name="Doe", 
                            balance=2000, address="Gold Street, Quezon City", 
                            email="johndoe@yahoo.com")

print("Account 2")
print(f"Name: {account2.first_name} {account2.last_name}")
print(f"Balance: ${account2.balance}")
print(f"Address: {account2.address}")
print(f"Email: {account2.email}")

print()

atm1 = ATM.ATM(serial_number=random.randint(100000, 999999), user_account=account1)
atm2 = ATM.ATM(serial_number=random.randint(100000, 999999), user_account=account2)

atm1.deposit(500)
print(f"ATM1 Serial ID: {atm1.serial_number}")
print(f"Current Balance (Account 1): ${atm1.check_current_balance()}")

atm2.deposit(300)
print(f"ATM2 Serial ID: {atm2.serial_number}")
print(f"Current Balance (Account 2): ${atm2.check_current_balance()}")

print("\nATM1 Transaction History:")
atm1.view_transactions()

print("\nATM2 Transaction History:")
atm2.view_transactions()

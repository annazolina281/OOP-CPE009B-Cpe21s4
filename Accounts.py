class Account:
    def __init__(self, account_number, first_name, last_name, balance, address='', email=''):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.address = address
        self.email = email

    def update_address(self, new_address):
        self.address = new_address
        
    def update_email(self, new_email):
        self.email = new_email

        

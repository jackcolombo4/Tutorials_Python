class Account:
    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

class Transaction:
    def __init__(self, source_account, target_account, amount):
        self.source_account = source_account
        self.target_account = target_account
        self.amount = amount

    def execute(self):
        if self.amount <= 0:
            raise ValueError("Amount must be positive")
        if self.source_account.balance < self.amount:
            raise ValueError("Insufficient balance in source account")
        self.source_account.withdraw(self.amount)
        self.target_account.deposit(self.amount)

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, balance=0):
        if account_id in self.accounts:
            raise ValueError("Account already exists")
        account = Account(account_id, balance)
        self.accounts[account_id] = account

    def get_account_balance(self, account_id):
        if account_id not in self.accounts:
            raise ValueError("Account does not exist")
        return self.accounts[account_id].balance

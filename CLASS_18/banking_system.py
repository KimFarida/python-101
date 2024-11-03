from abc import ABC, abstractmethod
from datetime import datetime
'''
    we’ll model a basic banking system with accounts, transactions,
     and simple operations like deposits, withdrawals, and checking balances.


    Blueprint
    Bank System

    Manages multiple bank accounts.
    Allows for account creation, deletion, and summary display of all accounts.
    Account (Abstract Class)

    Defines basic properties (account holder, balance).
    Implements core methods (deposit, withdraw).
    SavingsAccount & CheckingAccount (Inheritance)

    Savings Account has interest calculation.
    Checking Account has overdraft feature.
    Transaction (Class)

    Logs details of each transaction (date, amount, type).
'''

# Step 1: Define the abstract Account class to model a basic bank account
class Account(ABC):

    # fields  account_number, account_holder, account_balance, transactions list
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def __str__(self):
        return f"Account Holder : {self.account_holder}, Account Balance : {self.balance}\n"

    @abstractmethod
    def withdraw(self, amount):
        """Withdraw money from account"""
        pass

    def display_balance(self):
        """Display current balance"""
        print(f"""
        Balance : {self.balance}
        Account Name : {self.account_holder}
        Account Number : {self.account_number}
""")

    def add_transaction(self, amount, transaction_type):
        # Create a new Transaction Object
        transaction = Transaction(amount, transaction_type)
        self.transactions.append(transaction)

    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction)




#add abstract methods i,e withdraw, display_balance, add_transaction, display_transaction

# Step 2: Create a SavingsAccount class with interest (inherits from Account)
#will add the field interest and implement all methods from the abstract class
#including a calculate interest method
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, interest_rate=0.05):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def __str__(self):
        return f'Account Type: Savings Account'

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.add_transaction(amount, "Deposit")


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance =  self.balance - amount
            self.add_transaction(amount, "Withdraw")
        else:
            print(f"INSUFFICIENT FUNDS, BALANCE : {self.balance}")

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added to balance. New Balance : {self.balance}")


# Step 3: Create a CheckingAccount class with an overdraft feature
class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, overdraft_limit=10000):
        super().__init__(account_number, account_holder)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        super().__str__()
        return f"Account Type : Checking Account"

    def deposit(self, amount):
        self.balance += amount
        self.add_transaction(amount, "Deposit")

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.add_transaction(-amount, "Withdrawal")
        else:
            print("INSUFFICIENT FUNDS EVEN WITH ADDITION OF OVERDRAFT")



# Step 4: Create a Transaction class to model transactions
class Transaction:
    # Initialize transaction with date, amount, and type
    def __init__(self,amount, transaction_type):
        self.date = datetime.now()
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} || {self.transaction_type} || {self.amount}"

# Step 5: Define a Bank class to manage all accounts and operations
class Bank:
    # INITIALIZATION - # Store all accounts by account number in a dictionary
    def __init__(self):
        self.accounts = {}

    # Create a new account of the specified type and store it
    def create_account(self, account_type, account_number, account_holder):
        if account_type == 'savings':
            account = SavingsAccount(account_number,account_holder)
        elif account_type == 'checking':
            account = CheckingAccount(account_number, account_holder)
        else:
            print('Unknown Account Type')
            return

        self.accounts[account_number] = account
        print(f"Account created NAME : {account_holder} ACCOUNT NUMBER : #{account_number}")

    # Remove an account by account number
    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
        else:
            print("Account not Found")

    # Show all accounts in the bank
    def display_accounts(self):
        for account_number, account in self.accounts.items():
            print(account_number, end=' ')
            print(account)

    # Retrieve an account by account number for further operations
    def get_account(self, account_number):
        return self.accounts.get(account_number, "ACCOUNT NOT FOUND")

#TEST
bank = Bank()
bank.create_account('savings', 1003, 'Seyi')
bank.create_account('checking', 1009, 'Mahmud')

# seyi_account = bank.get_account(1003)
# if seyi_account:
#     seyi_account.deposit(500)
#     seyi_account.display_balance()
#     seyi_account.calculate_interest()
#     seyi_account.display_balance()
#
mahmud_account = bank.get_account(1009)
if mahmud_account:
    mahmud_account.deposit(20000)
    mahmud_account.withdraw(20000)
    mahmud_account.withdraw(10000)
    mahmud_account.withdraw(10000)
    mahmud_account.display_balance
    mahmud_account.display_transactions()
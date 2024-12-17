class BankAccount:
    def __init__(self, owner):
        self._owner = owner  # Protected attribute
        self.__balance = 0  # Private attribute

    @property
    def balance(self):  # Getter
        return self.__balance

    def deposit(self, amount):  # Setter method
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def _get_account_info(self):  # Protected method
        return f"Owner: {self._owner}, Balance: {self.__balance}"


# Usage example
account = BankAccount("Alice")
account.deposit(1000)
print(account.balance)  # Using property
#print(account.__balance)     # This will raise an error
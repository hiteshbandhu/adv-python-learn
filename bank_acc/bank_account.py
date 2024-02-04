class BalanceException(Exception):
    """ Raises exception when the balance amount is lower than the withdrawl amount """

    pass

class BankAccount:
    """ The main class used to make new accounts and perform operations on pre-existing accounts """

    def __init__(self, name:str, init_amt:float):
        self.name = name
        self.balance = init_amt
        print(f"\n\nAccount {self.name} created with Balance {self.balance:.2f}\n\n")

    def get_balance(self):
        print(f"{self.name} has Balance {self.balance:.2f}")

    def deposit(self, amount:float):
        self.balance += amount
        print(f"Money Deposited, New Balance for {self.name}: {self.balance:.2f}\n\n")

    def _viable_transaction(self, amount:float):
        """ PRIVATE METHOD. Checks if the transaction is viable, then proceeds or raises an error  """

        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry ! {self.name} only has {self.balance:.2f}, which is less than the amount requested")
        
    def withdraw(self, amount:float):
        try:
            self._viable_transaction(amount)
            self.balance -= amount
            print(f"\n {amount:.2f} withdrawn successfully !\n\n")
            self.get_balance()
        except BalanceException as error:
            print(error)

    def transfer(self, amount:float, account):
        try:
            self._viable_transaction(amount)
            self.balance -= amount
            print('\nWithdraw Successful !\n')
            self.get_balance()
            account.deposit(amount)
        except BalanceException as error:
            print(error)

    
class IntrAccount(BankAccount):
    """ Opens a new Interest Account, which gives a 5% premium on new deposits. """

    def deposit(self, amount: float):
        self.dep_intr = 1.05
        self.balance += (amount * self.dep_intr)
        self.get_balance()

class SavingAccount(IntrAccount):
    """ Opens a new savings account, which charges an amount of 5 per withdrawl """

    def __init__(self, name: str, init_amt: float):
        super().__init__(name, init_amt)
        self.wthdr_fee = 5
    def withdraw(self, amount: float):
        try:
            self._viable_transaction(amount)
            self.balance -= (amount + self.wthdr_fee)
            print(f"Amount {amount} withdrawn from {self.name}")
            self.get_balance()
        except BalanceException as error:
            print(error)

import datetime
import pytz

class Account:
    """Simple class account with balance"""

    # Class Variables
    account_type = 'default_type'

    # Static methods
    # The convention is that method starting with underscore are not public
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    # Instantiation
    def __init__(self, name, balance):
        # instance variables
        # 1. Attributes that start with a single underscore are meant to be used internally but nothing prevents mess
        # with them
        # 2 . The other option is to user two underscores. By doing this python mangles the variable using the name of
        # the class  when you use it internally in this case __balance is _Account__balance internally, but if the
        # variable is called from the outside it stays with no mangling so it can not be modified.
        # Second option is DISCOURAGED by python community, there is no point to complcate variable access, just follow
        # the convention and use good practices
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for {}".format(self._name))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("the amount must be greater than 0 and no more than {}".format(self.__balance))

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account('Tim', 0)

    tim.deposit(1000)
    tim.deposit(2000)
    tim.withdraw(40000)
    tim.withdraw(400)
    tim.show_transactions()

    carlos = Account("Carlos", 800)
    carlos.deposit(100)
    carlos.__balance = 200000
    carlos.withdraw(200)
    carlos.show_transactions()
    carlos.show_balance()



"""Demonstrate use of some bank account methods.
   The output for check deposits is misleading, 
   it looks like a new check each time.
"""
from bank_account import BankAccount
from money import Money
from check import Check


def show_balance(account: BankAccount):
    print(
        f"Balance {account.balance:8,.2f}  Available: {account.available:8,.2f}")


def perform(fun, arg):
    """Print and then invoke a function with one parameter."""
    print(f"{fun.__name__}({repr(arg)})")
    fun(arg)


if __name__ == '__main__':
    acct = BankAccount("Taksin Shinawat")
    print(f"Account {acct.account_name}, minimum balance {acct.min_balance}")
    perform(acct.deposit, Money(10000))
    show_balance(acct)
    check = Check(25000)
    perform(acct.deposit, check)
    print(f"{check} deposited")
    check2 = Check(5000)
    perform(acct.deposit, check2)
    print(f"{check2} deposited")
    show_balance(acct)
    print("Try to withdraw 30,000")
    try:
        perform(acct.withdraw, 30000)
        print("You withdrew 30,000")
    except ValueError as e:
        print("Error:", e)
    perform(acct.clear_check, check)
    print("Try to withdraw 30,000")
    try:
        perform(acct.withdraw, 30000)
        print("You withdrew 30,000")
    except ValueError as e:
        print("Error:", e)
    show_balance(acct)
    print("Deposit same check that was already deposited & cleared")
    try:
        perform(acct.deposit, check)
        print(f"{check} deposited")
    except ValueError as e:
        print("Deposit failed")
        print("Error:", e)
    show_balance(acct)
#   >>> acct.withdraw(30000)           # try to withdraw 30,000
#   Traceback (most recent call last):
#      ...
#   ValueError: Amount exceeds available balance
#   >>> acct.clear_check(c)
#   >>> acct.available                 # now the check value is available
#   49000.0
#   >>> acct.withdraw(30000)           # withdraw 30,000 should work
#   Money(30000, 'Baht')
#   >>> acct.balance
#   20000.0
#   >>> acct.withdraw(20000)           # try to withdraw EVERYTHING
#   Traceback (most recent call last):
#      ...
#   ValueError: Amount exceeds available balance
#   >>> acct.withdraw(15000)
#   Money(15000, 'Baht')
#   >>> acct.balance
#   5000.0

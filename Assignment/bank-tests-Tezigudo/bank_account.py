from money import Money
from check import Check


class BankAccount:
    """
    A BankAccount with a minimum required balance (default is 0)
    that accepts deposits of Money or Checks.

    A BankAccount has a balance and an "available balance".
    The balance is always the total of all deposits minus withdraws.
    However, the value of a check is not available for withdraw until
    the check clears by calling `clear_check(check)`. This simulates
    the "clearing" of checks in a real bank.

    The available balance (`available` property) is the amount that
    can be withdrawn such that
    a) value of checks not yet cleared cannot be withdrawn, and
    b) the balance after withdraw is at least the minimum balance.

    An account may have a minimum required balance. You can open a
    new account with balance 0 (less than min required balance),
    but you can never withdraw if it would cause the balance to fall
    below the min required balance.

    Checks that have not cleared yet can still be used to satisfy the
    minimum balance requirement.  So, if the minimum required balance
    is 1000 and you deposit 2000 (cash) and 500 (check), you can
    immediately withdraw 1500, since the check contributes 500 to 
    the required balance.

    Example:
    >>> acct = BankAccount("Taksin Shinawat",1000)  # min required balance is 1,000
    >>> acct.balance
    0.0
    >>> acct.available
    0.0
    >>> acct.min_balance
    1000.0
    >>> acct.deposit( Money(10000) )   # deposit 10,000 cash
    >>> acct.balance
    10000.0
    >>> acct.available
    9000.0
    >>> c = Check(40000)
    >>> acct.deposit(c)                # deposit check for 40,000
    >>> acct.balance
    50000.0
    >>> acct.withdraw(30000)           # try to withdraw 30,000
    Traceback (most recent call last):
       ...2
    ValueError: Amount exceeds available balance
    >>> acct.clear_check(c)
    >>> acct.available                 # now the check value is available
    49000.0
    >>> acct.withdraw(30000)           # withdraw 30,000 should work
    Money(30000, 'Baht')
    >>> acct.balance
    20000.0
    >>> acct.withdraw(20000)           # try to withdraw EVERYTHING
    Traceback (most recent call last):
       ...
    ValueError: Amount exceeds available balance
    >>> acct.withdraw(15000)
    Money(15000, 'Baht')
    >>> acct.balance
    5000.0
    """

    def __init__(self, name: str, min_balance: float = 0.0):
        """Create a new account with given name.

        Args:
            name - the name for this account
            min_balance - the minimum required balance, a non-negative number.
                Default min balance is zero.
        """
        # you don't need to test min_balance < 0. It's too trivial.
        assert min_balance >= 0, "min balance parameter must not be negative"
        self.__name = name
        self.__balance = 0.0
        self.__min_balance = float(min_balance)
        # checks deposited and waiting to be cleared
        self.__pending_checks = []

    @property
    def balance(self) -> float:
        """Balance in the account (float) as a value without a currency."""
        return self.__balance

    @property
    def available(self) -> float:
        """Available balance in this account (float), read-only."""
        sum_holds = sum(check.value for check in self.__pending_checks)
        avail = self.balance - self.min_balance - sum_holds
        return avail if (avail > 0) else 0.0

    @property
    def min_balance(self) -> float:
        """Minimum required balance for this account, as a number."""
        return self.__min_balance

    @property
    def account_name(self):
        """The account name."""
        return self.__name

    def deposit(self, money: Money):
        """Deposit money or check into the bank account.

        Arguments:
            money - Money or Check object with a positive value.
        Throws:
            ValueError if value of money parameter is not positive.
        """
        if money.value <= 0:
            raise ValueError("Cannot deposit a negative amount")
        # if it is a check, verify the check was not already deposited
        if isinstance(money, Check):
            # looks like a check
            if money in self.__pending_checks:
                raise ValueError("Check already deposited")
            else:
                # add to list of checking waiting to clear
                self.__pending_checks.append(money)
        # both cash and checks contribute to the balance
        self.__balance += money.value

    def clear_check(self, check: Check):
        """Mark a check as cleared so it is available for withdraw.

        Arguments:
            check - reference to a previously deposited check.

        Throws:
            ValueError if the check is not in the list of uncleared checks
        """
        if check in self.__pending_checks:
            self.__pending_checks.remove(check)

    def withdraw(self, amount: float) -> Money:
        """
        Withdraw an amount from the account.

        Args:
            amount - (number) the amount to withdraw,
                     at most the available balance
        Returns:
            a Money object for the amount requested.
        Throws:
             ValueError if amount exceeds available balance or is not positive.
        """
        if amount <= 0:
            raise ValueError("Amount to withdraw must be positive")
        if amount >= self.available:
            raise ValueError(f"Amount exceeds available balance")
        # try to create the money before deducting from balance,
        # in case Money throws an exception.
        m = Money(amount)
        self.__balance -= amount
        return m

    def __str__(self):
        """String representation of the bank account.
           Includes the acct name but not the balance.
        """
        return f"{self.account_name} Account"

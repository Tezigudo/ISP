"""Unit tests of the Bank Account class."""
import unittest
from bank_account import BankAccount, Check
from money import Money


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        """Create test fixtures for use in tests."""
        # account with 0 minimum balance
        self.account = BankAccount('Ted')
        # account with 599 minimum balance
        self.account1 = BankAccount('Nij', 500)

    def test_deposit_cash(self):
        """Test deposit correctly adds to balance."""
        # a new account should have 0 balance
        self.assertEqual(0.0, self.account.balance)
        total = 0
        for amount in [0.1, 1, 1000]:
            total += amount
            self.account.deposit(Money(amount))
            self.assertEqual(total, self.account.balance)

    def test_withdraw(self):
        """You can withdraw anything up to the balance from account."""
        self.account.deposit(Money(1000))
        # withdraw a tiny value
        amount = self.account.withdraw(1.0)
        self.assertEqual(1.0, amount.value)
        self.assertEqual(999.0, self.account.balance)
        # withdraw more
        amount = self.account.withdraw(900.0)
        self.assertEqual(900.0, amount.value)
        self.assertEqual(99, self.account.balance)

    def test_withdraw_invalid_amount(self):
        """You cannot withdraw more than the balance of account
        or withdraw negative value"""
        self.account.deposit(Money(100))
        with self.assertRaises(ValueError):
            # you have 100 then withdraw 900 it wont work
            self.account.withdraw(900)

        # you cant withdraw negative value
        with self.assertRaises(ValueError):
            self.account.withdraw(-1)

    def test_withdraw_check(self):
        """you cannot withdraw money and check that isnt cleared"""
        some_check = Check(1000)
        just_another_check = Check(200)
        self.account.deposit(some_check)
        with self.assertRaises(ValueError):
            self.account.withdraw(500)

        with self.assertRaises(ValueError):
            self.account.clear_check(just_another_check)

        self.account.clear_check(some_check)
        self.account.withdraw(500)
        self.assertEqual(500, self.account.balance)

    def test_deposit_invalid_amout(self):
        """you cannot deposit zero amount or negative value"""
        # you deposit zero baht it mean nothing
        with self.assertRaises(ValueError):
            self.account.deposit(Money(0))

        # you cant deposit negative value
        with self.assertRaises(ValueError):
            self.account.deposit(Money(-1))

    def test_withdraw_more_than_min_balance(self):
        """withdraw more than min balance it must raise ValueError"""
        self.account1.deposit(Money(600))
        with self.assertRaises(ValueError):
            self.account1.withdraw(300)

    def test_invalid_check_deposit(self):
        """testing that deposit the same check will ERROR"""
        some_check = Check(200)
        self.account.deposit(some_check)

        with self.assertRaises(ValueError):
            self.account.deposit(some_check)

    def test_available(self):
        """testing different between available and balance"""
        some_check = Check(1000)
        self.account1.deposit(some_check)
        self.account1.deposit(Money(300))
        self.assertEqual(300, self.account1.available)
        self.assertEqual(1300, self.account1.balance)

        self.account1.withdraw(300)

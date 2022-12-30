"""Test of the Tax Calculator.

Adaptors to Reduce Refactoring Work:

These tests call utility methods getTax() and addIncome() at the bottom of this file,
instead of calling TaxCalculator methods directly. None of the test methods call the
TaxCalculator directly, except setUp which creates a TaxCalculator.
When you refactor you modify the utility methods and (maybe) setUp.
Design Principle:  use indirection to isolate coupling between classes.

Usage:  python -m unittest [-v]
"""
import sys

import unittest
from person import Person
from tax_calculator import *

# The kinds of income. You can change the values of these constants.
ORDINARY = "wages"
INTEREST = "interest"
DIVIDEND = "dividend"


class TestTaxCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # The starter code prints a LOT of output on the console,
        # which makes reading the unittest output difficult.
        # So, temporarily redirect standard output to a file.
        # Error messages from unittest are printed to stderr
        # so they will still print on the console.
        cls.stdout = sys.stdout
        sys.stdout = open("output.txt", "w")

    @classmethod
    def tearDownClass(cls):
        # Restore stdout to the console.
        sys.stdout.close()  # close the file to avoid a warning message
        sys.stdout = cls.stdout

    def setUp(self):
        person = Person("1234567890123", "Joe", "Testcase")
        self.tc = TaxCalculator(person.id, person.first_name, person.last_name)
        # the personal deduction for ordinary income
        self.deduction = 60000

    def test_low_income_pays_zero_tax(self):
        """Tax on no income or low income should be zero."""
        self.assertEqual(0, self.getTax())
        self.addIncome(ORDINARY, "KU", 100000, 0)
        self.addIncome(ORDINARY, "AIS", 50000, 0)
        self.assertEqual(0, self.getTax())

    def test_tax_on_interest(self):
        """Tax on interest is 15%, but taxpayer can choose to use the ordinary tax formula."""
        self.addIncome(INTEREST, "BBL", 10000, 0)
        self.assertEqual(0, self.getTax())
        self.addIncome(INTEREST, "KTB", 90000, 0)
        # no tax because you can count it as ordinary income (zero tax)
        self.assertEqual(0, self.getTax())
        self.addIncome(INTEREST, "SCB", 360000, 0)
        # now total income is 460,000 Bt, taxable amount 400,000. Should use ordinary tax:
        expect_tax = 0.05 * (150000) + 0.10 * (400000 - 300000)
        self.assertEqual(expect_tax, self.getTax())
        # calculator should switch to interest tax formula (15%) for large interest amount
        self.addIncome(INTEREST, "SCB", 1500000, 0)
        expect_tax = 0.15 * (
            1500000 + 460000 - 20000
        )  # exclude first 20,000 Bt interest
        self.assertEqual(expect_tax, self.getTax())
        # test a HUGE amount of interest
        self.addIncome(INTEREST, "Govt Bond", 10000000, 0)
        expect_tax = 0.15 * (
            10000000 + 1500000 + 460000 - 20000
        )  # exclude first 20,000 Bt
        self.assertEqual(expect_tax, self.getTax())

    def test_tax_on_dividends(self):
        """Tax on dividends is 10% but taxpayer may choose ordinary tax formula.

        This results in lower tax if his total income in low."""
        self.addIncome(DIVIDEND, "payer1", 50000, 0)
        # no tax because you can count it as ordinary income (zero tax)
        self.assertEqual(0, self.getTax())
        self.addIncome(DIVIDEND, "payer2", 50000, 0)
        # still no tax because total income is too low
        self.assertEqual(0, self.getTax())
        self.addIncome(DIVIDEND, "payer3", 300000, 0)
        # now total income is 400,000 Bt. We should owe (using ordinary tax formula):
        taxable_income = 400000 - 60000
        expect_tax = 0.05 * (150000) + 0.10 * (taxable_income - 300000)
        self.assertEqual(expect_tax, self.getTax())
        # should still use ordinary income formula for mid-range amount
        # total income now 700,000
        self.addIncome(DIVIDEND, "payer4", 300000, 0)
        expect_tax = 48500
        self.assertEqual(expect_tax, self.getTax())
        # TaxCalculator should switch to dividend tax calculation if very large dividends
        # because the 10% dividend tax rate is less than ordinary income tax rate.
        self.addIncome(DIVIDEND, "payer5", 300000, 0)  # total now is 1,000,000
        expect_tax = 0.10 * (1000000)
        self.assertEqual(expect_tax, self.getTax())
        # test a very large value
        self.addIncome(DIVIDEND, "really rich", 10000000, 0)
        expect_tax = 0.10 * (1000000 + 10000000)
        self.assertEqual(expect_tax, self.getTax())

    def test_ordinary_income_tax(self):
        """Verify ordinary tax at each tax bracket endpoint is correct."""
        # these are upper end-points of ordinary income tax brackets
        income_and_tax = [
            (150000, 0),
            (300000, 7500),
            (500000, 27500),
            (750000, 65000),
            (1000000, 115000),
            (2000000, 365000),
            (4000000, 965000),
        ]

        # taxable income is total income - personal deduction, so add deduction to test income
        for (income, expected_tax) in income_and_tax:
            self.addIncome(ORDINARY, "payer", income + self.deduction, 0)
            self.assertEqual(
                expected_tax,
                self.getTax(),
                f"Tax on wages {income} should be {expected_tax}",
            )
            # reset test fixture for next test case
            self.setUp()

    def test_ordinary_income_and_deductable_interest(self):
        """Tax on ordinary income when also have some interest."""
        # interest <= 20000 is tax-exempt, so it should never change the total tax
        income_and_tax = [
            (150000, 0),
            (300000, 7500),
            (500000, 27500),
            (750000, 65000),
            (1000000, 115000),
            (2000000, 365000),
        ]
        for interest in (10000, 20000):
            for (ordinary_income, tax) in income_and_tax:
                self.addIncome(ORDINARY, "KU", ordinary_income + self.deduction, 0)
                self.addIncome(INTEREST, "SCB", interest, 0)
                # interest should not affect the tax
                self.assertEqual(
                    tax,
                    self.getTax(),
                    f"Wages {ordinary_income} + interest {interest} should pay tax {tax}",
                )
                # reset test fixture for next test case
                self.setUp()

    def test_ordinary_income_and_large_interest(self):
        """Interest income is large and person also has ordinary income, should pay 15% tax on interest."""
        self.addIncome(ORDINARY, "KU", 900000, 0)  # margin tax rate is 20%
        expect_tax = self.getTax()
        self.addIncome(INTEREST, "SCB", 50000, 0)
        expect_tax += 0.15 * (50000 - 20000)
        self.assertEqual(expect_tax, self.getTax())
        # add another interest income, should pay interest tax on that, too
        self.addIncome(INTEREST, "KTB", 40000, 0)
        expect_tax += 0.15 * 40000
        self.assertEqual(expect_tax, self.getTax())

    def test_ordinary_income_and_dividends(self):
        """Tax on ordinary income and dividends uses whichever calculation is lower."""
        income_and_tax = [
            (150000, 0),
            (300000, 7500),
            (500000, 27500),
            (750000, 65000),
            (1000000, 115000),
        ]
        dividend = 80000
        for (ordinary_income, tax) in income_and_tax:
            self.addIncome(ORDINARY, "KU", ordinary_income + self.deduction, 0)
            self.addIncome(DIVIDEND, "SCB", dividend, 0)
            if ordinary_income + dividend <= 300000:
                # should include dividend as ordinary income, pay 5% tax
                expected_tax = tax + 0.05 * dividend
            else:
                # should use the 10% dividend tax rate
                expected_tax = tax + 0.10 * dividend
            self.assertEqual(
                expected_tax,
                self.getTax(),
                f"Wages {ordinary_income} + dividend {dividend} should pay tax {expected_tax}",
            )
            # reset fixture for next test case
            self.setUp()

    def test_ordinary_income_and_large_dividends(self):
        """If total dividend is large then should always use 10% dividend tax rate."""
        income_and_tax = [
            (150000, 0),
            (300000, 7500),
            (500000, 27500),
            (750000, 65000),
            (1000000, 115000),
        ]
        dividend = 600000
        for (ordinary_income, tax) in income_and_tax:
            self.addIncome(ORDINARY, "KU", ordinary_income + self.deduction, 0)
            self.addIncome(DIVIDEND, "SCB", dividend, 0)
            # should use the 10% dividend tax rate
            expected_tax = tax + 0.10 * dividend
            self.assertEqual(
                expected_tax,
                self.getTax(),
                f"Wages {ordinary_income} + dividend {dividend} should pay tax {expected_tax}",
            )
            # reset fixture for next test case
            self.setUp()

    def test_tax_withholding(self):
        """Tax withholdings are deducted from the amount of tax due."""
        ordinary_income = 460000  # tax should be 17,500
        ordinary_tax_paid = 14000
        self.addIncome(ORDINARY, "KU", ordinary_income, ordinary_tax_paid)
        tax_owed = 17500 - 14000
        self.assertEqual(tax_owed, self.getTax())
        self.addIncome(DIVIDEND, "TSD", 200000, 10000)  # tax should be 20,000
        tax_owed += 20000 - 10000
        self.assertEqual(tax_owed, self.getTax())

        # KU pays additional income and this time witholds EXTRA tax
        # so the taxpayer's net liability is zero.
        # taxed at a 10% marginal rate (after 60,000 deduction)
        more_income = 50000
        more_tax_withheld = 0.10 * 50000 + tax_owed
        self.addIncome(ORDINARY, "KU2", more_income, more_tax_withheld)
        # so now he show owe no more tax
        self.assertEqual(0, self.getTax())

    def test_tax_over_withholding(self):
        """If too much tax withheld (tax_wh) then the taxpayer should get a refund."""
        interest_income = 20000  # first 20,000 Bt of interest pays 0 tax
        interest_tax_wh = 3000
        self.addIncome(INTEREST, "Bank", interest_income, interest_tax_wh)
        # No tax on interest <= 20,000, so all tax should be refunded
        tax_owed = -interest_tax_wh
        self.assertEqual(tax_owed, self.getTax())
        ordinary_income = 360000  # tax should be 7,500
        ordinary_tax_wd = 6000
        tax_owed += 7500 - 6000
        self.addIncome(ORDINARY, "KU", ordinary_income, ordinary_tax_wd)
        self.assertEqual(tax_owed, self.getTax(), f"Tax due should be {tax_owed}")

    ############################# Utility Methods ###############################

    def getTax(self):
        """Utility method to shorten call to compute_and_print_tax()
           and simplify refactoring.

        :returns: the amount of tax owed (if > 0) or amount to refund (if < 0)
        """
        # Change this when you refactor the method in TaxCalculator
        return self.tc.get_tax_owe_or_refund()

    def addIncome(self, income_type, description, amount, tax_withheld):
        """Utility method to simplify refactoring of add_income()."""
        # Change this when you apply your refactoring for parameter object.
        income = Income(income_type, description, amount, tax_withheld)
        self.tc.add_income(income)

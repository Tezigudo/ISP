"""Income tax calculator for Thai income tax."""
from typing import List

from dataclasses import dataclass


@dataclass(frozen=True)
class Income:
    """Data class for an Income item with immutable income_type, description,"""

    income_type: str
    description: str
    amount: int
    tax_withheld: int

    def get_data(self):
        """Return the income item as a tuple."""
        return (self.income_type, self.amount, self.tax_withheld)


class TaxCalculator:
    def __init__(self, taxpayer_id, first_name, last_name):
        """Initialize income tax calculator.

        :param taypayer_id: tax id of the tax payer.
        :param first_name: first name of the tax payer.
        :param last_name:  last name of the tax payer
        """
        self.tax_id = taxpayer_id
        self.first_name = first_name
        self.last_name = last_name
        # incomes is a list of income items.
        # Each income item is a tuple of values.
        # See add_income for details.
        self.incomes: List[Income] = []

    def add_income(self, income: Income):
        """Record an income item.

        :param income_type: the type of income,
                            should be "wages", "interest", or "dividend"
        :param description: describes source of income (company, person, business)
        :param amount: the total amount of income (including tax withheld)
        :param tax_withheld: amount of tax withheld by the source

        Income items are saved as a tuple: (income_type, desc, amount, tax_withheld)
        """
        self.incomes.append(income)

    @property
    def total_income(self):
        """The person's total income."""
        return sum(income.amount for income in self.incomes)

    def get_income(self):
        income_dct = {"wages": 0, "interest": 0, "dividend": 0}
        for income in self.incomes:
            income_dct[income.income_type] += income.amount
        return income_dct.values()

    def get_tax(self):
        tax_dct = {"wages": 0, "interest": 0, "dividend": 0}
        for income in self.incomes:
            tax_dct[income.income_type] += income.tax_withheld
        return tax_dct.values()

    def income_tax(self, deducted_income: int):
        "get a deducted income"
        if deducted_income <= 150000:
            return 0
        if deducted_income <= 300000:
            return 0.05 * (deducted_income - 150000)
        if deducted_income <= 500000:
            return 7500 + 0.10 * (deducted_income - 300000)
        if deducted_income <= 750000:
            return 27500 + 0.15 * (deducted_income - 500000)
        if deducted_income <= 1000000:
            return 65000 + 0.20 * (deducted_income - 750000)
        if deducted_income <= 2000000:
            return 115000 + 0.25 * (deducted_income - 1000000)
        if deducted_income <= 4000000:
            return 365000 + 0.30 * (deducted_income - 2000000)
        # net income over 4,000,000
        return 965000 + 0.35 * (deducted_income - 4000000)

    def get_income_and_tax(self, income_type):
        income = 0
        tax = 0
        filtered_incomes = filter(lambda i: i.income_type == income_type, self.incomes)
        for income_item in filtered_incomes:
            income += income_item.amount
            tax += income_item.tax_withheld

        return income, tax

    def compute_tax(self):
        """Compute income tax, the amount due or refund, and print everything.

        :return: the amount of tax due (> 0) or amount to refund (if <= 0).
        """

        ordinary_income, interest_income, dividend_income = self.get_income()
        (
            ordinary_tax_withheld,
            interest_tax_withheld,
            dividend_tax_withheld,
        ) = self.get_tax()

        # we need to know the total of all taxes paid, so sum them
        total_tax_withheld = (
            ordinary_tax_withheld + interest_tax_withheld + dividend_tax_withheld
        )

        # Compute the income tax on net ordinary income (wages),
        # which is the sum of wages/salary minus a personal exemption.
        # Each person gets a 60,000 Baht personal exemption (deduction).
        # The personal exemption may change in the future.
        deduction = 60000
        ordinary_income_tax = self.income_tax(ordinary_income - deduction)

        # Compute the tax on interest income.
        # First 20,000 Baht pays 0 tax, above 20,000 the tax is 15%.
        interest_tax = 0.15 * max(0, interest_income - 20000)

        # Compute the tax on dividend income.
        # The tax is a 10% fixed rate.
        dividend_tax = 0.10 * dividend_income

        # Special case:
        # A person can treat dividend and/or interest income as ordinary income
        # and pay the tax on ordinary income, if it results in a lower total tax.
        # (For example, if a person's income is in the 5% tax bracket.)

        # Add the income types and recompute the tax as ordinary income.
        # Then choose the one with lower tax liability.

        all_income = ordinary_income + dividend_income
        # Only include interest income if interest income > 20,000
        # since interest <= 20,000 Bt is not taxed using the interest-tax formula.
        if interest_income > 20000:
            all_income += interest_income

        # Apply the ordinary tax formula (same as above) to combined income
        all_income_tax = self.income_tax(all_income - deduction)

        # Choose the tax computation that results in the lower tax.
        # a) add tax on separate income types ordinary, dividends, and interest
        # b) combine all incomes and compute ordinary tax on the combined income

        total_tax = ordinary_income_tax + interest_tax + dividend_tax

        separate_income_types = total_tax <= all_income_tax
        # use the tax computed separately on each income category

        return separate_income_types, total_tax, total_tax_withheld, all_income_tax

    def get_tax_owe_or_refund(self):
        (
            separate_income_types,
            total_tax,
            total_tax_withheld,
            all_income_tax,
        ) = self.compute_tax()

        if separate_income_types:
            return total_tax - total_tax_withheld
        else:
            return all_income_tax - total_tax_withheld

    def print_tax(self):
        FORMAT1 = "{:40s} {:12,.2f} {:12,.2f}"
        FORMAT2 = "{:40s} {:12,.2f}"
        income_type_dct = {
            "wages": "Ordinary",
            "interest": "Interest",
            "dividend": "Dividend",
        }
        (
            separate_income_types,
            total_tax,
            total_tax_withheld,
            all_income_tax,
        ) = self.compute_tax()
        print(
            f"Tax Report for {self.first_name} {self.last_name}, Tax Id {self.tax_id}"
        )
        print("-" * 68)
        print(
            "{:40s} {:12s} {:12s}".format("Income Type", "Total Amount", "Tax Withheld")
        )
        for income_type, topic in income_type_dct.items():
            income, tax_withheld = self.get_income_and_tax(income_type)
            topic += " Income"
            print(FORMAT1.format(topic, income, tax_withheld))

        if separate_income_types:
            print(
                FORMAT1.format(
                    "Total Tax & Total Tax Withheld", total_tax, total_tax_withheld
                )
            )
            print()
            # Does he get a tax refund or owe additional tax?
            if total_tax > total_tax_withheld:
                # tax owed = total taxes - total tax withheld
                print(
                    FORMAT2.format("Amount of Tax Owed", total_tax - total_tax_withheld)
                )
            else:
                # tax refund = total tax withheld - total tax
                print(
                    FORMAT2.format(
                        "Amount of Tax Overpaid", total_tax_withheld - total_tax
                    )
                )
        else:
            print(
                FORMAT1.format(
                    "Total Tax & Total Tax Withheld", all_income_tax, total_tax_withheld
                )
            )
            print()
            # Does he get a tax refund or owe additional tax?
            if all_income_tax > total_tax_withheld:
                print(
                    FORMAT2.format(
                        "Amount of Tax Owed", all_income_tax - total_tax_withheld
                    )
                )
            else:
                print(
                    FORMAT2.format(
                        "Amount of Tax Overpaid", total_tax_withheld - all_income_tax
                    )
                )

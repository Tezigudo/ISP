"""Demonstrate use of Income Tax Calculator."""
from tax_calculator import *

if __name__ == "__main__":
    tax_calc = TaxCalculator("1409900123456", "Fatalai", "Jon")
    fatalai_income_tup = (
        Income("wages", "Kasetsart University", 290000, 10000),
        Income("interest", "Bangkok Bank", 12000, 0),
        Income("dividend", "TSD Corp", 15000, 1500),
    )
    for income in fatalai_income_tup:
        tax_calc.add_income(income)
    tax_calc.print_tax()
    tax_due = tax_calc.get_tax_owe_or_refund()

    if tax_due > 0:
        print(f"You owe {tax_due:,.2f} Baht additional tax. Sorry.")
    else:
        print(f"Good news! You get a tax refund of {-tax_due:,.2f}.")

    print("")
    big_tax = TaxCalculator("3409900565656", "Taksin", "Shinawat")
    taksin_income_tup = (
        Income("wages", "CEO salary", 8000000, 0),
        Income("dividend", "AIS", 4000000, 400000),
        Income("dividend", "Intouch", 4000000, 400000),
        Income("interest", "Bank of Dubai", 2000000, 0),
    )
    for income in taksin_income_tup:
        big_tax.add_income(income)
    big_tax.print_tax()
    tax_due = big_tax.get_tax_owe_or_refund()

    if tax_due > 0:
        print(f"Sorry, you owe {tax_due:,.2f} Baht additional tax.")
    else:
        print(f"Good news! You get a tax refund of {-tax_due:,.2f}.")

    tax_calc = TaxCalculator("0" * 13, "Test", "Taxpayer")

    # example where too much tax is withheld. Should get a refund
    tc = TaxCalculator("8" * 13, "Joe", "Taxpayer")
    joe_income_tup = (
        Income("interest", "Bank", 20000, 3000),
        Income("wages", "KU", 360000, 6000),
    )

    for income in joe_income_tup:
        tc.add_income(income)

    tc.print_tax()

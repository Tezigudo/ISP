## Tax Calculator 

## Test Code

`test_tax_calculator.py` contains unit tests that should all pass.

When you refactor `tax_calculator`, some refactorings require a 
change in `test_tax_calculator`, too.  The test code is written so
that you should need to make changes only in these places

- `getTax()` - calls `tax_calculator.compute_and_print_tax` to get the tax due and returns it
- `addIncome()` - calls `tax_calculator.add_income`.
- 3 constants - there are 3 constants at the top of the test code. When you refactor, change the **value** assigned to these constants, but don't eliminate the constants, which would require changes in many test methods.
- `setUp()` - creates a TaxCalculator, so if you modify the constructor to TaxCalculator, make a change in `setUp`, too.

None of the test methods *directly* invoke the TaxCalculator methods, so you should not need to modify the test methods when you refactor.


## Types of Income and Tax Rates

There are 3 kinds of income: "wages" (including salary), "dividend",  and "interest".

| Income type | Tax                                        |
|-------------|--------------------------------------------|
| Wages       | 0 - 35% (see table below).                 |
| Interest    | 0 for first 20,000, 15% of amount > 20,000 |
| Dividend    | 10% tax on all dividends                   |

## Tax Rates for Ordinary Income

Ordinary income means 'wages'. (In reality it would also include "salary" and "other" income.)  
The tax is computed on "net income" which is ordinary income minus a 60,000 Bt personal exemption (a deduction).

The tax on *net ordinary income* is:

| Net ordinary income | Tax Rate        |
|--------------------|-----------------|
| 0 - 150,000        | zero            |
| 150,000 - 300,000  | 5% of amount above 150,000 |
| 300,000 - 500,000  | 7,500 + 10% of amount above 300,000 |
| 500,000 - 750,000  |27,500 + 15% of amount above 500,000 |
| 750,000 - 1,000,000 | 65,000 + 20% of amount above 1,000,000 |
| 1,000,000 - 2,000,000 | 115,000 + 25% of amount above 1,000,000 |
| 2,000,000 - 4,000,000 | 365,000 + 30% of amount above 2,000,000 |
| more than 4,000,000 | 965,000 + 35% of amount above 2,000,000 |

You have two choices for how to compute income tax. You can use whichever one results in the smallest tax.

1. Separately compute tax on ordinary income, interest, and dividends using the 3 different formulas. Sum the taxes to get your total tax.
2. Count interest and/or dividends as "ordinary income". Compute the tax using the formula for ordinary income applied to this combined income.  If you include interest income, then *all* interest is taxed (no 20,000 Bt exclusion).

If your interest income is <= 20,000 then you should always use the separate tax formula for "interest", since there is no tax on interest <= 20,000 Baht. 

## Example

Fatalai Jon has the following income:

- wages    290,000 Bt
- interest  30,000 Bt
- dividend  15,000 Bt

He gets a 60,000 Baht deduction from wage income.
His *taxable ordinary income* is 290,000 - 60,000 = 230,000.

Using the basic tax formula:
```
tax on net income: 5%*(230000 - 150000) = 4,000
tax on interest:   15%*(30000 - 20000)  = 1,500
tax on dividend:   10%*15,000           = 1,500
Total tax liability:                      7,000
```

Since his tax rate on ordinary income is low (5%) he should try the 
option to count all income as "ordinary income" and see if that reduces his tax:
```
ordinary income      290,000
interest income       30,000  (pay tax on the entire amount)
dividend income       15,000
----------------------------
total income         335,000
personal exemption -  60,000
Net taxable income   275,000

Ordinary income tax: 5% * (275,000 - 150,000) = 6,250
```

Good news!  His tax is only 6,250 Baht.

If his interest income was 20,000 (instead of 30,000) then he should count it as "interest" (no tax on 20,000) and only include dividends in ordinary income. 

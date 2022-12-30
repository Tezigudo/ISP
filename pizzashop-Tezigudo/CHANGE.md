## Change in Pizza Pricing

Do this **after** you finish and test all refactorings in README.md.

## Change in Pizza Prices

The Pizza Shop wants to change the large pizza and topping prices as follows:

| Pizza Size  | Base Price | Price Per Topping  |
|-------------|------------|-------------|
| small       | 120        | 20 Bt.      |
| medium      | 200        | 25 Bt.      |
| large       | 300        | 30 Bt.      |

How would you implement this change?

There are many ways. One solution is to add the per-topping price to PizzaSize.

## Enum with attributes

The value of an Enum member can be *anything*, not just a number. We can set it to a dictionary of attributes for the base price and topping price:
```python
class PizzaSize(Enum):
    small =  {'base_price': 120, 'topping': 20}
    medium = {'base_price': 200, 'topping': 25}
    large =  {'base_price': 300, 'topping': 30}

    @property
    def price(self):
        return self.value['base_price']
    
    @property
    def topping_price(self):
        return self.value['topping']
```

and in Pizza.get_price:
```python
   def get_price(self):
       return self.size.price + self.size.topping_price*len(self.toppings)
```

### Benefit of Encapsulation

When the Pizza Shop changes prices, the change to the code is localized: just update the prices in PizzaSize.

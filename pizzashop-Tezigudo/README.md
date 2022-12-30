## Refactoring Practice

Make some improvements in the Pizza class and pizzashop file by refactoring. 

Goals to achieve for the code are:

1. Replace string literals with named constants.
2. Rename methods to use the Python naming convention.
3. Move misplaced code to a better place (Extract Method and then Move Method). This improves encapsulation and makes the code more reusable.
4. Replace "switch" (`if` ... `elif` ... `elif`) with object behavior.

### Background

Pizza describes a pizza with a size and optional toppings.  The price depends on size and number of toppings.  For example, large pizza is 280 Baht plus 20 Baht per topping.
```python
pizza = Pizza('large')
pizza.addTopping("mushroom")
pizza.addtopping("pineapple")
print("The price is", pizza.getPrice())
'The price is 320'
```
There are 2 files to start with:
```
pizza.py     - code for Pizza class
pizzashop.py - create some pizzas and print them. Use to verify code.
```

## 1. Replace String Literals with Named Constants

> Use Named Constants instead of Literals in Code.

In the Pizza class replace 'small', 'medium', and 'large" with named constants.  Use your IDE's refactoring feature, not manual find and replace.

1. Select 'small' in Pizza.
   - VSCode: right click -> Refactor -> Extract variable.
   - Pycharm: right click -> Refactor -> Introduce Constant. **Preview** changes.
   - Pydev: Refactoring -> Extract local variable. 

2. Do the same thing for "medium" and "large".

3. In my tests, none of the IDE did exactly what I want.  The constants SMALL, MEDIUM, and LARGE are top-level variables in `pizza.py`, but not part of the Pizza class.    
   ```python
   SMALL = 'small'
   MEDIUM = 'medium'
   LARGE = 'large'

   class Pizza:
       ...
   ```
   I would prefer to *encapsulate* the sizes inside the Pizza class, e.g. `Pizza.SMALL`. However, we will eventually replace these constants with an enum, so *leave the constants as top-level variables* for now.

5. Did the IDE also change the sizes in `pizzashop.py`?  If not, edit pizzashop.py and change sizes to references (`SMALL`)
    ```python
    from pizza import *

    if __name__ == "__main__":
        pizza = make_pizza(SMALL)
        ...
        pizza2 = Pizza(MEDIUM)
        ...
        pizza3 = make_pizza(LARGE)
    ```    
    
7. Run the code. Verify the results are the same.

## 2. Rename Method

1. `getPrice` is not a Python-style name.  Use refactoring to rename it to `get_price`.
    - VSCode: right-click on method name, choose "Rename Symbol"
    - Pycharm: right-click, Refactor -> Rename, **Preview** changes.
    - Pydev: "Refactoring" menu -> Rename

2. Did the IDE **also** rename `getPrice` in `order_pizza()`?
    - VSCode: no
    - Pycharm: yes. Notification of dynamic code in preview.
    - Pydev: yes (lucky guess)
    - This is a limitation of tools for dynamic languages. The tool can't be *sure* that the "pizza" parameter in `order_pizza` is *really* a Pizza.  To help it, use type annotations.

3. Undo the refactoring, so you have original `getPrice`.

4. Add a type annotation in pizzashop.py so the IDE knows that parameter is *really* a Pizza: 
   ```python
   def order_pizza(pizza: Pizza):
   ```
    - Save the change in pizzashop.py
    - Then, in `pizza.py` do Refactoring -> Rename again.
    - Does the IDE also change `getPrice` to `get_price` in pizzashop.py?

5. Rename `addTopping` in Pizza to `add_topping`.  Did the IDE also rename it in pizzashop?
    - If not, rename it manually.
    - In this case, a smart IDE *can* infer that `addTopping` in pizzashop refers to Pizza.addTopping. Why?

6. Run the code. Verify the code works the same.


## 3. Extract Method and Move Method

> Perform refactorings in small steps. 
> In this case, we extract a method first, then move it to a better place.

`order_pizza` creates a string `description` to describe the pizza.  That is a poor location for this because:
1. the description could be needed elsewhere in the application
2. it relies on info about a Pizza that only the Pizza knows.

Therefore, it should be the Pizza's job to describe itself.  This is also known as the *Information Expert* principle.

Try an *Extract Method* refactoring, followed by *Move Method*.

1. **Select** these statements in `order_pizza` that create the description:
   ```python
    description = pizza.size
    if pizza.toppings:
        description += " pizza with "+ ", ".join(pizza.toppings)
    else:
        description += " plain pizza"
    ```
2. Refactor (**Extract Method**):
    - VS Code: right click -> 'Extract Method'. Enter "describe" as method name. (This worked in 2020, but in current VS Code it does not.)
    - PyCharm: right click -> Refactor -> Extract -> Method
    - PyCharm correctly suggests that "pizza" should be parameter, and it returns the description. (correct!)
    - PyDev: Refactoring menu -> Extract method.  PyDev asks you if pizza should a parameter (correct), but the new method does not return anything.  Fix it.
    - All IDE: after refactoring, move the two comment lines from `order_pizza` to `describe` as shown here:
    ```python
    def describe(pizza):
        # create printable description of the pizza such as
        # "small pizza with muschroom" or "small plain pizza"
        description = pizza.size
        if pizza.toppings:
            description += " pizza with "+ ", ".join(pizza.toppings)
        else:
            description += " plain pizza"
        return description
    ```
    Forgetting to move comments is a common problem in refactoring. Be careful.

3. **Move Method:** The code for `describe()` should be a method in the Pizza class, so it can be used anywhere that we have a pizza.
   - Select the method. Does the IDE "Refactoring" menu have a "Move Method" refactoring?
   - None of the 3 IDE do this correctly (for me), so do it manually.
   - Select the `describe(pizza)` method in pizzashop.py and CUT it.
   - Inside the Pizza class (pizza.py), PASTE the method.
   - Change the parameter name from "pizza" to "self" (Refactor -> Rename).
   
4. **Rename Method:** In `pizza.py` rename `describe` to `__str__(self)` method. You should end up with this:
    ```python
    # In Pizza class:
    def __str__(self):
        # create printable description of the pizza such as
        # "small pizza with muschroom" or "small plain pizza"
        description = self.size
        if self.toppings:
            description += " pizza with "+ ", ".join(self.toppings)
        else:
            description += " plain cheese pizza"
        return description
    ```
4. Back in `pizzashop.py`, modify the `order_pizza` to get the description from Pizza:
    ```python
    def order_pizza(pizza):
        description = str(pizza)
        print(f"A {descripton}")
        print("Price:", pizza.get_price())
    ```
5. **Eliminate Temp Variable** The code is now so simple that we don't need the `description` variable.  Eliminate it:
    ```python
    def order_pizza(pizza)
        print(f"A {str(pizza)}")
        print("Price:", pizza.get_price())
    ```
6. **Test.** Run the pizzashop code. Verify the results are the same.


## 4. Replace 'switch' with Call to Object Method

This is the most complex refactoring, but it gives big gains in code quality:
- code is simpler
- enables us to validate the pizza size in constructor
- prices and sizes can be changed or added without changing the Pizza class

The `get_price` method has a block like this:
```python
if self.size == SMALL:
    price = ...
elif self.size == MEDIUM:
    price = ...
elif self.size == LARGE:
    price = ...
```
The pizza has to know the pricing rule for each size, which makes the code complex.
An O-O approach is to let the pizza sizes compute their own price.
Therefore, we will define a new datatype (class) for pizza size.

Python has an `Enum` type for this.
An "enum" is a type with a fixed set of values, which are static instances of the enum type.  Each enum member has a **name** and a **value**.

1. In `pizza.py` replace the named constants LARGE, MEDIUM, and SMALL with an Enum named `PizzaSize`:
   ```python
   from enum import Enum

   class PizzaSize(Enum):
       # Enum members written as: name = value
       small = 120
       medium = 200
       large = 280

       def __str__(self):
           return self.name
   ```
2. Write a short script (in pizza.py or another file) to test the enum:
   ```python
   if __name__ == "__main__":
       # test the PizzaSize enum
       for size in PizzaSize:
           print(size.name, "pizza has price", size.value)
   ```
   This should print the pizza prices. But the code `size.value` doesn't convey it's meaning: it should be the price. but the **meaning** of `size.value` is **not clear**.  Add a `price` property to PizzaSize:
   ```python
   # PizzaSize
       @property
       def price(self):
           return self.value
   ```
3. In Pizza.get_price(), eliminate the `if size == SMALL: elif ...` It is no longer needed.  The Pizza sizes know their own price.
   ```python
   def get_price(self):
       """Price of a pizza depends on size and number of toppings"""
       price = self.size.price + 20*len(self.toppings)
   ```
4. In `pizzashop.py` replace the constants SMALL, MEDIUM, and LARGE with `PizzaSize.small`, `PizzaSize.medium`, etc.

5. Run the code. It should work as before. If not, fix any


### Extensibility

Can you add a new pizza size *without* changing the Pizza class?
```python
class PizzaSize(Enum):
    ...
    jumbo = 450

# and in pizzashop.__main__:
pizza = Pizza(PizzaSize.jumbo)
```

### Type Safety

Using an Enum instead of Strings for named values reduces the chance for error in creating a pizza, such as `Pizza("LARGE")`.

For type safety, you can add an annotation and a type check in the Pizza constructor:
```python
    def __init__(self, size: PizzaSize):
        if not isinstance(size, PizzaSize):
            raise TypeError('size must be a PizzaSize')
        self.size = size
```

## Further Refactoring

What if the price of each topping is different? 
Maybe "durian" topping costs more than "mushroom" topping.

There are two refactorings for this:

1. *Pass whole object instead of values* - instead of calling `size.price(len(toppings))`, use `size.price(toppings)`.
2. *Delegate to a Strategy* - pricing varies but sizes rarely change, so define a separate class to compute pizza price. 
    (Design principle: "*Separate the parts that vary from the parts that stay the same*")

## References

* The [Refactoring](https://cpske.github.io/ISP/refactoring/) course topic has suggested references.
* *Refactoring: Improving the Design of Existing Code* by Martin Fowler is the bible on refactoring.  The first 4 chapters explain the fundamentals.

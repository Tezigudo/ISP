from pizza import Pizza, PizzaSize

# This example shows the limitations on tool-assisted
# refactoring in a dynamic language like Python.
#
# When you rename the Pizza get_price method to get_price,
# does it rename the method here?
#
# - if no type hint on the pizza parameter, maybe not
# - if you use type hint ':Pizza' on the parameter, it should


def order_pizza(pizza: Pizza):
    """Print a description of a pizza, along with its price."""

    # create printable description of the pizza such as
    # "small pizza with muschroom" or "small plain pizza"
    print(f"A {pizza}")
    print("Price:", pizza.get_price(), "Baht")


def make_pizza(size, *toppings) -> Pizza:
    """Build a pizza with optional toppings.

    :param size: size of the pizza
    :param toppings: optional names of toppings
    :returns: a pizza (of course)
    """
    pizza = Pizza(size)
    for topping in toppings:
        pizza.add_topping(topping)
    return pizza


if __name__ == "__main__":
    # small pizza with 3 toppings
    pizza1 = make_pizza(PizzaSize.small, "mushroom", "pineapple", "tomato")
    order_pizza(pizza1)

    # a plain medium pizza
    pizza2 = Pizza(PizzaSize.medium)
    order_pizza(pizza2)

    # large pizza with one topping
    pizza3 = make_pizza(PizzaSize.large, "seafood")
    order_pizza(pizza3)

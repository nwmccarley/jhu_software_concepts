import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import pytest
from order import Order
from pizza import Pizza
#Test pizza init
@pytest.mark.pizza
def test_pizza_init():
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["mushrooms"])
    assert pizza.crust == "thin"
    assert pizza.sauces == ["marinara"]
    assert pizza.cheese == "mozzarella"
    assert pizza.toppings == ["mushrooms"]
#Test pizza cost
@pytest.mark.pizza
def test_pizza_cost():
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["mushrooms"])
    assert pizza.cost() > 0
#Test pizza str
@pytest.mark.pizza
def test_pizza_str():
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["mushrooms"])
    result = str(pizza)
    assert "thin" in result
    assert "marinara" in result
    assert "mozzarella" in result
    assert "mushrooms" in result
    assert f"${pizza.cost()}" in result
#Test pizza cost with multiple toppings
@pytest.mark.pizza
def test_pizza_cost():
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["pineapple"])
    assert pizza.cost() == 5 + 2 + 1 + 3

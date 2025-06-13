import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import pytest
from order import Order
from pizza import Pizza

@pytest.mark.order
def test_order_init():
    order = Order()
    assert order.pizzas == []
    assert order.total_cost == 0
    assert order.paid is False
#Test oder
@pytest.mark.order
def test_order_str():
    order = Order()
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["mushrooms"])
    order.input_pizza(pizza)
    expected_substring = "mushrooms"
    assert expected_substring in str(order)
    assert f"${pizza.cost()}" in str(order)

@pytest.mark.order
def test_input_pizza_():
    order = Order()
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["mushrooms"])
    cost_before = order.total_cost
    order.input_pizza(pizza)
    assert order.total_cost == cost_before + pizza.cost()
    assert pizza in order.pizzas

@pytest.mark.order
def test_order_paid():
    order = Order()
    assert order.paid is False
    order.order_paid()
    assert order.paid is True

import pytest
from pizza import Pizza
from order import Order

@pytest.mark.order
def test_order_init():
    order = Order()
    assert order.pizzas == []
    assert order.total_cost == 0
    assert order.paid is False

@pytest.mark.order
def test_order_str():
    order = Order()
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["mushrooms"])
    order.input_pizza(pizza)
    expected_substring = "mushrooms"
    assert expected_substring in str(order)
    assert f"${pizza.cost()}" in str(order)

@pytest.mark.order
def test_order_input_pizza_updates_cost():
    order = Order()
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["mushrooms"])
    cost_before = order.total_cost
    order.input_pizza(pizza)
    assert order.total_cost == cost_before + pizza.cost()
    assert pizza in order.pizzas

@pytest.mark.order
def test_order_paid_updates_flag():
    order = Order()
    assert order.paid is False
    order.order_paid()
    assert order.paid is True

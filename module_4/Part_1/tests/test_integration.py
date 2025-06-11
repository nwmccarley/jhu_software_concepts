import pytest
from order import Order
from pizza import Pizza

@pytest.mark.order
@pytest.mark.pizza
def test_multiple_pizzas_total_cost():
    order = Order()

    pizza1 = Pizza("thin", ["pesto"], "mozzarella", ["mushrooms"])
    pizza2 = Pizza("thick", ["marinara"], "mozzarella", ["mushrooms"])

    expected_total = pizza1.cost() + pizza2.cost()

    order.input_pizza(pizza1)
    order.input_pizza(pizza2)

    assert len(order.pizzas) == 2
    assert order.total_cost == expected_total

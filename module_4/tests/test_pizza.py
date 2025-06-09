import pytest
from pizza import Pizza
from order import Order

@pytest.mark.pizza
def test_pizza_init():
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["mushrooms"])
    assert pizza.crust == "thin"
    assert pizza.sauce == ["marinara"]
    assert pizza.cheese == "mozzarella"
    assert pizza.toppings == ["mushrooms"]

@pytest.mark.pizza
def test_pizza_cost_nonzero():
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["mushrooms"])
    assert pizza.cost() > 0

@pytest.mark.pizza
def test_pizza_str_contains_details():
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["mushrooms"])
    result = str(pizza)
    assert "thin" in result
    assert "marinara" in result
    assert "mozzarella" in result
    assert "mushrooms" in result
    assert f"${pizza.cost()}" in result

@pytest.mark.pizza
def test_pizza_cost_correct_calculation():
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["pineapple"])
    # Crust: 5, Marinara: 2, Mozzarella: 1, Pineapple: 3
    assert pizza.cost() == 5 + 2 + 1 + 3

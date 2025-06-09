class Pizza:
    CRUST_PRICES = {
        "thin": 5,
        "thick": 6,
        "gluten_free": 7
    }

    SAUCE_PRICES = {
        "marinara": 2,
        "pesto": 3,
        "liv_sauce": 5
    }

    CHEESE_PRICE = 1  # Only mozzarella is allowed

    TOPPING_PRICES = {
        "mushrooms": 2,
        "pineapple": 3,
        "pepperoni": 3
    }

    def __init__(self, crust, sauce, cheese, toppings):
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings

    def cost(self):
        total = 0
        total += self.CRUST_PRICES.get(self.crust, 0)
        total += sum(self.SAUCE_PRICES.get(s, 0) for s in self.sauce)
        total += self.CHEESE_PRICE if self.cheese == "mozzarella" else 0
        total += sum(self.TOPPING_PRICES.get(t, 0) for t in self.toppings)
        return total

    def __str__(self):
        return (
            f"Pizza with {self.crust} crust, "
            f"sauces: {', '.join(self.sauce)}, "
            f"cheese: {self.cheese}, "
            f"toppings: {', '.join(self.toppings)} "
            f"=> ${self.cost()}"
        )

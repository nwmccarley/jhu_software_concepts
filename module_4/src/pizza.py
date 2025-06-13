class Pizza:
    """
    A class to represent a pizza.

    :ivar crust: The crust of the pizza.
    :ivar sauces: A list of sauces used.
    :ivar cheese: The cheese used.
    :ivar toppings: A list of toppings.
    """

    def __init__(self, crust, sauces, cheese, toppings):
        """
        Initialize a pizza.

        :param crust: Crust type
        :param sauces: List of sauces
        :param cheese: Cheese
        :param toppings: List of toppings
        """
        self.crust = crust
        self.sauces = sauces
        self.cheese = cheese
        self.toppings = toppings

    def cost(self):
        """
        Calculate the total cost of the pizza.

        :return: The total price
        :rtype: float
        """
        prices = {
            "thin": 5,
            "thick": 6,
            "stuffed": 7,
            "marinara": 2,
            "alfredo": 3,
            "mozzarella": 1,
            "cheddar": 1.5,
            "mushrooms": 2,
            "pineapple": 3,
            "pepperoni": 2,
            "sausage": 2.5,
        }

        total = prices.get(self.crust, 0)
        total += sum(prices.get(sauce, 0) for sauce in self.sauces)
        total += prices.get(self.cheese, 0)
        total += sum(prices.get(topping, 0) for topping in self.toppings)

        return total

    def __str__(self):
        """
        Return a string representation of the pizza.

        :return: String description
        :rtype: str
        """
        return (
            f"Crust: {self.crust}, "
            f"Sauces: {', '.join(self.sauces)}, "
            f"Cheese: {self.cheese}, "
            f"Toppings: {', '.join(self.toppings)}, "
            f"Cost: ${self.cost()}"
        )

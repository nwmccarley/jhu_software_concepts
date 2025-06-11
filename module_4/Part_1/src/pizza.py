class Pizza:
    """
    A class to represent a pizza.

    :ivar crust: The crust of the pizza.
    :ivar sauce: A list of sauces used.
    :ivar cheese: The cheese used.
    :ivar toppings: A list of toppings.
    """

    def __init__(self, crust, sauce, cheese, toppings):
        """
        Initialize a pizza.

        :param crust: Crust type
        :param sauce: Sauce(s)
        :param cheese: Cheese
        :param toppings: Toppings
        """
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings

    def cost(self):
        """
        Calculate the total cost of the pizza.

        :return: The total price
        :rtype: float
        """
        total = 0
        return total

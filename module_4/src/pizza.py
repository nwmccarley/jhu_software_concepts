class Pizza:
    """
    A class to house individual pizzas.

    Attributes:
        crust (str): The type of crust.
        sauce (list of str): The sauces used.
        cheese (str): The cheese used (Mozzarella).
        toppings (list of str): Additional toppings.
    """

    def __init__(self, crust, sauce, cheese, toppings):
        """
        Initialize a Pizza with specific crust, sauce, cheese, and toppings.

        Parameters:
            crust (str): The crust of the pizza.
            sauce (list of str): The sauce(s) of the pizza.
            cheese (str): The cheese of the pizza.
            toppings (list of str): The toppings of the pizza.
        """
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings

    def cost(self):
        """
        Determine the cost of the pizza.

        Returns:
            float: Total cost of the pizza.
        """
        total = 0
        # (price logic here)
        return total

class Order:
    """
    A class to house the customer order.

    Attributes:
        pizzas (list): A list of Pizza objects.
        total_cost (float): Total cost of all pizzas in the order.
        paid (bool): Whether the order is marked as paid.
    """

    def __init__(self):
        self.pizzas = []
        self.total_cost = 0
        self.paid = False

    def input_pizza(self, pizza):
        """
        Add a Pizza object to the Order.

        Parameters:
            pizza (Pizza): A pizza to add to the order.
        """
        self.pizzas.append(pizza)
        self.total_cost += pizza.cost()

    def order_paid(self):
        """
        Set the order as paid.
        """
        self.paid = True

class Order:
    """
    A class to house the customer order.

    :ivar pizzas: A list of Pizza objects.
    :ivar total_cost: The total cost of the order.
    :ivar paid: Boolean indicating if the order is paid.
    """

    def __init__(self):
        self.pizzas = []
        self.total_cost = 0
        self.paid = False

    def input_pizza(self, pizza):
        """
        Add a Pizza object to the Order.

        :param pizza: A Pizza object to be added.
        :type pizza: Pizza
        :return: None
        :rtype: None
        """
        self.pizzas.append(pizza)
        self.total_cost += pizza.cost()

    def order_paid(self):
        """
        Set the order as paid.

        :return: None
        :rtype: None
        """
        self.paid = True

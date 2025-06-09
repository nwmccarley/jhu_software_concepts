class Order:
  def __init__(self):
      self.pizzas = []
      self.total_cost = 0
      self.paid = False

  def input_pizza(self, pizza):
      self.pizzas.append(pizza)
      self.total_cost += pizza.cost()

  def order_paid(self):
      self.paid = True

  def __str__(self):
      pizza_descriptions = '\n'.join(str(pizza) for pizza in self.pizzas)
      return f"Order Summary:\n{pizza_descriptions}\nTotal Cost: ${self.total_cost}"

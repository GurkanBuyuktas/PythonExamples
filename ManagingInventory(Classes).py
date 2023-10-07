class Product:
  def __init__(self, name, price, units):
    self.name = name
    self.price = price
    self.units = units
    self.is_on_sale = False
  
  def describe(self):
    print(f"Product name: {self.name}")
    print(f"Product price: {self.price}")
    print(f"Available units: {self.units}")
    print(f"On sale? {self.is_on_sale}")
    print(f"In stock? {self.is_in_stock()}")
    print("-------------------------")

  def add_units(self, units):
    if isinstance(units, int):
        self.units += units
    else:
      print("Cannot add units. Use a correct value.")
      print("-------------------------")

  def reduce_units(self, units):
    if isinstance(units, int):
      if self.units - units >= 0:
        self.units -= units
      else:
        print("Error: Not enough units in inventory.")
    else:
      print("Cannot reduce units. Use a correct value.")
      print("-------------------------")

  def reduce_price(self, discount):
    if discount < 1 and discount > 0:
      self.price = self.price * (1 - discount)
      self.is_on_sale = True
    elif discount < 0:
      print("Error: Discount cannot be negative.")
      print("-------------------------")
    elif discount >= 1:
      print("Error: Discount cannot be more than 99%.")
      print("-------------------------")

  def is_in_stock(self):
    if self.units > 0:
      return True
    else:
      return False

laptop = Product("Dell Laptop", 850, 12)
laptop.describe()



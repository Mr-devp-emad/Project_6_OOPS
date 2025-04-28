class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        print("Getting the price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            print("Setting the price...")
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

# Create an object of Product
p = Product(200)

# Access the price
print(p.price)

# Update the price
p.price = 250
print(p.price)

# Try to set a negative price
p.price = -50

# Delete the price
del p.price

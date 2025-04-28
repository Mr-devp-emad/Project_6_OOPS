class Car:
    # Public variable
    brand = "Tesla"  # Default brand
    
    # Public method
    def start(self):
        return f"The {self.brand} car has started!"

# Create an instance of Car
my_car = Car()

# Access the public variable
print(f"Car brand: {my_car.brand}")

# Change the public variable
my_car.brand = "BMW"
print(f"New car brand: {my_car.brand}")

# Call the public method
print(my_car.start())

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Store the factor

    def __call__(self, value):
        return value * self.factor  # Multiply input by factor

# Create an object of Multiplier
m = Multiplier(6)

# Test if the object is callable
print(callable(m))  # Should print True

# Call the object like a function
result = m(10)
print(result)  # Should print 60

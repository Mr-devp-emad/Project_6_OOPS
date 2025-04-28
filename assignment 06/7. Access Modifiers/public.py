class Employee:
    # Public variable - accessible from anywhere
    name = "Ahmed "
    
    # Protected variable - accessible within the class and its subclasses
    _salary = 75000
    
    # Private variable - accessible only within the class
    __ssn = "328-76-2936"
    
    def __init__(self):
        print("Initializing Employee...")
        print(f"Inside class - Public name: {self.name}")
        print(f"Inside class - Protected salary: {self._salary}")
        print(f"Inside class - Private SSN: {self.__ssn}")

# Create an instance of Employee
emp = Employee()

# Accessing variables from outside the class
print("\nAccessing variables from outside the class:")
print(f"Public name: {emp.name}")  # This works fine
print(f"Protected salary: {emp._salary}")  # This works but shows a warning
try:
    print(f"Private SSN: {emp.__ssn}")  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error accessing private SSN: {e}")

# Note: In Python, private variables can still be accessed using name mangling
# The actual name becomes _ClassName__variableName
print(f"\nAccessing private variable using name mangling:")
print(f"Private SSN (using name mangling): {emp._Employee__ssn}")

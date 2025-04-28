# Define a custom exception
class InvalidAgeError(Exception):
    pass

# Define a function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18!")
    else:
        print("Age is valid.")

# Use try...except to handle the exception
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")

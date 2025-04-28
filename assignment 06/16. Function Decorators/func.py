# Define the decorator
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

# Apply the decorator to say_helloS
@log_function_call
def say_hello():
    print("Hello, World!")

# Call the decorated function
say_hello()

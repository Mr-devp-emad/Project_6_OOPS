class Counter:
    # Class variable to keep track of count
    count = 0
    
    def __init__(self):
        # Increment the count when a new object is created
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        # Class method using cls to access the class variable
        return cls.count
    
    @classmethod
    def display_count(cls):
        # Class method to display the current count
        print(f"Number of Counter objects created: {cls.count}")

# Example usage
if __name__ == "__main__":
    # Create some Counter objects
    counter1 = Counter()
    counter2 = Counter()
    counter3 = Counter()
    
    # Display the count using the class method
    Counter.display_count()
    
    # Get the count using the class method
    print(f"Count using get_count(): {Counter.get_count()}") 
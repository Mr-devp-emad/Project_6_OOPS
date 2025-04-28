class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Example usage
if __name__ == "__main__":
    # Create a dog instance
    my_dog = Dog("Ruffy", "Golden Retriever")
    
    # Call the bark method
    my_dog.bark()

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Example usage
if __name__ == "__main__":
    # Create a rectangle
    rect = Rectangle(5, 4)
    print(f"Area of rectangle: {rect.area()}")  
    
    # This would raise TypeError because Shape is abstract
    # shape = Shape()  # Uncomment to see the error

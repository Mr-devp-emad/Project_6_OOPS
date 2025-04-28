class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
if __name__ == "__main__":
    # Create a student object
    student1 = Student("Emad Ahmed ", 90)
    # Display student details
    student1.display() 
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the parent class constructor
        self.subject = subject

# Example usage
if __name__ == "__main__":
    # Create a teacher instance
    teacher = Teacher("Amin Alam ", "Python")
    
    # Print the teacher's information
    print(f"Teacher Name: {teacher.name}")
    print(f"Subject: {teacher.subject}")

class A:
    def show(self):
        print("This is class A's show method")

class B(A):
    def show(self):
        print("This is class B's show method")

class C(A):
    def show(self):
        print("This is class C's show method")

class D(B, C):
    pass

# Create an object of class D
d = D()

# Call the show method
print("Calling show() on object of class D:")
d.show()

# Print the Method Resolution Order
print("\nMethod Resolution Order (MRO) for class D:")
print(D.__mro__)

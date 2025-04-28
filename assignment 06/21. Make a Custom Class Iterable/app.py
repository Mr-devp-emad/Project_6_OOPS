class Countdown:
    def __init__(self, start):
        self.start = start  # Starting number
        self.current = start

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.current >= 0:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration

# Create a Countdown object
cd = Countdown(7)

# Use the object in a for-loop
for number in cd:
    print(number)

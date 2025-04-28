class Logger:
    def __init__(self):
        """Constructor: Called when an object is created"""
        print("Logger object created!")
    
    def __del__(self):
        """Destructor: Called when an object is destroyed"""
        print("Logger object destroyed!")

# Example usage
if __name__ == "__main__":

    logger = Logger()
    
   

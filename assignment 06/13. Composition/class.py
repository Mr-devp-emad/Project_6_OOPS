class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine started with {self.horsepower} horsepower"
    
    def stop(self):
        return "Engine stopped"

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has an Engine
    
    def start_engine(self):
        return self.engine.start()  # Accessing Engine's method
    
    def stop_engine(self):
        return self.engine.stop()  # Accessing Engine's method
    
    def get_car_info(self):
        return f"{self.make} {self.model} with {self.engine.horsepower}hp engine"

# Example usage
if __name__ == "__main__":
    # Create an engine
    engine = Engine(800)
    
    # Create a car with the engine
    car = Car("Mercedes", "G63", engine)
    
    # Demonstrate composition
    print(car.get_car_info())  # Accessing car's own method
    print(car.start_engine())  # Accessing engine's method through car
    print(car.stop_engine())   # Accessing engine's method through car

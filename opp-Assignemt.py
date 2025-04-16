# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}. My power is {self.power}.")

    def fight(self):
        print(f"{self.name} is fighting with {self.power}!")

# Subclass with inheritance and polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")

    # Override the fight method to show polymorphism
    def fight(self):
        print(f"{self.name} fights from the air using {self.power}!")

# Creating objects
hero1 = Superhero("IronShield", "Super Strength", "Earth")
hero2 = FlyingHero("SkyFalcon", "Wind Control", "Skytropolis", 300)

# Using methods
hero1.introduce()
hero1.fight()

print("-----")

hero2.introduce()
hero2.fly()
hero2.fight()

# Base class
class Vehicle:
    def move(self):
        print("The vehicle moves.")

# Subclasses with polymorphic behavior
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# List of vehicles demonstrating polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

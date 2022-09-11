# multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")


dog = Dog()
print(dog.alive)    # inherited from the Organism class
dog.eat()           # inherited from the Animal class
dog.bark()          # defined in Dog class

# -----------------------------------------------------------------------------
# multiple inheritance = when a child class is derived from more than one parent class
print ("*" * 100)
class Prey:

    def flee(self):
        print("This animal flees")
    
    def iam(self):
        print("I'm a prey")

class Predator:

    def hunt(self):
        print("This animal is hunting")

    def iam(self):
        print("I'm a predator")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator, Prey):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# rabbit.flee()
# hawk.hunt()
fish.flee()
fish.hunt()
fish.iam()  # Depends on the order
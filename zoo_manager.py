class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self._speak = "Animal sound"

    # def __str__(self):
    #     return f"{self.name}{self.speak}"

    def speak(self):
        return self._speak


class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def give_birth(self):
        return f"{self.name} the {self.species} has given birth"

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"

class Primate(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def climb_trees(self):
        return f"{self.name} the {self.species} is climbing trees"

class Marsupial(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self._carry_baby = "carrying its baby"

    def carry_baby(self):
        return f"{self.name} the {self.species} is {self._carry_baby}"

class Aviary:
    def __init__(self, birds=[]):
        self.birds = birds

class ReptileEnclosure:
    def __init__(self, reptiles=[]):
        self.reptiles = reptiles


# cat = Animal("Feline", )
# print(cat)
# fido = Animal("Fido", "dog")
# fido.speak()
# print(fido)
# cat = Mammal("Adam", "feline") #create instance
# cat.give_birth() #call the method for that instance
        
# Essentially this is saying that the class Aviary should have an attribute named birds (self.birds =) and it should store a list of birds (self.birds = [])
        
        # A car is a vehicle (inheritance) || A car has an engine (composition)

        # I would say yes, I think I may need to see an example but essentially if you see the need for the “super()” method that means you are utilizing inheritance.

        # Composition:
        # - an engine is part of a car, wheels are part of a car
        # Inheritance:
        # -has a relationship to eacth other, dependent upon each other


        # Polymorphism:
        # ability for different objects to respond to the same method call in a way that's appropriate for their individual types
        # -the same interface for different classes
        #-though you inherit a classes inheritance, you can override it on that individual class ie.
        # -polymorphism means you are overwriting inherited behavior.


# from abc import ABC, abstractmethod    #abstractmethod =Abstract Base Classes or abc aka class interfaces in other languages

#using abstract methods mean your code has rules placed inside it, so that any methods associated with that class must utilize the abstract methods, which also means less code for you to write out
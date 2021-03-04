# Classes in Python

# Creating a class using the keyword 'class'
class newClass:
    x = 5

p1 = newClass()
print(p1.x)

# These classes and objects are the most simplest forms, and aren't really useful in real life applications

# Using the __init__ function
class Person:
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):   # Function is executed when the class is being initiated
        self.age = age      # Function is used to assign values to object properties
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase

    # Object methods. Methods in objects are functions that belong to the object

    def identify(self):
        print("Hello my name is " + self.first_name)

user = Person(16, 150, 168, 'Kabir', 'Verma', 'Hello sir, I am an expert coder')

user.identify()
print(user.catch_phrase)


# Another example
class Monkey:
    def __init__(self, breed, colour):
        self.breed = chimpanzee
        self.colour = brown

    def screech(self):
        print('oo oo aa aa')

    def swing(self):
        print('weeeeeeee')

    def eat(self):
        print('nomnomnom')

# The self parameter is a reference to the current instance of the class
# It doesn't have to be named self, but it has to be the first paramter of any function in the class

class Game:
    def __init__(myGame, name, year_of_release):
        myGame.name = name
        myGame.year_of_release = year_of_release

    def myFav(abc):
        print("My favorite game is " + abc.name)

game1 = Game("CSGO", 2012)
game1.myFav()

# Modifying properties on objects
game1.year_of_release = 2013

print(game1.year_of_release)

# Pass statement
class Useless:
    pass

test = Useless()
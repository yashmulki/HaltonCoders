# Functions in Python

# Simple function
def print_hello():
    print('Hello!')


# Calling a function
print_hello()


# Passing in arguments/parameters
def say_hello(name):                # Parameters are the variables listed inside the parenthesis in the func def
    print('Hello ' + name + '!')    # Arguments are the values sent into the function (in this case, it's 'Kabir'


say_hello('monkey')


# Working with multiple arguments
def add(num1, num2):
    print(num1 + num2)


add(4, 9)   # Functions must be called with the correct number of arguments


# Keyword arguments
def monkeys(monkey3, monkey1, monkey2):
    print('The loudest monkey is ' + monkey2)


monkeys(monkey1 = 'Fred', monkey2 = 'Kevin', monkey3 = 'Kabir')


# Default parameters
def fruits(fruit = 'banana'):
    print('My favorite fruit is a ' + fruit)


fruits('Apple')
fruits('Strawberry')
fruits()


# Return values
def multiply(x, y):
    return x * y


input_x = int(input('Enter your first number: '))
input_y = int(input('Enter your second number: '))
print(multiply(input_x, input_y))


# Pass statement
def useless():
    pass

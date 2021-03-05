print("Hello, world!")         # Display some text.
input("What's your name? \n")  # The backslash (\) before the 'n' indicates it is an 'escape code'.
# Because of this, you can't directly put a backslash in a string.
print("\\")                    # To overcome this, you can write '\\'.

# print tags in python automatically add a new line character after the string
# To overcome this, after your string input put a comma and then add <end="">
print("This is a sentence.", end="")
print("This is another sentence.")

# These are comments; stuff you write here will be ignored when your code is run. To write a
# comment, start the line with a hash symbol (#). Python ignores everything you write after it.

"""
These are multiline comments, which are sometimes called 'docstrings'. The 'doc' comes from 
'documentation', which refers to specific kinds of text that accompanies and explains code, 
typically running through any potentially unexpected behavior of the code.
"""

'''
Using single quotes also works. In addition, these can also be used as multiline strings. The
biggest difference is that instead of using the '\n' escape code as mentioned above, you can 
simply start new lines like you would normally. More on this soon.
Multiline strings can by typed as you normally would and will be printed exactly as you typed 
them in the source  file.
You may have also noted that  our code has 4 spaces for each indent and that it doesn't go beyond a
certain length , (120) characcters. This is to make your code readable and it follows PEP guidelines
PEP: Python Enhancement Proposal
While you do not need to learn this, we reccomend you don't we also advise you to follow the PEP 
guidelines pycharm  highlights.
'''

# [Variables]
# -------------------------------------------------------------------------------------------------
# Variables are things which store values, kind of like a box. You can also think of it as
# attaching a name to a value. You can declare (make) a variable by writing '<name> = <value>',
# where <name> is the name you'd like to refer to the variable with, and <value> is the value (like
# a number, string, a mathematical expression, or even another variable.
#
# As their name implies, variables can change ('vary'-able). Most often, you'll change a variable
# by assigning something to it; this looks the same as declaring a variable ('<name> = <value>').
# Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#  Variable names are case-sensitive (age, Age and AGE are three different variables)

string = "This is a sentence!"  # A variable that stores some text. The text surrounded in quotes
# on the right side of the '=' called a 'string literal', since it
# is literally a string of characters (that forms text).

integer = 8  # A variable that stores an integer (colloquially called 'int' for short). The '8'
# here is an 'integer literal', similarly to string literals. These numbers can be (in
# theory) as large as you want (one billion, negative ten trillion, or even a googol).

double = 8.0  # A variable that stores a decimal number; Python call these 'floats', short for
# 'floating-point number'. That name refers to the way decimal numbers are stored by
# most computers. Floats can be basically as large as you want, but they will get
# more and more inaccurate the farther you stray from zero.

boolean = True  # A variable that stores a boolean value, either 'True' or 'False'. These are
# useful in many situations in programming, particularly those where you have to
# make choices.
list = [1, 2, 3, 4, 5]  # A list is what the name suggests, a list of objects or items. Lists in most
# languages are called and are accessed by indices(singular: index) An index
# is just the location of an item in a list. Unlike normal counting, the first
# item in a list is not at index 1 but instead it is at index: 0
listItem = list[0]  # This variable now has a value of 1

a = 6  # Unlike in many other languages, Python doesn't require that you specify what kind of
b = 8  # value (the 'type') a variable is going to store when you declare one. In fact, you
# can even assign a variable a value of a different type than it initially had (though
# this is highly discouraged).

a, b = 6, 8  # You can also declare multiple variables at once; this is the same as the above code.
# For reference, this is called 'multiple assignment' or 'unpacking'.

# !!!!!!!!!!!!!!!!!!! not changed from here on yet !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Variable conversion
# Variables in python can be converted really easily with the use of some simple functions
# Int to String
num1 = 1000
print(num1)  # this will print: 1000
string1 = str(num1)
print(string1)  # this will print: "1000"

# String to int
# If the string is a numeric value you can convert it to a num. Otherwise it will give you an error.
string2 = "18746"
print(string2)  # this will print: "18746"
num2 = int(string2)  # this will print: 18746

# String to list
# You can split the string into multiple items in a list.
string3 = "My name is Coder and I enjoy programming with my friends"
list1 = string3.split()
print(list1)  # this will give you a list with each word in the list as an item
# the value that you give to the split function is called the separator and is the value which it removes and uses to
# separate items. The default separator is a space ' '
list2 = string3.split(" ")
print(list2)  # this will also give you a list with every word.
list3 = string3.split("e")
print(list3)  # this will split the string at every 'e', the list will have 4 items

# conditionals
# using conditionals with booleans
true, false = True, False
if true:
    print("The value was True")
else:
    print("The value was False")

if false:
    print("The value was true")
else:
    print("The value was False")
# If the value is true, the code block after the if statement is run, if it is not true, the code block in else is run

# Using elif
alsoTrue, alsoFalse = True, False

if true:
    print("The value was True")
elif alsoTrue:
    print("The first value was False but the second value is True")
else:
    print("Neither of the values was True")

if false:
    print("The value was True")
elif alsoTrue:
    print("The first value was False but the second value is True")
else:
    print("Neither of the values was True")

"""
The computer goes line by line, checking the if, then the 1st elif, then 2nd and so on till one of the elifs is true. 
after the 'elifs' in the case that none of them are true, it will run the else. 
"""

if false:
    print("The value was True")
elif alsoFalse:
    print("The first value was False, but the second is true")
elif alsoTrue:
    print("The second value was also False but the third value is True")
else:
    print("Neither of the values was True")
'''
What an if statement does is just check 'if' something is true or not.
boolean variables are important when using conditionals
'''

# Operations with variables
# With numbers. PS: using a double and an integer in a calculation results in a double as the answer
# mathematical operators
a, b, c = 8, 6, 10  # variable declarations

print(a+b)  # prints 14
print(a+b+c)  # prints 24, this can be used for as many variables as you want
print(a-b)  # prints 2, b - a would print '-2'
print(a*b)  # prints 48
print(a/b)  # prints 1.333333333
print(a//b)  # prints 1, truncates the decimal values(not the same as rounding, more like cutting them away)
print(a % b)  # prints 2, gives the remainder
print(2 ** 3)  # prints 8, gives the value of 2 ^ 3. Syntax base ** exponent

# functions for comparing values
print(max(a, b, c))  # prints 10
print(min(a, b, c))  # prints 6

# Comparing Integers to get booleans
bool1 = a > b  # bool1 will be true if a is bigger than b.
print(bool1)  # As 8 > 6, this prints true
print(a > b)  # this will also print True, you do need to put it in a variable, you can perform operations in print
print(a < b)  # False, a is not smaller than b
print(a == b)  # False, a is not equal to b
print(a != b)  # True, a is unequal to b
x = 9
y = 9
print(x == y)  # True, x is equal to y
print(x != y)  # True, x is not unequal to y

print(x >= y)  # True, x is equal to y.
print(a >= b)  # True, a is smaller than b
print(x <= y)  # True, x is equal to y.
print(a <= b)  # False, a is smaller than b
print(x > a > b)  # True, x is bigger than a and a is bigger than b
print(b < a < y)  # True, b is smaller than and a is smaller than y
# >= and <= check both equality and greater/lesser respectively


# Comparing Booleans to get booleans
alsoTrue2, alsoFalse2 = True, False
print(true and alsoTrue)   # True | 'and' operator prints true ONLY if ALL the values being compared are true
print(true and alsoTrue and alsoTrue2)  # returns True
print(true and false)  # False
print(true or false)   # True | 'or' operator prints true if ANY of the values being compared are true
print(true or false or alsoFalse2)  # returns True
print(true or true)  # True
print(not true)  # False | not operator inverses the value of the boolean
print(not false)  # True
print(not not true)  # False | even number of 'not' negate themselves out

'''
Now that you know the comparisons that convert integers to booleans  you can figure out how they will behave in if 
statements
'''
# Integers | a, b, c = 8, 6, 10
if a > b:
    print("a is bigger than b")
elif b > a:
    print("b is bigger than a")
else:
    print("a is equal to b")


# Operations on Lists/array
listNums = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10]
listLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(listNums)  # Printing a list in python will print it the same way that you wrote the list out.
print(listLetters)  # This prints: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# In python a string is a basically an array of characters, so p much any operation that you can do on an array
# can be done on a string. There are a few differences so discretion is advised in using certain functions

# type casting is basically converting one type into another
# i.e. int into a string and etc etc
# https://www.tutorialspoint.com/python/python_type_casting.htm

# conversion from int to float is done automatically
a = 10
b = 10.5
c = a + b 
print(c)
# c = 20.5

# booleans also get converted automatically
# True is 1 
# False is 0 
a = True
b = 10.5
c = a + b
print(c)
# c = 11.5

# EXPLICIT TYPE CASTING
# by using int() float() str() you can forcefully change one type into another
a = int(2*3.14)
# a = 6
a = int(True)
# a = 1

# binary to integer conversation
a = int("110011",2)
# a = 51
# second digit shows our base
# octal conversion
a = int("20", 8)
print(a)
# a = 16
# hexadecimal conversion
a = int("2A9", 16)
# a = 681

# float conversion
# it'll just keep the dot or will add .0 at the end
a = float(10)
# a = 10.0
a = float("1.00E4")
# a = 10000.0
a = float("1.00E-4")
# a = 0.0001

# string conversion
a = str(11.10)
# a = 11.1
a = str(2/5)
# a = 0.4
# scientific notation
a = str(10E4)
# a = 100000.4
a = str(1.23e-4)
# a = 0.000123

# string conversion with lists
a = [1,2,3]
# and tuples
b = (1,2,3)
# and just a string for a list conversion
c = "hey"
object = list(c)
# object = ['h','e','y']

# lots more of conversions are available depending on the situation
# but can just pretty much google them
'''
1 	Python int() function

Converts x to an integer. base specifies the base if x is a string.
2 	Python long() function

Converts x to a long integer. base specifies the base if x is a string.
3 	Python float() function

Converts x to a floating-point number.
4 	Python complex() function

Creates a complex number.
5 	Python str() function

Converts object x to a string representation.
6 	Python repr() function

Converts object x to an expression string.
7 	Python eval() function

Evaluates a string and returns an object.
8 	Python tuple() function

Converts s to a tuple.
9 	Python list() function

Converts s to a list.
10 	Python set() function

Converts s to a set.
11 	Python dict() function

Creates a dictionary. d must be a sequence of (key,value) tuples.
12 	Python frozenset() function

Converts s to a frozen set.
13 	Python chr() function

Converts an integer to a character.
14 	Python unichr() function

Converts an integer to a Unicode character.
15 	Python ord() function

Converts a single character to its integer value.
16 	Python hex() function

Converts an integer to a hexadecimal string.
17 	Python oct() function

Converts an integer to an octal string.
'''
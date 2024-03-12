# https://www.tutorialspoint.com/python/python_variables.htm

# declaring variables
counter = 100 # integer
miles = 1000.0 # float/floating point 
name = "Bob Johnnes" # string

# deleting variables
del counter
del miles, name

# getting the type of a variable
exampleString = "this is a string"
print(type(exampleString))
# <class 'str'> will show up in console

# can declare variables yourself
x = str(10) # x is "10"
y = int(10) # y is 10
z = float(10) # z is 10.0

# variables are case sensitive
word = "dog"
Word = "cat"
print(f"{word} is not the same as a {Word}")

# instead of writing
a=10
b=10
c=10 
# you can write
a=b=c=10
# or 
a,b,c = 10,20,30


# NAMING CONVENTION
# you can use screaming snake case to declare constants (values that don't change)
PI_VALUE = 3.145
# data types define what sort of variables we are using
# https://www.tutorialspoint.com/python/python_data_types.htm
'''
Numeric - int, float, complex
String - str
Sequence - list, tuple, range
Binary - bytes, bytearray, memoryview
Mapping - dict
Boolean - bool
Set - set, frozenset
None - NoneType
'''

# NUMERIC
var1 = 1 # int
var2 = True # bool
var3 = 10.420 # float
var4 = 10+3j # complex, two parts - real and imaginary, j is the imaginary number, math stuffs

# can use type() to check the type of these
print(type(var1))
# <class 'int'>

# STRING
varString = "dog"
print(varString) # dog
print(varString + varString) # dogdog
print(varString[0]) # d
print(varString[1:2]) # og
print(varString*4) # dogdogdogdog
print("cat" + varString) # catdog

# SEQUENCE 
# lists
randomList = ['abcd', 10, 124.124, True, "Bob"]
smallList = ['foo','bar']
print(randomList) # prints the entire list
print(randomList[0]) # prints the first thing in the list (abcd)
print(randomList[2:4]) # prints 3rd and 4th entries (124.124, True)
print(randomList[2:]) # prints all after the 3rd entry (124.124, True, "Bob")
print(smallList*2) # prints list two times
print(randomList + smallList) # prints both lists

# tuple

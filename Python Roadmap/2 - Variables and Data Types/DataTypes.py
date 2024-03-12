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
# tuples are similar to lists as they also have sequences
personTuple = ("Bob","Dylan",1998,10,26)
# it can also have a list in itself or another tuple
tupleInATuple = (
    ("this is the first tuple", 123, 321),
    ("this is the second tuple",5,5),
    ["this","is","a","list","inside","a","tuple"]
    )
# same print operations apply as with a list

tinyTuple = (1,2,3)
tinyList = [1,2,3]
# tinyTuple[2] = 10 # this is invalid
tinyList[2] = 10 # this is valid
# you can't change tuple members

# dictionaries
# consist of key:value pairs
tinyDict = {1:"one", 2:"two", 3:"three"}
# creating a dictionary
tempDict = {}
# adding a pair
tempDict['one'] = "this is one"
# tempDict = {'one':"this is one"} 
tempDict[2] = "this is two"
# tempDict = {'one':"this is one", 2:"this is two"}
print(tempDict['one']) # "this is one"
print(tempDict[2]) # this is two
print(tempDict) # prints the entire thing
print(tempDict.keys) # prints all the keys (first part of the couple)
print(tempDict.values) # prints all the values

# set
# https://www.w3schools.com/python/python_sets.asp
# a collection, but not ordered or indexed
# can only put int, float, complex or bool, string or tuple
# no dictionaries or lists inside
# only immutable objects are hashable
exampleSet = {"apple","banana","cherry"}
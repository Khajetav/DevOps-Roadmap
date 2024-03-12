# done following the https://www.tutorialspoint.com/python/python_basic_syntax.htm
# imports are handled at the top
import sys

# one line comment
'''
multi 
line 
comment
'''

# python doesn't need type declarations (don't need to say that something is an integer or a string or something else)
item_one, item_two, item_three = 1, 2, 3
# THIS WILL NOT WORK print("Item one is " + item_one + " item two is " + item_two + " item three is " + item_three)
# you need to concatenate integers into strings in Python
# two ways to do it
print("Item one is " + str(item_one) + ", item two is " + str(item_two) + ", item three is " + str(item_three))
print(f"Item one is {item_one}, item two is {item_two}, item three is {item_three}")

# multi-line statements using \
total = item_one + \
    item_two + \
    item_three
print (f"Total is {total}")

# python supports different quote symbols
word = 'word'
sentence = "this is a sentence"
paragraph = """this is a paragraph. it has multiple sentences"""

# print something out to the console
# \n means that you display something in a new line
print(word + "\n" + sentence + "\n" + paragraph)

# wait for user's input
# NOTE - python3 uses input, python2 uses raw_input
input("\n\nPress the enter key to continue.")

# multiple statements in a line
x = 'foo'; y = 'bar'
sys.stdout.write(x+y+"\n")

# a group of statements in a block are called SUITES in Python
if x == y :
    print(f"{x} is equal to {y}") # this is a suite
elif x == word :
    print(f"{x} is equal to {word}") # this is also a suite
else :
    print(f"{x} is not equal to {y} or {word}") # this is another suite

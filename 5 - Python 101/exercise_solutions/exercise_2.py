"""
Iterate using a for-loop through all odd numbers between 5 and 27 using range()
"""
for i in range(5, 28, 2):
	print(i)

"""
Count from 1 to 10 using a while-loop and break out afterwards
"""

i = 0

while i < 10:
    i += 1
    print(i)

while True:
    for i in range(10):
        i += 1
    break

while True:
    print(list(range(1, 11)))
    break

while True:
    print(i)
    i += 1
    if i > 10:
        break

"""
Create a program that prints the letters of a word one-by-one
"""
word = 'test word'

for letter in word:
    print(letter, end='-')  # fix the separator

"""
Create a function with two input arguments that returns the sum of these two numbers
"""


def addition(a, b):
    sum = a + b
    return sum


print(addition(5, 2))

"""
Create a function that returns True if input is string "test word"
"""


def matching_string(input_string):
    return input_string == 'test word'


print(matching_string('other word'))
print(matching_string('test word'))

"""
Create a function string_length(a) that returns the length of a string by using the len() function
Now do it without len()
and maybe not counting the space
"""


def string_length(a):
    return len(a)


def simpler_string_length(a):
    length = 0
    for letter in a:
        if letter != ' ': # optional
        	length += 1
    return length


print(string_length('testing testing'))
print(simpler_string_length('testing testing'))
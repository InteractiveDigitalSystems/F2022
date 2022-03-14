"""
Create a list that contains all odd integers between 5 and 27
"""
start = 5
end = 28
odd_ints = list(range(start, end, 2))
print(odd_ints)

new_odd_ints = []
for i in range(5, 28, 2):
    new_odd_ints.append(i)

"""
Create a function that returns a random entry from a list of strings
"""

import random
def return_random_string():
	strings = ['hello', 'goodbye', 'whatever']
	num = random.randint(0,len(strings))
	#return strings[num]
	return random.choice(strings)

print(return_random_string())

def random_country():
	foo = ['denmark', 'norge', 'sverige']
	print(random.choice(foo))
	return random.choice(foo)

"""
Create a function that accepts a list of integers and returns the largest number
"""

import random
integers = [2, 5, 1, 29, 6]

def max_entry(a):
	return max(a)

def new_max_entry(a):
	max_var = 0
	for num in a:
		if num > max_var:
			max_var = num
	return max_var

def new_new_max_entry(a):
	a.sort()
	return a[-1]

print(max_entry(integers))
print(new_max_entry(integers))
print(new_new_max_entry(integers))

"""
Create a function that accepts a list of floats and returns the average
"""

def get_avg(a):
	length = len(a)
	sum = 0
	for number in a:
		sum += number
	return sum / length

print(get_avg(integers))
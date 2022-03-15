def get_numbers(omit=()):
	list = []
	for i in range(1,26):
		list.append(i)
		for j in omit:
			if j != i:
				list.remove(i)
	return list

def get_numbers_two(omit=()):
	list = list(range(1,26))
	for num in omit:
		list.remove(num)
	return list

def get_numbers_three(omit=()):
	list = []
	for i in range(1,26):
		if i not in omit:
			list.append(i)
	return list

def get_numbers_four(omit=()):
	if type(omit) is not tuple:
		print('Omit needs to be a tuple!')


print(get_numbers())
# print(get_numbers((3,5,8)))
print(get_numbers_four([1,2]))




import random

random_number = random.randint(0, 100)

def test_function():
	print('hello')

while True:
    print('Guess the number')
    user_guess = int(input())
    if random_number == user_guess:
        print('Well done, you guessed it!')
        break
    elif random_number > user_guess:
        print('number is higher')
    elif random_number < user_guess:
        print('number is lower')

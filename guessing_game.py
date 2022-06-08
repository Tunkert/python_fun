import random

def guessing_game(random_number):
	guess = int(input("What is your guess? "))
	if guess != random_number:
		if guess < random_number:
			print("Sorry, guess again, too low.")
		else:
			print("Sorry, guess again, too high.")
		guessing_game(random_number)
	else:
		print("You are correct!")
		play_again = input("Do you want to play again? y or n ").lower()
		if play_again == 'y':
			guessing_game(random.randint(1, 10))
		else:
			print("Thanks for playing! Have a great day!")

random_int = random.randint(1, 10)

guessing_game(random_int)
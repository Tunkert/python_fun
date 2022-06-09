# improved rock, paper, scissors game
import random

def determine_comp(comp_value):
	""" this function determines what computer choice is
	based on a random number"""
	if comp_value == 1:
		comp = 'rock'
	elif comp_value == 2:
		comp = 'paper'
	else:
		comp = 'scissors'
	return comp


def player_pick():
	""" this function determines the player choice and error
	check for choices that aren't valid """
	player_choice = input("Rock, paper or scissors? ").lower()
	while player_choice != 'rock' and player_choice != 'paper' and \
		  player_choice != 'scissors':
		print("Listen buddy, that's not a choice! ")
		player_choice = input("Rock, paper, or scissors? ").lower()
	return player_choice


def output_game(comp_choice, state):
	""" this function outputs who won the rock, paper, scissors pick """
	print(f"Computer picked {comp_choice}, {state}!")


def who_won(comp_wins, player_wins, win_state):
	""" this function prints who won the most games """
	print(f"The computer won {comp_wins} and you won {player_wins}. {win_state}.")


def games_status(comp_wins, player_wins):
	""" this function determines who won the most games """
	if comp_wins == player_wins:
			win_state = 'Draw'
			who_won(comp_wins, player_wins, win_state)
	elif comp_wins > player_wins:
		win_state = 'The computer won more times'
		who_won(comp_wins, player_wins, win_state)
	else:
		win_state = 'You won more times than the computer.'
		who_won(comp_wins, player_wins, win_state)


def play_again(comp_wins, player_wins):
	""" this function determines if you want to play another game or not """
	play_more = input("Do you want to play more? (y/n) ").lower()
	while play_more != 'y' and play_more != 'n':
		print("That's not a valid choice.")
		play_more = input("Do you want to play more? (y/n) ").lower()
	if play_more == 'y':
		rps_game(comp_wins, player_wins)
	else:
		games_status(comp_wins, player_wins)


def p1_wins(comp_wins, player_wins, comp_choice):
	""" this function is run if player 1 wins a game and 
	increments player 1's score """
	comp_wins += 0
	player_wins += 1
	state = 'player wins'
	output_game(comp_choice, state)
	play_again(comp_wins, player_wins)


def c_wins(comp_wins, player_wins, comp_choice):
	""" this function is run if the computer wins a game
	and increments the computers score """
	comp_wins += 1
	player_wins += 0
	state = 'computer wins'
	output_game(comp_choice, state)
	play_again(comp_wins, player_wins)


def outcomes(p1_choice, comp_choice, comp_wins, player_wins):
	""" this function determines outcomes of an individual game """
	if p1_choice == comp_choice:
		print("draw!")
		comp_wins += 0
		player_wins += 0
		rps_game(comp_wins, player_wins)
	elif p1_choice == 'rock':
		if comp_choice == 'scissors':
			p1_wins(comp_wins, player_wins, comp_choice)
		else:
			c_wins(comp_wins, player_wins, comp_choice)
	elif p1_choice == 'paper':
		if comp_choice == 'rock':
			p1_wins(comp_wins, player_wins, comp_choice)
		else:
			c_wins(comp_wins, player_wins, comp_choice)
	else:
		if comp_choice == 'paper':
			p1_wins(comp_wins, player_wins, comp_choice)
		else:
			c_wins(comp_wins, player_wins, comp_choice)


def rps_game(comp_wins, player_wins):
	""" this function runs a game """
	comp_value = random.randint(1, 3)
	comp_choice = determine_comp(comp_value)
	p1_choice = player_pick()
	outcomes(p1_choice, comp_choice, comp_wins, player_wins)
	
rps_game(0, 0)


# Seperation of concern
# Rock Paper Scissor

import random

print('******** Rock Paper Scissor **********')
# constants are uppercased
OPTIONS = ['Rock','Paper','Scissor']

def get_computer_choice():
	return random.choice(OPTIONS)

def get_human_choice():
	choice_number = int(input('Enter number of your choice: ' ))
	return OPTIONS[choice_number-1]

def print_option():
	print('Choose anyone option:')
	print('\n'.join(f'({i+1}) {option.title()}' for i,option in enumerate(OPTIONS)))

def print_choices(human_choice,computer_choice):
	print(f'You chose: {human_choice}\nComputer chose: {computer_choice}')

def print_win_loose(human_choice , computer_choice , human_loses_to , human_beats):
	if computer_choice == human_loses_to:
		print(f'Sorry , {human_loses_to} beats {human_choice} !')
		return;
	else:
		print(f'Hurray , {human_choice} beats {human_beats} !')
		return;

def print_result(human_choice,computer_choice):
	if human_choice == computer_choice:
		print('Draw !!')
		return;
	if human_choice == 'Rock':
		print_win_loose('Rock' , computer_choice ,'Paper','Scissor')
	if human_choice == 'Paper':
		print_win_loose('Paper', computer_choice , 'Scissor', 'Rock')
	if human_choice == 'Scissor':
		print_win_loose('Scissor', computer_choice , 'Rock', 'Paper')

print_option()
computer_choice = get_computer_choice()
human_choice = get_human_choice()
print_choices(human_choice,computer_choice)
print_result(human_choice,computer_choice)

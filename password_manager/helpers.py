import os
import sys

def get_terminal_size():
	try:
		return os.get_terminal_size()
	except OSError:
		return os.get_terminal_size(80, 25)

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

def get_user_choice(options):
	while True:
		try:
			choice = int(input())
			if (choice >= 0 and choice <= len(options)):
				return choice
			else:
				print("Invalid choice, try again: ")
		except ValueError:
				print("Please enter a valid number")

def exit_program():
	print("Are you sure you want to quit?")
	print("1) yes")
	print("2) no")
	choice = get_user_choice([1, 2])
	if choice == 1:
		clear_screen()
		sys.exit()
	else:
		pass
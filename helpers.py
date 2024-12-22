import os

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

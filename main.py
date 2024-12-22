import os

def get_terminal_size():
	try:
		return os.get_terminal_size()
	except OSError:
		return os.get_terminal_size(80, 25)

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

def get_user_choice():
	while True:
		try:
			choice = int(input())
			if (choice >= 0 and choice <= 3):
				return choice
			else:
				print("Invalid choice, try again: ")
		except ValueError:
				print("Please enter a valid number")

def display_options():
	print("Choose an option below: \n")
	print("\033[1;31m1)\033[0m Generate a Password")
	print("\033[1;31m2)\033[0m View a Passwords")
	print("\033[1;31m3)\033[0m Exit\n")
	print("Enter Your choice[1-3]: ")
	get_user_choice()

def display_welcome():
	big_title = r""" ____                                     _   __  __                                   
|  _ \ __ _ ___ _____      _____  _ __ __| | |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| | | |  | | (_| | | | | (_| | (_| |  __/ |   
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                                       |___/           
"""
	small_title = r""" ____                                     _ 
|  _ \ __ _ ___ _____      _____  _ __ __| |
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
                                            
 __  __                                   
|  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
| |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |  | | (_| | | | | (_| | (_| |  __/ |   
|_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                          |___/           
"""
	size = get_terminal_size()
	title = big_title if size.columns >= 100 else small_title

	clear_screen()

	for line in title.splitlines():
		print(line.center(size.columns))
	print("\n")
	print("Welcome to your Password Manager!".center(size.columns))
	print("\n")
	display_options()

if __name__ == "__main__":
	display_welcome()
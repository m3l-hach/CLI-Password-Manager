import helpers

menu_titles = {
	"main_menu": {
		"big_title":  r""" ____                                     _   __  __                                   
|  _ \ __ _ ___ _____      _____  _ __ __| | |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| | | |  | | (_| | | | | (_| | (_| |  __/ |   
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                                       |___/           
""",
		"small_title": r""" ____                                     _ 
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
	},
	"pass_gen_menu": {
		"big_title": r""" ____                                     _    ____                           _             
|  _ \ __ _ ___ _____      _____  _ __ __| |  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| | | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                            
""",
		"small_title": r""" ____                                     _ 
|  _ \ __ _ ___ _____      _____  _ __ __| |
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
                                            
  ____                           _             
 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_| |  __/ | | |  __/ | | (_| | || (_) | |   
 \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                               """
	},
	"pass_tab_menu": {
		"big_title": r""" ____                                     _       _____     _     _      
|  _ \ __ _ ___ _____      _____  _ __ __| |___  |_   _|_ _| |__ | | ___ 
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` / __|   | |/ _` | '_ \| |/ _ \
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| \__ \   | | (_| | |_) | |  __/
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|___/   |_|\__,_|_.__/|_|\___|
                                                                         
""",
		"small_title": r""" ____                                     _     
|  _ \ __ _ ___ _____      _____  _ __ __| |___ 
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` / __|
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| \__ \
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|___/
                                                
 _____     _     _      
|_   _|_ _| |__ | | ___ 
  | |/ _` | '_ \| |/ _ \
  | | (_| | |_) | |  __/
  |_|\__,_|_.__/|_|\___|
                        """
	}
}

menu_content = {
	"main_menu": "Welcome to your Password Manager!",
	"pass_gen_menu": "Here you can generate passwords.",
	"pass_tab_menu": "Here you can see all your saved passwords"
}

menu_options = {
	"main_menu": [
		"Generate a password",
		"View passwords",
		"Exit"
	],
	"pass_gen_menu": [
		"Generate a password",
		"Come back to main menu"
	],
	"pass_tab_menu": [
		"Add password",
		"Del password",
		"Come back to main menu"
	]
}

class Menu:
	def __init__(self, menu_name, titles, content, options):
		self.menu_name = menu_name
		self.titles = titles[menu_name]
		self.content = content[menu_name]
		self.options = options[menu_name]

	def display_title(self):
		helpers.clear_screen()
		size = helpers.get_terminal_size()
		title = self.titles["big_title"] if size.columns >= 100 else self.titles["small_title"]
		for line in title.splitlines():
			print(line.center(size.columns))
	
	def display_content(self):
		print("\n")
		size = helpers.get_terminal_size()
		for line in self.content.splitlines():
			print(line.center(size.columns))
		print("\n")

	def display_options_get_choice(self):
		print("Choose an option below: \n")
		for i, option in enumerate(self.options):
			print(f"\033[1;31m{i + 1})\033[0m {option}")
		print(f"\nEnter Your choice[1-{len(self.options)}]: ")
		return helpers.get_user_choice(self.options)

	def display_menu(self):
		self.display_title()
		self.display_content()
		return self.display_options_get_choice()

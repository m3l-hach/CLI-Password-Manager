import menu
import pass_storage
from helpers import exit_program
from pass_gen import generate_pass

main_menu = menu.Menu("main_menu", menu.menu_titles, menu.menu_content, menu.menu_options)
pass_gen_menu = menu.Menu("pass_gen_menu", menu.menu_titles, menu.menu_content, menu.menu_options)
pass_tab_menu = menu.Menu("pass_tab_menu", menu.menu_titles, menu.menu_content, menu.menu_options)


current_menu = main_menu

while current_menu:
	if not pass_storage.render_db():
		pass
	else:
		pass_tab_menu.content = pass_storage.render_db()
	choice = current_menu.display_menu()

	if current_menu == main_menu:
		if choice == 1:
			current_menu = pass_gen_menu
		elif choice == 2:
			current_menu = pass_tab_menu
		else:
			exit_program()
	elif current_menu == pass_gen_menu:
		if choice == 1:
			generate_pass()
		elif choice == 2:
			current_menu = main_menu
	elif current_menu == pass_tab_menu:
		if choice == 1:
			pass_storage.add_passwords()
		elif choice == 3:
			current_menu = main_menu
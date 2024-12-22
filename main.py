import menu

main_menu = menu.Menu("main_menu", menu.menu_titles, menu.menu_content, menu.menu_options)

choice = main_menu.display_menu()
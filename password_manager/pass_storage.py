import sqlite3
from tabulate import tabulate
import time
from helpers import get_user_choice
import pass_encryption
from config import DB_FILE

def init_db():
	conn = sqlite3.connect(DB_FILE)
	cursor = conn.cursor()

	cursor.execute("""
				CREATE TABLE IF NOT EXISTS passwords (
				service TEXT NOT NULL,
				username TEXT,
				password TEXT NOT NULL 
				)
				""")
	
	conn.commit()
	conn.close()

init_db()

def render_db(key):
	conn = sqlite3.connect(DB_FILE)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM passwords")
	pass_table = cursor.fetchall()
	decrypted_pass_table = [(row[0], row[1], pass_encryption.decrypt_data(key, row[2])) for row in pass_table]
	conn.close()
	if not pass_table:
		return None
	headers = ["Service", "Username", "Password"]
	table_str = tabulate(decrypted_pass_table, headers, tablefmt="grid")
	return table_str

def	get_services():
	conn = sqlite3.connect(DB_FILE)
	cursor = conn.cursor()
	cursor.execute("SELECT service FROM passwords")
	services = cursor.fetchall()
	services_list = [row[0] for row in services]
	return services_list

def add_password(key):
	services_list = get_services()
	while True:
		service = input("Enter the service name (e.g., Gmail): ")
		if service.strip() in services_list:
			print(f"{service} already exists.")
		elif service.strip():
			break
		else:
			print("Service cannot be blank.")
	username = input("Enter the username/email (or leave blank): ")
	while True:
		password = input("Enter the password (cannot be blank): ")
		if password.strip():
			encrypted_password = pass_encryption.encrypt_data(key, password)
			break
		print("Password cannot be blank. Please enter a valid password.")

	conn = sqlite3.connect(DB_FILE)
	cursor = conn.cursor()
	cursor.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)", (service, username, encrypted_password))
	conn.commit()
	conn.close()

	print(f"\033[1mPassword for {service} saved successfully.\033[0m")
	time.sleep(2)

def	validate_deletion(choice):
	print(f"Are you sure you want to delete \033[1m{choice}\033[0m password?")
	print("1) yes")
	print("2) no")
	choice = get_user_choice([1, 2])
	if choice == 1:
		return 1
	else:
		return 2

def del_password():
	services_list = get_services()
	if not services_list:
		print("No password to delete.")
		time.sleep(2)
	else:
		while True:
			choice = input("Enter the service's name of the password to delete: ")
			if choice in services_list:
				if validate_deletion(choice) == 1:
					conn = sqlite3.connect(DB_FILE)
					cursor = conn.cursor()
					cursor.execute("DELETE FROM passwords WHERE service = (?)", (choice,))
					conn.commit()
					conn.close()
					print(f"\033[1mPassword for {choice} deleted successfully.\033[0m")
					time.sleep(2)
				break
			else:
				print(f"\033[1m{choice}\033[0m does not exists.")
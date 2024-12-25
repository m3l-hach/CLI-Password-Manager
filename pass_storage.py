import sqlite3
from tabulate import tabulate
import time

def init_db():
	conn = sqlite3.connect('passwords.db')
	cursor = conn.cursor()

	cursor.execute("""
				CREATE TABLE IF NOT EXISTS passwords (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				service TEXT,
				username TEXT,
				password TEXT NOT NULL 
				)
				""")
	
	conn.commit()
	conn.close()

init_db()

def render_db():
	conn = sqlite3.connect('passwords.db')
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM passwords")
	pass_table = cursor.fetchall()
	conn.close()
	if not pass_table:
		return None
	headers = ["ID", "Service", "Username", "Password"]
	table_str = tabulate(pass_table, headers, tablefmt="grid")
	return table_str

def add_passwords():
	service = input("Enter the service name (e.g., Gmail) (or leave blank): ")
	username = input("Enter the username/email (or leave blank): ")
	while True:
		password = input("Enter the password (cannot be blank): ")
		if password.strip():
			break
		print("Password cannot be blank. Please enter a valid password.")

	conn = sqlite3.connect('passwords.db')
	cursor = conn.cursor()

	cursor.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)", (service, username, password))

	conn.commit()
	conn.close()

	print(f"\033[1mPassword for {service} saved successfully.\033[0m")
	time.sleep(2)

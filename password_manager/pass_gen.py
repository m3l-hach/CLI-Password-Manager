import string
import random
import time
import pyperclip

def get_pass_len():
	while True:
		try:
			lenght = int(input("Enter the desired password length: "))
			if lenght >= 8:
				return lenght
			else:
				print("Enter a number greater than 8.")
		except ValueError:
			print("Enter a valid number.")

def check_choices(choices):
	for elem in choices:
		if elem < 1 or elem > 3:
			return False
	return True

def get_char_set():
	print("Choose the character set for your password:\n")
	print("1. Digits")
	print("2. Letters")
	print("3. Special characters\n")
	print("You can enter multiple sets separated by space:")
	while True:
		choices = list(map(int, input().split()))
		if check_choices(choices) == True:
			return choices
		else:
			print("Enter valid choice.")
	
def create_chars_list():
	charartersList = ""
	choices = get_char_set()

	if 1 in choices:
		charartersList += string.digits
	if 2 in choices:
		charartersList += string.ascii_letters
	if 3 in choices:
		charartersList += string.punctuation

	return charartersList

def generate_pass():
	length = get_pass_len()
	charactersList = create_chars_list()
	password = []

	for i in range(length):
		randomChar = random.choice(charactersList)
		password.append(randomChar)
	print("Password: " + "".join(password))
	pyperclip.copy("".join(password))
	print("\033[1mThe password is now in your clipboard.\033[0m")
	time.sleep(5)
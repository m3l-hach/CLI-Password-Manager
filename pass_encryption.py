import getpass
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode

def	get_salt():
	if not os.path.exists("salt.bin"):
		with open("salt.bin", "wb") as f:
			salt = os.urandom(16)
			f.write(salt)
	else:
		with open("salt.bin", "rb") as f:
			salt = f.read()
	return salt

def	derive_key(password):
	salt = get_salt()
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=32,
		salt=salt,
		iterations=1000000
		)
	return urlsafe_b64encode(kdf.derive(password.encode()))

def	create_master_password():
	while True:
		master_password = getpass.getpass("Create a master password: ").strip()
		if len(master_password) < 8:
			print("Master password should be at least 8 characters long. Try again.")
			continue
		confirm_password = getpass.getpass("Confirm your password: ").strip()
		if master_password != confirm_password:
			print("Passwords don't match. Try again.")
			continue
		salt = os.urandom(16)
		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=salt,
			iterations=1000000
		)
		hashed_password = urlsafe_b64encode(kdf.derive(master_password.encode()))
		with open("master.hash", "wb") as f:
			f.write(salt + b"\n" + hashed_password)
		break

def verify_master_password():
	if not os.path.exists("master.hash"):
		print("No master password found. let's create one.")
		create_master_password()
	
	with open("master.hash", "rb") as f:
		lines = f.readlines()
		salt = lines[0].strip()
		stored_hashed_pass = lines[1].strip()
	
	master_password = getpass.getpass("Enter your master password: ")

	kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=salt,
			iterations=1000000
		)
	
	derived_hashed_pass = urlsafe_b64encode(kdf.derive(master_password.encode()))
	if derived_hashed_pass == stored_hashed_pass:
		return derive_key(master_password)
	else:
		print("Incorrect password. Try again.")
		return None

def encrypt_data(key, plaintext):
	fernet = Fernet(key)
	plaintext = str(plaintext).encode()
	cyphertext = fernet.encrypt(plaintext)
	return cyphertext.decode()

def decrypt_data(key, cyphertext):
	fernet = Fernet(key)
	cyphertext = str(cyphertext).encode()
	plaintext = fernet.decrypt(cyphertext)
	return plaintext.decode()

def start_program():
	key = None
	while not key:
		key = verify_master_password()
	return key

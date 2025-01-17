import os

# Define the base directory in the user's home directory
BASE_DIR = os.path.expanduser("~/.password_manager")

# Paths for specific files
SALT_FILE = os.path.join(BASE_DIR, "salt.bin")
PASSWORD_FILE = os.path.join(BASE_DIR, "master_password.hash")
DB_FILE = os.path.join(BASE_DIR, "passwords.db")

# Ensure the base directory exists
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
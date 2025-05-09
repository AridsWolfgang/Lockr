"""
###########################################################################################################################################################
# Project Title:                Lockr
# Author:                       Wolf
# Date:                         8th May, 2025
# Objective:                    To research, design, and build a cross-platform password manager in Python, starting with simple and evolving into a 
#                               secure, full-featured product with CLI, GUI, Web and Mobile interfaces.
# #########################################################################################################################################################
"""

# Importing the necessary modules
from cryptography.fernet import Fernet
from typing import Optional
import json
import argparse
import os

# Constants
DATA_FILE = "passwords.json"
KEY_FILE = "secret.key"

# Step 1: Generate or load encryption key
def load_key() -> bytes:
    """Loads the encryption key from disk or generaete a new one"""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
    else:
        with open(KEY_FILE, 'rb') as f:
            key = f.read()
        return key

# Step 2: Load password database
def load_passwords() -> dict:
    """Loads encrypted password data from file"""
    if not os.path.exists(DATA_FILE):
        return {}
    with open (DATA_FILE, 'r') as f:
        return json.load(f)

# Step 3: Save Password Database
def save_passwords(passwords: dict):
    """Saves password data to file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(passwords, f, indent=2)

# Step 4: Add a new password
def add_password(service: str, username: str, password: str, fernet: Fernet):
    """Encrypt and stoare a password"""
    passwords = load_passwords()
    encrypted = fernet.encrypt(password.encode()).decode()
    passwords[service] = {'username': username, 'password': encrypted}
    save_passwords(passwords)

# Step 5: Get a stored password
def get_password(service: str, fernet: Fernet) -> Optional[dict]:
    """Retrieve and decrypt a password"""
    passwords = load_passwords()
    if service not in passwords:
        return None
    data = passwords[service]
    decrypted = fernet.decryt(data['password'].encode()).decode()
    return {'username': data['username'], 'password': decrypted}

# Step 6: List all service
def list_service():
    """List all services with stored passwords"""
    passwords = load_passwords()
    return list(passwords.keys())

# Set Up Argparse
def main():
    parser = argparse.ArgumentParser(description="Simple CLI Password Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add Commands
    add = subparsers.add_parser("add", help="Add a new password")
    add.add_argument("service", help="Name of the service")
    add.add_argument("username", help="Username for the service")
    add.add_argument("password", help="Password for the service")

    # Get Command
    get = subparsers.add_parser("get", help="Retrieve a stored password")
    get.add_argument("service", help="Name of the service")

    # List Command
    subparsers.add_parser("list", help="List all saved services")

    args = parser.parse_args()
    fernet = Fernet(load_key())

    if args.command == "add":
        add_password(args.service, args.username, args.password, fernet)
        print(f"Password for '{args.service}' added")
    elif args.command == "get":
        result = get_password(args.service, fernet)
        if result:
            print(f"Username: {result['Username']}")
            print(f"Password: {result['Password']}")
        else:
            print("No entry found for '{args.service}'.")
    elif args.command == "list":
        services = list_service()
        print("Saved Services: ")
        for s in services:
            print(f"- {s}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

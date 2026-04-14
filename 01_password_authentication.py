# Assignment Date: 07/02/2026
# Assignment Name: Password Authentication
# Description: Create a strong code for password authentication using python.

import hashlib
import getpass
import re


def hash_password(password: str) -> str:
    """Return a SHA-256 hash of the given password."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def is_strong_password(password: str) -> tuple[bool, str]:
    """Check whether a password meets the strength rules."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, "Strong password."


def register(users: dict) -> None:
    print("\n--- Register ---")
    username = input("Choose a username: ").strip()
    if username in users:
        print("Username already exists.")
        return

    while True:
        password = getpass.getpass("Choose a strong password: ")
        ok, msg = is_strong_password(password)
        if ok:
            break
        print(msg)

    confirm = getpass.getpass("Confirm password: ")
    if password != confirm:
        print("Passwords do not match. Try again.")
        return

    users[username] = hash_password(password)
    print(f"User '{username}' registered successfully.")


def login(users: dict) -> None:
    print("\n--- Login ---")
    username = input("Username: ").strip()
    if username not in users:
        print("User not found.")
        return

    for attempt in range(3):
        password = getpass.getpass("Password: ")
        if hash_password(password) == users[username]:
            print(f"Welcome back, {username}!")
            return
        print(f"Incorrect password. Attempts remaining: {2 - attempt}")
    print("Too many failed attempts. Try again later.")


def main() -> None:
    users: dict[str, str] = {}
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ").strip()
        if choice == "1":
            register(users)
        elif choice == "2":
            login(users)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

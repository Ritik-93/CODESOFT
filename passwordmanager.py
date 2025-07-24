import random
import string
def generate_password():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length should be at least 4 characters for better security.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Your generated password is: {password}")
generate_password()
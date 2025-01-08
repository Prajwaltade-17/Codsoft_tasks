import random
import string

def generate_password():
    characters = string.ascii_letters
    symbols = "!@#$%^&*()-_=+[]{}|;:<>,.?/"
    numbers = string.digits

    selected_characters = random.choices(characters, k=5)
    selected_symbols = random.choices(symbols, k=3)
    selected_numbers = random.choices(numbers, k=3)

    password_components = selected_characters + selected_symbols + selected_numbers
    random.shuffle(password_components)

    password = ''.join(password_components)

    while len(password) <= 10:
        password += random.choice(string.ascii_letters)
    
    return password

print("Generated Password:", generate_password())

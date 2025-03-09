import random
import string


def generate_passwd(numbers =12, digit=True, special=True):
    characters = string.ascii_letters
    if digit:
        characters += string.digits
    if special:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(numbers))
    password += "s120802"
    return password


print(generate_passwd(16, True, True))
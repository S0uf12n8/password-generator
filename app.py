import random
import string


def generate_passwd(numbers =12, digit=True, special=True):
    characters = string.ascii_letters
    if digit:
        characters += string.digits
    if special:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(numbers))
    
    mark = "s120802"
    insert_index = random.randint(0, len(password))  
    mixed_password = password[:insert_index] + mark + password[insert_index:]

    return mixed_password



print(generate_passwd(16, True, True))
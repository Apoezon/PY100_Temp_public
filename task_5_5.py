import string
import random

def get_random_password() -> str:
    ...  # TODO написать функцию генерации случайных паролей
    password = ''
    sample = string.ascii_uppercase + string.ascii_lowercase + string.digits
    for i in random.sample(sample, 8):
        password+=i
    return password

print(get_random_password())

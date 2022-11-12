import random

def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    a = []
    while len(a) < 15:
        el = random.randint(-10, 10)
        if el not in a:
            a.append(el)
    return a

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

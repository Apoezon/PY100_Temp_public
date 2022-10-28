def draw_field(field: list) -> None:
    """
    Функция рисует в консоль состояние поля из "двумероного массива" заданного размера
    Пусть: 0 - пустое поле " "
          1 - нолик "O"
          2 - крестик "X"

    Пример пустого поля:
      [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]
    В консоли:
    | | | |
    | | | |
    | | | |
    Пример поля:
      [[2, 0, 2],
      [0, 1, 0],
      [0, 0, 1]]
    В консоли:
    |Х| |Х|
    | |O| |
    | | |O|
    :param field:
    :return:
    """
    field_size = len(field)
    range_size = range(field_size)
    # print(f"Размер поля равен {field_size}")
    output_string = ""
    for i in range_size:
        output_string += "|"
        for g in range_size:
            if field[i][g] == 0:
                output_string += " |"
            elif field[i][g] == 1:
                output_string += "O|"
            elif field[i][g] == 2:
                output_string += "X|"
            else:
                print(f"Некорректный ввод в столбце {g + 1} строки {i + 1}")
                return
        output_string += "\n"
    print(output_string)
    return


def new_field(field_size: int):
    """
    Функция создает пустое игровое поле размера field_size.
    На входе получает значение размера поля и выводит "двумерный массив" для отображения поля функцией draw_field
    :param field_size:
    :return:
    """
    new_field = []
    range_size = range(field_size)
    for i in range_size:
        line_array = []
        for g in range_size:
            line_array.append(0)
        new_field.append(line_array)

    # print(new_field)
    return new_field


a = [[2, 0, 2],
     [0, 1, 0],
     [0, 0, 1]]
b = [
    [2, 0, 1, 2],
    [1, 2, 0, 1],
    [2, 2, 0, 0],
    [1, 0, 1, 0]
]
c = [[2, 0, 2],
     [0, 1, 0],
     [3, 0, 1]]
first_player = input("Начнем! Введите первого игрока: ")
second_player = input("Введите второго игрока: ")
field_size = input("Введите размер поля: ")
start_field = new_field(int(field_size))
draw_field(start_field)
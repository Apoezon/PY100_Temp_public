def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    dict_char = {}
    for symbol in str_.lower():
        if symbol.isalpha():
            dict_char[symbol] = 0

    for i in str_.lower():
        if i.isalpha():
            dict_char[i] += 1

    return dict_char

def get_percentage_char(symbol_dict):
    symbol_amount = sum(symbol_dict.values())
    for t in symbol_dict:
        symbol_dict[t] = round(symbol_dict[t] / symbol_amount * 100, 2)
    return symbol_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

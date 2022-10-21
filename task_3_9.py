salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
def start_up_money(income, costs, months, inflation):
    money = 0
    for i in range(months):
        money = costs - income + money
        costs = costs*(1+inflation)
    return money
print(round(start_up_money(salary, spend, months, increase)))


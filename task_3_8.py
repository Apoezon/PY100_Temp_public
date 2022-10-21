money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

#month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
def bankrot(debit_, income_, costs_, inflation_):
    month_ = 0
    while debit_ > 0:
        if (debit_ - costs_)>0:
            month_ += 1
            debit_ = debit_ - costs_
            costs_ = costs_*(1+inflation_)
            debit_ = debit_ + income_
            # print("остаток после месяца №"+str(month_)+" равен "+ str(debit_))
        else:
            break
    return month_
month = bankrot(money_capital, salary, spend, increase)

print(month)

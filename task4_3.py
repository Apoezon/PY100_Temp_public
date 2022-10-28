def delete(list_, index=None):
    changed_list = ''  # TODO реализовать функцию удаления элемента из списка по индексу
    if index == None:
        changed_list = list_[0 : len(list_)-1]
    elif index != None:
        list1 = list_[0 : index]
        list2 = list_[index+1 : ]
        changed_list = list1+list2

    return changed_list

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

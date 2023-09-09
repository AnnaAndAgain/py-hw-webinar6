# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
#
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
#
# Устно решили, что диапазон тоже вводится на старте.
# Для примера он от 7 до 10 вкл.


def find_index_in_range(lst1, min_val, max_val):
    lst2 = list()
    for i in range (len(lst1)):
        if max_val >= lst1[i] >= min_val:
            lst2.append(i)

    return lst2


def sanity_check(min_val, max_val):
    if min_val < max_val:
        return True
    else:
        return False


def input_int(str1):
    return int(input(str1))


user_lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
user_min = input_int("Введите минимальное значение: ")
user_max = input_int("Введите максимальное значение: ")
if sanity_check(user_min, user_max):
    print(find_index_in_range(user_lst, user_min, user_max))
else:
    print("Вы ошиблись при вводе: минимум должен быть больше максимума. Начните заново.")



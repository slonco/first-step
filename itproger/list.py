# Список, который хранит числа

# numbers = [1,2,3,4,5,10]
#
#
# # ## Добавление символов
#
# numbers.append(100) # добавить число в конец списка
#
# numbers.insert(0, True) # вставить число в список ("куда вставляем", "что вставляем"). Если "куда вставляем" указать отрицательное значение (-1, -2, -3 и т.д.), то элемент будет добавлен с конца.
#
# # numbers.extend(["Y", "N", "M"]) # вставить список в конце
#
# # а можно поместить список в отдельную переменную:
#
# b = [4, 5, 1]
#
# numbers.extend(b)
#
# numbers.sort()
#
# # numbers.reverse() # делает реверс строки (конец ставит в начало)
#
# # ## Удаление символов
#
# # numbers.pop() # Удаляет один элемент с конца. В скобках можно передать индекс элемента, который надо удалить
#
# # numbers.remove(True) # Удаляет выбранный элемент
#
# # numbers.clear() # Удаляет все
#
# print(numbers)

# ## Цикл со списком

# nums = [0, 1, 2,3,4,5, "50", False]
#
# for el in nums:
#     # el = el *2
#     el *= 2
#     print(el)

## Пользователь сам заполняет список (при этом изначально задает длину)

n = int(input("Введите длину списка: "))

user_list = []

i = 0

while i < n:
    string = "Enter element #" + str(i+1) + ": "
    user_list.append(input(string))
    i += 1

print(user_list)
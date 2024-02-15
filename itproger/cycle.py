# Цилы - конструкции, которые позволяют выполнять код несколько раз подряд (неограниченное количество раз).
## Существует 2 операторы циклов: "for" и "while"



# FOR - удобен, когда нам нужно "перебарть" определенный диапазон

## указываем оператор for и далее создаем некую переменную, пусть будет i.

## далее указываем дипазон цикла (пусть будет до 6 чисел) - in range(6). В таком случае значения будут начинаться с "0".
### Если хотим, чтобы числа шли, например, от 1, то прописываем -  range(1, 6)
### Также, можно указать на сколько будет увеличиваться следующий шаг - range(1, 6, 2)

## далее,внустри самого цикла будем каждый раз выводить нашу переменную i

# for i in range(6):
# for i in range(1, 6):
# for i in range(1, 6, 2):
#     print(i)

# count = 0
# word = "Hello World!"
# for i in word:
#     if i == "l":
#         count += 1 # каждый раз, когда в word встречается символ l, count увеличивается на +1
#
# print("Count:", count)




# While - удобен, когда нам нужно запустить "бесконечной" цикл


# i = 5
#
# while i < 15:
#     print(i)
#     i += 2


# isHasCar = True
#
# while isHasCar:
#     if input("Enter data: ") == "stop":
#         isHasCar = False

# break - оператор, который выходит из цикла

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# continue - оператор, который озволяет пропустить итерацию

# for i in range(1, 11):
#     if i % 2 == 0:      # как только мы находим четное число, мы пропускаем итерацию.
#         continue
#     print(i)





#####

# Задача - найти определенный символ в строке

found = None    # ничего не устанавливаем в переменную

for i in "Hello":
    if i == "Д":
        found = True
        break   # если его не прописать, то на этапе else мы пропишем в переменную found другое значение. А указав break мы явно указываем, что цикл завершен
else:
    found = False

print(found)
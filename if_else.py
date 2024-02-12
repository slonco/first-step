# Условные конструкции (оператор if / else)
###
# if - оператор "если"
###
# else:  - прописывается в конце условной конструкции, если применяется оператор if.
#
# Пример:
#     else:
#         print("")
###
# elif - оператор else-if, который позволяет прописать дополнительное условие
#
# Пример:
#     isHappy = True
#     userdata = int(input("Введите число: "))
#
#     if isHappy:
#         print("User is happy")
#     elif userdata == 5:
#         print("number is 5")
#     elif userdata == 3:
#         print("number is 3")
#     elif userdata == 1:
#         print("number is 1")
#     else:
#         print("Nope")
###
# В рамках оператора if можно проверять несколько условий (и / или)
#
# Пример:
#     isHappy = False
#     userdata = int(input("Введите число: "))
#
#     if isHappy and userdata ==2:
#         print("User is happy")
#     elif userdata == 5:
#         print("number is 5")
#     elif userdata == 3 and not isHappy:
#         print("number is 3")
#     elif userdata == 1:
#         print("number is 1")
#     else:
#         print("Nope")
###
# Тернарный оператор

data = input()

# if data == "Five":
#     number = 5
#
# else:
#     number = 0

# можно записать в одну строку:

number = 5 if data == "Five" else 0

print(number)
###
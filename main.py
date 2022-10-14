print("Задание 1")
while True:
    try:
        num = int(input("Введите число "))
        break
    except ValueError as e:
        print("Введен символ отличный от числа")
if num > 7:
    print("Привет")



print("\nЗадание 2")
name = input("Введите имя ")
if name.lower() == "вячеслав":
    print("Привет, Вячеслав")
else:
    print("Нет такого имени")


print("\nЗадание 3")
while True:
    try:
        string_of_numbers = input("Введите числа через пробел ").split(" ")
        list_of_numbers = list(map(int, list(string_of_numbers)))
        break
    except ValueError as e:
        print("Введены неверные данные, пожалуйста, введите числа через пробел")

final_list = []
for i in list_of_numbers:
    if i % 3 == 0:
        final_list.append(i)
print(final_list)

# Задание 4. Данная скобочная последовательность не является правильной. Если заменить предпоследнюю закрывающую
# квадратную  скобку на круглую закрывающую, то последовательность станет правильной

# Задача 2: Найдите сумму цифр трехзначного числа.

a = int(input("Введите трехзначное число: "))
b = 0
c = a
while c >= 1:
    b = b + c % 10
    c = c // 10
print (f'Сумма цифр числа {a} = {b}')


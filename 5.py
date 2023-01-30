# Задача 2: - HARD необязательная, идет за 3 обязательных. 
# Найдите сумму цифр любого вещественного или целого числа. 
# Можно использовать decimal. Через строку решать нельзя.
from decimal import Decimal

num = Decimal(input("Введите число: "))
a = num

while a != int(a):
    a = a * 10
    
b = 0
c = int(a)
while c >= 1:
    b = b + c % 10
    c = c // 10
print (f'Сумма цифр числа {num} = {b}')



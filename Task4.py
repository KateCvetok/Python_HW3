# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = int(input())
new_str = ''
while a > 0:
    new_str = str(a % 2) + new_str
    a //= 2
print(new_str)

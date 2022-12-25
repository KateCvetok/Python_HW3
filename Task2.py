# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

some_list = input().split()
new_list = []
for i in range(0, (len(some_list) - 1) // 2 + 1):
    new_list.append(int(some_list[i]) * int(some_list[len(some_list) -i - 1]))
print(new_list)
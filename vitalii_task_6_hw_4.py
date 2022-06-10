"""Удалить элемент из кортежа.
Входные данные: (1, 2, 3)
Результат: (1, 2)"""

user_input = (1, 2, 3)
user_list: list = list(user_input)
user_list.remove(3)
y = tuple(user_list)

print(y)

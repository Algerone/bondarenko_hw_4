"""
Написать программу которая данный список кортежей переведет в список списков
Входные данные: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Результат: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
"""

ex_list = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]  # list of tuples from example

fin_list = [list(i) for i in ex_list]  # list comprehension to change every element from tuple to list

print(fin_list)

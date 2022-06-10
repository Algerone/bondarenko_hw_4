"""Тема range
Есть последовательность от -99 до 99. Ее шаг 3. т.е. [-99, -96]
напечатать все элементы последовательности которые делятся на 3 без остатка.
напечатать в формате 'это <<ЧИСЛО>> делится без остатка на 3'
использовать метод редактирования строки f' строки"""

my_range = range(-99, 99)  # range from example

for i in my_range:  # check each element of the sequence
    if i % 3 == 0:  # check for divisibility by 3 without a remainder
        print(f"это {i} делится без остатка на 3")  # print every number using f-string method

"""Написать программу, которая подсчитывает количество символов в строке
и формирует dict в котором key = буква, value= количество их в слове:
Входная строка : 'Hillel school'
Результат :  {'H': 1, 'i': 1, 'l': 3, 'e': 1, ' ': 1, 's': 1, 'c': 1, 'h': 1, 'o': 2}"""

user_input: str = input('Enter your phrase\n')
user_list = list(user_input)
final_dict = {}

for i in user_list:
    key: str = i
    value: int = user_list.count(i)
    final_dict[key] = value
print(final_dict)

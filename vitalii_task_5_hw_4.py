"""Пользователь вводит через запятую последовательность слов например цвета или продукты.
Программа возвращает уникальные слова отсортированные по алфавиту.
Входные данные: red, white, black, red, green, black
Результат: black, green, red, white"""

user_data: str = "red, white, black, red, green, black".lower()
splited_data: list = user_data.split(", ")
user_set: set = set(splited_data)
sorted_by_alphabet = sorted(user_set)

print(sorted_by_alphabet)
user_name = input("Please enter your name\n")  # пользователь вводит имя

name_upper = user_name.upper()  # с помощью метода .upper получаем имя большими буквами
name_lower = user_name.lower()  # с помощью метода .lower получаем имя маленькими буквами

print("{0}, {1} ".format(name_upper, name_lower))  #выводим значение

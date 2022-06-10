user_string = input("Введите ваше слово\n")  #пользователь задает строку


while len(user_string) < 2:
    # проверяем с помощью цикла кол-во символов, если < 2, просим повторить ввод
    user_string = input(f"Строка слишком короткая - {user_string}, повторите ввод\n")

final_string = user_string[:2] + user_string[-2:]
# содиняем с помощью срезов 2 первых и 2 последних элемента
print(final_string)

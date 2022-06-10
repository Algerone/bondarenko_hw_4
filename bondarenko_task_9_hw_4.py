"""
Даны два списка элементов если хоть один елемент совпадает отпринтить True.
print(Тrue) не слово! а объект подставить.
"""

user_input = input('Enter first list\n')
user_input_2 = input('Enter second list\n')

for i in user_input:
    if i in user_input_2:
        print(True)
        break

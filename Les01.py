print('Первая прога')
print('Привет, программер!')
name = input('Ваше имя: ')

print(name, ', добро пожаловать в мир Python')

ans = input('Давайте поработаем? (Y/N)')

if 'Y':
    what = input(
        'Чем займемся? \n\n 1 - Кодим \n 2 - Фиксим \n 3 - Вычисляем \n')
    if what == 1:
        print('Отличный выбор! Кодить круто')
    elif what == 2:
        print('Будем исправлять рукожопство.')
    elif what == 3:
        print('Python - крутой калькулятор')
    else:
        print('Некорректный ввод!')

elif ((ans == 'Нет') or (ans == 'нет') or (ans == 'n') or (ans == 'N') or
        (ans == '2')):
    print('До свидания!')
else:
    print("Некорректный ввод")

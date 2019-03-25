import os
import sys
import psutil

print('Первая прога')
print('Привет, программер!')
name = input('Ваше имя: ')

print(name, ', добро пожаловать в мир Python')

ans = input('Давайте поработаем? (Y/N)')

if 'Y':
    choose = int(input(
        'Чем займемся? Я умею:\n\n 1 - выведу список файлов\n'
        '2 - выведу информацию о системе\n 3 - выведу список процессов\n'
        '4 - завершение программы\n'))
    if choose == 1:
        print(os.listdir())
    elif choose == 2:
        print('кодировка файловой системы:', sys.getfilesystemencoding())
        print('платформа операционной системы:', sys.platform.title())
        print('количество ядер процессора:', os.cpu_count())
        print('имя пользователя:', os.getlogin())
        print('имя текущей директории:', os.getcwd())
    elif choose == 3:
        print(psutil.pids())
    elif choose == 4:
        print('Программа завершена')
    else:
        print('Некорректный ввод!')

elif 'N':
    print('Программа завершена')
else:
    print("Некорректный ввод!")

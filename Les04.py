import os
import sys
import psutil
import shutil

print('Первая прога')
print('Привет, программер!')
name = input('Ваше имя: ')

print(name, ', добро пожаловать в мир Python')

ans = ''
while ans != 'q':
    ans = input('Давайте поработаем? (Y/N/q) ')
    if ans == 'Y':
        choose = int(input(
                     'Чем займемся? Я умею:\n\n'
                     ' 1 - выведу список файлов\n'
                     ' 2 - выведу информацию о системе\n'
                     ' 3 - выведу список процессов\n'
                     ' 4 - продублирую файлы в текущей директории\n'
                     ' 5 - проублирую указанные файлы\n'
                     ' 6 - удалю дубликаты в указанной директории\n'
                     ' Выберете действие: '))
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
            print('=Дублирование файлов в текущей директории=')
            file_list = os.listdir()  # создание списка файлов
            i = 0
            while i <= len(file_list):
                if i == len(file_list):
                    print('Выполено успешно! Созданы копии', i, 'файлов.')
                    break
                newfile = file_list[i] + '.dupl'
                shutil.copy(file_list[i], newfile)
                i += 1

        elif choose == 5:
            print('=Дублирование файлов, которые вы укажите=')
            dupl_files = ''
            while True:
                dupl_files = input('Введите название файла, который нужно'
                                   'дублировать, либо q для прекращения'
                                   'операции:\n')
                if dupl_files == 'q':
                    break  # прекащаем дублирование
                elif os.path.isfile()
                newfile = dupl_files + '.dupl'
                shutil.copy(dupl_files, newfile)
                print('Дублирование файлов выполено успешно!')
                continue

        elif choose == 6:
            print('=Удаление дубликаотов, в указанной директори=')
            directory = input('Введите путь к директори:\n')
            dir_files = os.listdir(directory)
            i = 0
            while i < len(dir_files):
                fullname = os.path.join(directory, dir_files[i])
                if fullname.endswith('.dupl'):
                    os.remove(fullname)
                    print('Удален файл:', dir_files[i])
                i += 1
            print('Удаление дубликатов выполено успешно!')

        else:
            print('Некорректный ввод!')

    elif ans == 'N':
        print()
    else:
        print('Программа завершена')

import os
import shutil
import sys


# import psutil

def duplicat_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print(f'Файл {newfile} успешно создан!')
        else:
            print("Возникли проблемы копирования")


def sys_info():
    print('кодировка файловой системы:', sys.getfilesystemencoding())
    print('платформа операционной системы:', sys.platform.title())
    print('количество ядер процессора:', os.cpu_count())
    print('имя пользователя:', os.getlogin())
    print('имя текущей директории:', os.getcwd())


def remove_duple(directory):
    dir_files = os.listdir(directory)
    count = 0
    for f in dir_files:
        fullname = os.path.join(directory, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                count += 1
            continue
    if count == 0:
        print('Дубликатов, оканчивающихся на .dupl нет')
    else:
        print('Удаление дубликатов выполено успешно! '
              f'Удалено {count} файлов')
    return count


def duble_files(dirname):
    file_list = os.listdir(dirname)  # создание списка файлов
    i = 0
    for f in file_list:
        fullname = os.path.join(dirname, f)
        duplicat_file(fullname)
        i += 1


def main():
    print('Первая прога')
    print('Привет, программер!')
    name = input('Ваше имя: ')

    print(name, ', добро пожаловать в мир Python')

    ans = ''
    while ans != 'q':
        ans = input('Давайте поработаем? (Y/N/q) ')
        if ans.lower() == 'y':
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
                sys_info()

            # elif choose == 3:
            #     print(psutil.pids())

            elif choose == 4:
                print('=Дублирование файлов в текущей директории=')
                print(f'Скопировано{duble_files(".")}')

            elif choose == 5:
                print('=Дублирование файлов, которые вы укажите=')
                while True:
                    filename = input('Введите название файла, который нужно '
                                     'дублировать, либо q для прекращения '
                                     'операции:\n')
                    if filename == 'q':
                        break  # прекащаем дублирование
                    duplicat_file(filename)

            elif choose == 6:
                print('=Удаление дубликаотов, в указанной директори=')
                directory = input('Введите путь к директори:\n')
                remove_duple(directory)

            else:
                print('Некорректный ввод!')

        elif ans == 'N':
            print()
        else:
            print('Программа завершена')


if __name__ == '__main__':
    main()

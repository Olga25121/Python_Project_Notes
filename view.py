import datetime
from random import choice
import controller as controller

commands = [
    'Создать заметку',
    'Показать все заметки',
    'Удалить заметку',
    'Редактировать заметку',
    'Выбрать заметки по дате',
    'Выход из программы'
]

def menu():
    print('\n Главное меню:')
    for i, line in enumerate(commands, 1):
        print(f'\t{i}. {line}')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 > choice > 7:
                return choice
            else:
                print('\nТакого пункта нет. Попытайтесь еще раз.')
        except ValueError:
             print('\nВведено неверное значение. Попробуйте еще раз. ')
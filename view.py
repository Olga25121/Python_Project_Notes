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

def create_note(new_id: int):
    date_note = datetime.datetime.now().strftime("%d.%m.%Y : %H.%M.%S")
    res = {'id': new_id, 'title': input('Заголовок заметки: '), 'msg': input('Содержание заметки: '), 'data_change': date_note}
    return res

def show_new_note(note: dict):
    print('\nНовая заметка:')
    print('ID: ' + str(note['id']) + '\n' + 'Заголовок: ' + note['title'] + '\n' + 'Содержание: ' + note['msg'] + '\n' + 
          'Дата создания/изменения: ' + note['data_change'])
    
def show_all(notes):
    print('\nЗаметки:')
    if len(notes) == 0:
        print('\tПока нет ни одной заметки')
    else:
        for note in notes:
            print('\nID: ' + str(note['id']) + '\n' + 'Заголовок: ' + note['title'] + '\n' + 'Содержание: ' + note['msg'] + '\n' + 
                  'Дата создания/изменения: ' + note['data_change'])
            
def select_del_note() -> int:
    while True:
        try:
            id_del = int(input('\nВыберите id заметки, которую хотите удалить: '))
            return id_del
        except ValueError:
            print('\nВведите число, пожалуйста. ')

def del_confirm(title: str):
    result = input(f'Вы действительно хотите удалить заметку "{title}"? (y/n): ').lower()
    if result == 'y':
        return True
    else:
        return False
    
def select_change_note() -> int:
    while True:
        try:
            id_note_change = int(input('\nВыберите id заметки, которую хотите изменить: '))
            return id_note_change
        except ValueError:
            print('\nВведите число, пожалуйста. ')

def modification_note(note_change: dict):
    print('Введите новые данные. При нажатии на Enter без ввода новых данных удаляются имеющиеся данные.')
    note_change['title'] = input('Новый заголовок: ')
    note_change['msg'] = input('Новое содержание: ')
    return note_change

def show_change_note(note: dict):
    print('\nИзмененная заметка:')
    print('ID: ' + str(note['id']) + '\n' + 'Заголовок: ' + note['title'] + '\n' + 'Содержание: ' + note['msg'] + '\n' + 
          'Дата создания/изменения: ' + note['data_change'])
    
def view_changes():
    print('\nИзменения внесены.')

def undo_changes():
    print('\nИзменения отменены. Возвращаемся в главное меню')


def find_date_note():
    find = input('\nУкажите, от какого числа ищем заметки в формате ДД.ММ.ГГГГ: ')
    return find


def find_error():
    print('\nЗаметок нет. Возможно, был неверно указан формат даты или нет заметок с указанной датой.')


def input_error():
    print('\nОшибка ввода. Нет заметки с таким ID.')


def exit_prog():
    print('\nПрограмма завершена. До свидания!')


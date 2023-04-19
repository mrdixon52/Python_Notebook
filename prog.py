import json 
import datetime

def print_menu():
    print("""
    ------------------------------------------------------------- \n
    Добро пожаловать в "Заметки"! \n
    Ниже представлен функционал программы. \n
    Впишите в терминал цифру для работы с соответвующей функцией! \n
    1 - Добавить заметку\n 
    2 - Вывести все заметки\n  
    3 - Найти и отредактировать заметку\n 
    4 - Удалить заметку\n 
    5 - Выход\n  
    ----------------------------------------------------------- \n 
    """)

def read_notes():
    with open(file_path, 'r', encoding='utf8') as open_book:
            notes = json.load(open_book)
    return notes

def save_notes(notes):
    with open(file_path, 'w', encoding='utf8') as open_book:
        json.dump(notes, open_book, indent=4)


file_path = "notebook.json"
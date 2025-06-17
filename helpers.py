import json
import os

from config import PATH


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_dict(data: dict, indent:int = 0):
    """
    Функция выводит словарь в читаемом виде

    Args:
        data(dict): словарь, который нужно вывести
        indent(int): Длина отступа для верхнего уровня вложенности
    """
    for key, value in data.items():
        print(' ' * indent + str(key)+':', end=' ')
        if isinstance(value, dict):
            print()
            print_dict(value, indent=4)
        else:
            print(value)

def menu_pause():
    input('Нажмите ENTER для продолжения')

def dump_data(new_data):
    with open (PATH, 'w') as f:
        json.dump(new_data, f, indent=4)

def yes_no(text:str) -> bool:
    """
    Функция запускает меню с выбором (y/n)

    Args:
        test(str): Текст для этого приглашения

    Returns:
        yes(bool): true - cошласие, false - отказ/невернный ввод
    """
    print(text)
    continue_tag = input('Продолжить? (y/n): ')
    if continue_tag == 'n' or continue_tag == 'N':
        return False
    elif continue_tag != 'y' and continue_tag != 'Y':
        print("Некорректный ввод!\nВы будете возвращены в меню")
        return False
    return True



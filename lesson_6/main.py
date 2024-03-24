''' Задание 1 - Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет '''

def yes_or_no(list):
    new_list = set()
    for num in list:
        if new_list.__contains__(num):
            print('Yes')
        else:
            print('No')
            new_list.add(num)
list = [1, 2, 3, 4, 5, 1, 2, 3]
yes_or_no(list)

''' Задание 2 - Написать функцию count_char, которая принимает строковое значение
STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
'буква': количество-вхождений-в-строку
}
например: {
'p': 2,
'y': 1,
}
STR_VAL = 'python is the fastest-growing major programming language'
Нельзя пользоваться collections.Counter! '''

STR_VAL = 'python is the fastest-growing major programming language'
def count_char(STR_VAL):
    new_dict = {}
    for char in STR_VAL:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    return new_dict
print(count_char(STR_VAL))

'''Задание 3 - Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"
Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__} '''

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'Выполнено {func.__name__}')
        return result
    return wrapper

name = input('Имя:')
@log_decorator
def hello(name):
    print(f'Привет, {name}')
hello(name)

''' Задание 4 - С помощью декораторов реализовать конвейер сборки бургера
Написать декоратор bread, который:
- до декорируемой функции будет печатать
"</------------\\>"
- после декорируемой функции будет
печатать "<\\____________/>"
Написать декоратор tomato, который:
- до декорируемой функции будет печатать
"*** помидоры ****"
Написать декоратор salad, который:
- до декорируемой функции будет
печатать "~~~~ салат ~~~~~"
Написать декоратор cheese, который:
- до декорируемой функции будет
печатать "^^^^^ сыр ^^^^^^"
Написать декоратор onion, который:
- до декорируемой функции будет
печатать "----- лук ------"
Написать функцию beef, которая:
- печатает "### говядина ###"
Написать функцию chicken, которая:
- печатает "|||| курица ||||" '''

def bread(func):
    def wrapper():
        print('</------------\\\\>')
        func()
        print('<\\\\____________/>')
    return wrapper

def tomato(func):
    def wrapper():
        print('*** помидоры ****')
        func()
    return wrapper

def salad(func):
    def wrapper():
        print('~~~~ салат ~~~~~')
        func()
    return wrapper

def cheese(func):
    def wrapper():
        print('^^^^^ сыр ^^^^^^')
        func()
    return wrapper

def onion(func):
    def wrapper():
        print('----- лук ------')
        func()
    return wrapper


@bread
@onion
@tomato
def beef():
    return '### говядина ###'


@bread
@cheese
@salad
def chicken():
    return '|||| курица ||||'

beef()
chicken()

'''
Task_4_1
Собрать с помощью декораторов гамбургер:
- булка
- лук
- помидоры
- говядина
- булка
'''
def bread(func):
    def wrapper():
        print('Булка')
        func()
    return wrapper

def onion(func):
    def wrapper():
        print('Лук')
        func()
    return wrapper

def tomato(func):
    def wrapper():
        print('Помидоры')
        func()
    return wrapper

def beef(func):
    def wrapper():
        print('Говядина')
        func()
    return wrapper


@bread
@onion
@tomato
@beef
@bread
def hamburger():
    pass
hamburger()

'''
Task_4_2
Собрать с помощью декораторов чикенбургер:
- булка
- сыр
- салат
- курица
- булка
'''
def bread(func):
    def wrapper():
        print('Булка')
        func()
    return wrapper

def cheese(func):
    def wrapper():
        print('Сыр')
        func()
    return wrapper

def salad(func):
    def wrapper():
        print('Салат')
        func()
    return wrapper

def chicken(func):
    def wrapper():
        print('Курица')
        func()
    return wrapper

@bread
@cheese
@salad
@chicken
@bread
def chickenburger():
    pass
chickenburger()

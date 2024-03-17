# 1
# Создать два списка произвольного содержания
list1 = [1,2,3,4]
list2 = ['a','b','c','d']

# Добавить к каждому списку по одному элементу в конец и в начало.
list1.insert(0, 0)
list1.append(5)
print(list1)

list2.insert(0, 'aa')
list2.append('dd')
print(list2)

# Расширить первый список вторым.
list1.extend(list2)
print(list1)

# 2
# Создать два списка, с одинаковым кол-вом элементов. Сделать из этих списков словарь.
list_1 = [1, 2]
list_2 = ['one', 'two']
dict_1 = dict(zip(list_1, list_2))
print(dict_1)

# 3
# Работа с Дзен Python.
# Количество строк: Определите количество строк в Дзене Питона.
zen_file = open('zen.txt', 'r')
zen_lenght = len(zen_file.readlines())
print(zen_lenght)

# Ключевые слова: Подсчитайте количество вхождений ключевых слов из Дзена Питона, таких как "is", "and", "or". Сложить в
# словарь такого типа {“is”: 4, “and”: None, “or”: 100}
zen_file = open('zen.txt').read()
count_is = zen_file.count('is')
count_and = zen_file.count('and')
count_or = zen_file.count('or')
print(count_is, count_and, count_or)

zen_dict = {}
zen_dict["is"] = count_is
zen_dict["and"] = count_and
zen_dict["or"] = count_or
print(zen_dict)

# Замена слова: Замените все вхождения слова "is" в Дзене Питона на "is not".
zen_file_upd = zen_file.replace('is', 'is not')
print(zen_file_upd)

# 1) В семье свадьба. Они решили выбрать заведение, где будут праздновать в
# зависимости от количества людей, которое прибудет к утру. Если их будет
# больше 50 - закажут ресторан
# если от 20 до 50 -то кафе,
# а если меньше 20 то отпраздную дома.

guests = int(input('enter guests:'))
if guests > 50:
    print('restaurant')
elif 50 >= guests >= 20:
    print('cafe')
else:
    print('home')

# 2) Ввести строку. Если длина строки больше 10 символов, то создать новую строку с 3
# восклицательными знаками в конце ('!!!') и вывести на экран. Если меньше 10, то
# вывести на экран второй символ строки

string = input('enter a string:')
if len(string) > 10:
    new_string = string + '!!!'
    print(new_string)
elif len(string) < 2:
    print('out of range')
else:
    print(string[1])

# 3) Получить на ввод количество рублей и копеек и вывести в правильной форме,
# например, 3 рубля, 1 рубль 25 копеек, 3 копейки

ruble = int(input('введите рубли:'))
penny = int(input('введите копейки:'))
if ruble == 0:
    rubles = ''
elif ruble == 1:
    rubles = '1 рубль'
elif ruble % 10 == 1 and ruble % 100 != 11:
    rubles = f'{ruble} рубль'
elif ruble % 10 in [2, 3, 4] and ruble % 100 not in [12, 13, 14]:
    rubles = f'{ruble} рубля'
else:
    rubles = f'{ruble} рублей'
if penny == 0:
    pennies = ''
elif penny == 1:
    pennies = '1 копейка'
elif penny % 10 == 1 and penny % 100 != 11:
    pennies = f' {penny} копейка'
elif penny % 10 in [2, 3, 4] and penny % 100 not in [12, 13, 14]:
    pennies = f' {penny} копейки'
else:
    pennies = f' {penny} копеек'
print(rubles+pennies)

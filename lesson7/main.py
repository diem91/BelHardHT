'''Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на
экран. Создать объект класса Dog, вызвать все методы объекта и вывести на
экран все его атрибуты.'''
class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f'{self.name} jump')
    def run(self):
        print(f'{self.name} run')
    def bark(self):
        print(f'{self.name} bark')

dog = Dog(height=30, weight=20, name='my_dog', age=3)

dog.jump()
dog.run()
dog.bark()

print(dog.height)
print(dog.weight)
print(dog.name)
print(dog.age)

'''Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и
меняет атрибут имени у объекта. Создать один объект класса. Вывести имя.
Вызвать метод change_name. Вывести имя.'''

class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f'{self.name} jump')
    def run(self):
        print(f'{self.name} run')
    def bark(self):
        print(f'{self.name} bark')

    def change_name(self, new_name):
        self.name = new_name

dog = Dog(height=30, weight=20, name='my_dog', age=3)
print(f'name: {dog.name}')
dog.change_name('my_dog_1')
print(f'new name: {dog.name}')

'''Создать класс Phone, у которого будут следующие атрибуты:
Определить атрибуты
- brand - бренд
- model - модель
- issue_year - год выпуска
Определить методы:
- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит
{name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}'''

class Phone:
    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, caller_name):
        print(f'Звонит {caller_name}')

    def get_info(self):
        return (self.brand, self.model, self.issue_year)

    def __str__(self):
        return (f'Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}')

phone = Phone('Samsung', 'Galaxy S22', 2022)
phone.receive_call('Dmitry')
print(phone)

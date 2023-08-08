# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

import math

class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_curcult(self):
        return math.pi * self._radius * 2

    def get_area(self):
        return math.pi * (self._radius ** 2)


n = Circle(7)
print(n.get_curcult())
print(n.get_area())

# -----------------------------------------------------------------------------------------
# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle:

    def __init__(self, height: int, width=None):
        self.height = height
        if width:
            self.width = width
        else:
            self.width = height

    def get_perimeter(self):
        return 2 * (self.height + self.width)


    def get_area(self):
        return self.width * self.height

rectangle1 = Rectangle(5, 2)
rectangle2 = Rectangle(7)

print(f'{rectangle1.get_perimeter() = },  {rectangle1.get_area() = }')
print(f'{rectangle2.get_perimeter() = },  {rectangle2.get_area() = }')

# ----------------------------------------------------------------------------------------------
# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person:

 def __init__ (self, last_name, first_name, surname, age):
    self.last_name = last_name
    self.first_name = first_name
    self.surname = surname
    self.__age = age

 def get_age(self):
    return self.__age

 def get_birth(self):
    self.__age += 1

 def full_name(self):
    return f'{self.last_name} {self.first_name} {self.surname}'

if __name__ == '__main__':
   p_1 = Person ('Иванов', 'Иван', 'Иванович', 30)

print(p_1.full_name())
p_1.get_birth()
print(p_1.get_age())

# ------------------------------------------------------------------------------
# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from random import randint


class Human:

 def __init__(self, first_name, last_name, age):
   self.first_name = first_name
   self.last_name = last_name
   self.__age = age

 def get_age(self):
   return self.__age

 def birthday(self):
   self.__age += 1

 def get_full_name(self):
   return f'{self.first_name} {self.last_name}'


class Employee(Human):

 def __init__(self, first_name, last_name, age, id_num):
   super().__init__(first_name, last_name, age)
   if (99999 < id_num) and (id_num < 10000000):
     self.id_num = id_num
   else:
     self.id_num = randint(100000, 999999)

 def set_level(self):
   return sum([int(item) for item in str(self.id_num)]) % 7


if __name__ == '__main__':
  spam = Employee('Smit', 'Jon', 33, 89)
print(f'{spam.id_num = }')
print(f'{spam.set_level() = }')

# ------------------------------------------------------------------
# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Animals:

 def __init__(self, name):
   self.name = name
 
 def animal_name(self):
   return f'Имя: {self.name}'

class Fish(Animals):
  def __init__(self, name, depth):
    super().__init__(name)
    self.depth = depth
  def get_info(self):
    return f'Глубина обитания: {self.depth} m '

class Birds(Animals):
  def __init__(self, name, wingspan):
    super().__init__(name)
    self.wingspan = wingspan
  def get_info(self):
    return f'Размах крыльев: {self.wingspan} sm '

class Reptiles(Animals):
  def __init__(self, name, length):
    super().__init__(name)
    self.length = length

  def get_info(self): 
    return f'Длина тела: {self.length} m '
  
class Cat(Animals):
  def __init__(self, name, breed):
    super().__init__(name)
    self.breed = breed

  def get_info(self):
    return f'Порода: {self.breed}'
  
# if __name__ == '__main__':
#   fish = Fish('Som', 5)
#   bird = Birds('Parrot', 10)
#   reptile = Reptiles('Anaconda', 3)
# print(fish.animal_name())
# print(fish.get_info())
# print(bird.animal_name())
# print(bird.get_info())
# print(reptile.animal_name())
# print(reptile.get_info())

class AnimalFactory:
    def __init__(self):
      self.animal_classes = {
        'Cat': Cat,
        'Reptiles': Reptiles,
        'Fish': Fish,
        'Birds': Birds     
        }
      
    def make_animal(self, animal_type, *args):
        if animal_type not in self.animal_classes:
          raise ValueError('Неправильный тип')
        
        animal_classes = self.animal_classes[animal_type]
        return animal_classes(*args)
      


if __name__ == '__main__':
    factory = AnimalFactory()
    
    cat = factory.make_animal('Cat', 'murzik', 'metiz')
    reptile = factory.make_animal('Reptiles', 'lizard', 0.8)
    fish = factory.make_animal('Fish', 'kloun', 1.4)
    bird = factory.make_animal('Birds', 'eagle', 1.5)

    print(fish.get_info())
    print(reptile.get_info())
    print(bird.get_info())
    print(cat.get_info())

# -----------------------------------------------------------------------------
# Возьмите 1-3 любые задачи из прошлых семинаров которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.
#  
#  Треугольник существует только тогда, когда сумма любых двух его сторон
#  больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
#  Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
#  Если хотя бы в одном случае отрезок окажется больше суммы двух других,
#  то треугольника с такими сторонами не существует. Отдельно сообщить
#  является ли треугольник разносторонним, равнобедренным или равносторонним.

class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def check(self):
        if self.a > self.b + self.c or self.b > self.a + self.c \
                or self.c > self.a + self.b:
            return f"Треугольника с такими сторонами не существует"
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return f"Треугольник разносторонний"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return f"Треугольник равнобедренный"


test = Triangle(1, 2, 3)
print(test.check())
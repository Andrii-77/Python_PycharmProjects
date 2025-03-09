# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

from typing import Self


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, other: Self):
        return self.area + other.area

    def __sub__(self, other: Self):
        return self.area - other.area

    def __eq__(self, other: Self):
        return self.area == other.area

    def __ne__(self, other: Self):
        return self.area != other.area

    def __lt__(self, other: Self):
        return self.area < other.area

    def __gt__(self, other: Self):
        return self.area > other.area

    def __len__(self):
        return (self.x + self.y) * 2


rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(7, 6)

print(rectangle1 + rectangle2)
print(rectangle1 - rectangle2)
print(rectangle1 == rectangle2)
print(rectangle1 != rectangle2)
print(rectangle1 < rectangle2)
print(rectangle1 > rectangle2)
print(len(rectangle1))
print('*' * 40)


# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    def __str__(self):
        return str(self.__dict__)

    @classmethod
    def get_count(cls):
        print(cls.__count)


class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cinderella(self, cinderella_list: list[Cinderella]):
        for cinderella in cinderella_list:
            if cinderella.foot_size == self.shoe_size:
                print(cinderella)


cind_list: list[Cinderella] = [
    Cinderella('Anna', 20, 30),
    Cinderella('Lili', 21, 31),
    Cinderella('Bonna', 22, 32),
    Cinderella('Sofija', 23, 33),
    Cinderella('Rosa', 24, 34)
]
prince = Prince('Zorg', 26, 33)

prince.find_cinderella(cind_list)

Cinderella.get_count()
print('*' * 40)

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazines()
#     print('-' * 40)
#     Main.show_all_books()

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):

    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'This is book {self.name}')


class Magazine(Printable):

    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'This is magazine {self.name}')


class Main:
    __printable_list: list[Printable] = []

    @classmethod
    def add(cls, item: Book | Magazine):
        if isinstance(item, (Book, Magazine)):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Book('Book-4'))
Main.add(Magazine('Magazine-3'))
Main.add(Book('Book-2'))
Main.add(Magazine('Magazine-4'))
Main.add(Book('Book-3'))
Main.add('Figna jaka ne maje projty - 2')
Main.add(Magazine('Magazine-5'))
Main.add('Figna jaka ne maje projty - 3')
Main.add(Book('Book-1'))
Main.add('Figna jaka ne maje projty - 1')
Main.add(Magazine('Magazine-2'))
Main.add(Book('Book-5'))
Main.add(Magazine('Magazine-1'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
print('*' * 40)

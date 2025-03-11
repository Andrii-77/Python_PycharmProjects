# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com
# (Хеш то що з ліва записувати не потрібно)

try:
    with open('emails.txt') as source, open('gmail.txt', 'w') as target:
        for line in source:
            email = line.split()[-1]
            if email.endswith('gmail.com'):
                # target.write(f'{email}\n')
                print(email, file=target)  # запис файлу за допомогою прінта, прінт зразу додає перенос строки.
except Exception as e:
    print(e)
print('-' * 20)

# ----------------------------------------------------------------------------------------------------------------

# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

import json


class Purchases:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__purchases = []
        self.__read_file()
        self.__id = self.__gen_id()

    def __show_all(self):
        print('*' * 20)
        for purchase in self.__purchases:
            print(f'{purchase['id']}) {purchase['name']} - {purchase['price']}')
        print('*' * 20)

    def __add(self):
        name = input('Name: ')
        while True:
            try:
                price = float(input('Enter price: '))
                break
            except ValueError:
                pass

        new_purchase = {'id': next(self.__id), 'name': name, 'price': price}
        self.__purchases.append(new_purchase)
        self.__write_file()

    def __find_by(self):
        value = input("Enter value: ")

        for purchase in self.__purchases:
            if value in purchase.values() or (value.isdigit() and float(value) in purchase.values()):
                print(purchase)

    def __write_file(self):
        try:
            with open(self.__file_name, mode="w") as file:
                json.dump(self.__purchases, file)
        except Exception as e:
            print(e)

    def __most_expensive(self):
        print(max(self.__purchases, key=lambda x: x['price']))

    def __delete_by_id(self):
        self.__show_all()

        while True:
            try:
                _id = int(input('Enter id: '))
                break
            except ValueError:
                pass

        index = next((i for i, v in enumerate(self.__purchases) if v['id'] == _id), None)

        if index:
            del self.__purchases[index]
            self.__write_file()
            return

        print('Error, there is no such ID.')

    def menu(self):
        while True:
            print('1). Показати всі покупки.')
            print('2). Додати покупку.')
            print('3). Пошук по значенням.')
            print('4). Найдорожча покупка.')
            print('5). Видалення по ID.')
            print('9). Вихід.')

            choice = input("Enter your choice: ")
            match choice:
                case '1':
                    self.__show_all()
                case '2':
                    self.__add()
                case '3':
                    self.__find_by()
                case '4':
                    self.__most_expensive()
                case '5':
                    self.__delete_by_id()
                case '9':
                    return  # можна дати break

    def __read_file(self):
        try:
            with open(self.__file_name) as file:
                self.__purchases = json.load(file)
        except (Exception,):
            self.__write_file()

    def __gen_id(self):
        _id = self.__purchases[-1]['id'] + 1 if self.__purchases else 1
        while True:
            yield _id
            _id += 1


# purchases = Purchases('p1.json')

# purchases.add()
# purchases.find_by()

# purchases.menu()
# ---------------------------------------------------------------------------------------------------------------

# 3) Є ось такий список:
# data = [
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1111, "field": {}},
#         {"id": 1112, "field": {}},
#         {"id": 1113, "field": {}},
#         {"id": 1114, "field": {}},
#         {"id": 1115, "field": {}},
#     ],
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1120, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1123, "field": {}},
#         {"id": 1124, "field": {}},
#         {"id": 1125, "field": {}},
#
#     ],
#     [
#         {"id": 1130, "field": {}},
#         {"id": 1131, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1132, "field": {}},
#         {"id": 1133, "field": {}},
#
#     ]
# ]
#
# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122, .......]

data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]


def cut(arr):
   res = []
   gens = [(i['id'] for i in item if i['id'] not in res) for item in arr]
   while gens:
       gen = gens.pop(0)
       try:
           res.append(next(gen))
           gens.append(gen)
       except StopIteration:
           pass
   return res


print(cut(data))

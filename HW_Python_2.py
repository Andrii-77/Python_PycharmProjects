# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи


def notebook():
    todo_list = []

    def add_todo(todo):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all():
        return todo_list

    return [add_todo, get_all]


add_todo, get_all = notebook()
add_todo('football')
print(get_all())
add_todo('tea')
print(get_all())
#-------------------------------------------------------------------------------------------------------
def notebook_mentor():
    todo_list = []

    def add_todo(todo):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all():
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all


add1, get_all1 = notebook_mentor()
add2, get_all2 = notebook_mentor()

add1('apple')
add2('HP')
add1('go to home')

print(get_all1())
print('********************************')
print(get_all2())
#-------------------------------------------------------------------------
print('###############################')


# 2) протипізувати перше завдання

from typing import List, Callable


def notebook() -> List[Callable[[str], None] | list[str]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        return todo_list

    return [add_todo, get_all]


add_todo, get_all = notebook()
add_todo('football')
add_todo('tea')
add_todo('golf')
print(get_all())
#--------------------------------------------------------------------------
from typing import Callable
# def notebook_mentor() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
def notebook_mentor():
    todo_list: list[str] = []

    def add_todo(todo:str):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all


add1, get_all1 = notebook_mentor()
add2, get_all2 = notebook_mentor()

add1('apple')
add2('HP')
add1('go to home')

print(get_all1())
print('********************************')
print(get_all2())
#--------------------------------------------------------------------------
print('###############################')


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(num: int) -> str:
    num_in_str = str(num)
    arr = []
    for i in range(len(num_in_str)):
        number = num_in_str[i]
        if number != "0":
            arr.append(number + '0' * (len(num_in_str) - i - 1))
    # print(arr)
    result = '+'.join(arr)
    print(result)
    return result


# Якщо не знати join, то можна це прописати трохи інакше:
#     result = ""
#     for i in arr:
#         if result:
#             result += "+" + i
#         else:
#             result = i
#     print(result)

expanded_form(12)
expanded_form(42)
expanded_form(70304)
#---------------------------------------------------------------------------
def expanded_form_mentor(num: int) -> str:
    st = str(num)
    length = len(st) - 1
    res = []
    for i, ch in enumerate(st):
        if ch != "0":
            res.append(ch + '0' * (length - i))
    return ' + '.join(res) + f' = {st}'


print(expanded_form_mentor(12))
print(expanded_form_mentor(42))
print(expanded_form_mentor(70304))
#---------------------------------------------------------------------------
print('###############################')


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій

def decor(func):
    counter = 0

    def inner():
        nonlocal counter
        counter += 1
        print('count: ', counter)
        func()

    return inner


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func1()
func1()
func2()
func1()
#--------------------------------------------------------------------------
def count_decor_mentor(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(f'{count=}')
    return inner


@count_decor_mentor
def func1():
    print('f1')


@count_decor_mentor
def func2():
    print('f2')

func1()
func1()
func2()
func1()

#---------------------------------------------------------------------------
print('###############################')

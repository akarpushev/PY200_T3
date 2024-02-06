# А если в дочернем классе, после переопределения метода **`__init__`**
# все равно необходимо вызвать конструктор базового класса?
#
# В таком случае необходимо воспользоваться встроенной функцией **`super()`**.
#
# **`super()`** эквивалентно переменной `cls`, только на родительский класс.

class BaseClass:
    def __init__(self):
        print(f'Вызван конструктор базового класса')


class SubClass(BaseClass):
    def __init__(self):
        print(f'Вызван конструктор дочернего класса')

b = BaseClass()
s = SubClass()
print()

class BaseClass:
    def __init__(self):
        print(f'Вызван конструктор базового класса')


class SubClass(BaseClass):
    def __init__(self):
        super().__init__()  # вызывает метод родительского класса
        print(f'Вызван конструктор дочернего класса')

b = BaseClass()
s = SubClass()
class A:
    ...

class B(A):  # наследуемся от A
    ...

print(A.mro())  # [<class '__main__.A'>, <class 'object'>]
print(B.mro())  # [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]


class A:
    ...

class B:
    ...

class C(A, B):  # наследуемся от A и B. Поиск методов при множественном наследовании слева направо
    ...

print(C.mro())  # [__main__.C, __main__.A, __main__.B, object]
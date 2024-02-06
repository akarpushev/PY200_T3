class Photo:
    def photo(self):
        print("photo")

class Video:
    def video(self):
        print("video")

class Call:
    def call(self):
        print("call")

class BasePhone:
    def __init__(self, display, color):
        self.display = display
        self.color = color

class Phone1(BasePhone, Call, Video):
    pass

a = Phone1("abc", "black")
print(a.display, a.color, a.video(), a.call())

class Photo2(Phone1, Photo):
    pass

class A:
    data = 22
    def func(self):
        print("AAA")

class B:
    data = 33
    def func(self):
        print("BBB")

class C(A, B):
    pass

c = C()
print(c.func(), c.data)
print(C.mro())

class D(B, A):
    def func(self): # перезаписали функцию
        super().func() # выясняем откуда, из B или A
        print("DDD")

d = D()
print(d.func())
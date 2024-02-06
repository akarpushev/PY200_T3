class PaperBook:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Книга "{self.name}"'


class EBook(PaperBook):
    def __init__(self, name: str):
        self.format = "pdf"

print(PaperBook("Букварь"))
...  # TODO инициализировать экземпляр электронной книги

book = EBook('book')
print(book.format)


class PaperBook:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Книга "{self.name}"'

class EBook(PaperBook):
    def __init__(self, name: str):
        super().__init__(name)  # вызываем конструктор базового класса
        self.format = "pdf"

print(EBook("Букварь"))

# Не важно с какими атрибутами вы работаете.
# При наследовании и расширение конструктора базового класса
# лучше перестраховаться и вызывать его, чтобы верно
# проинициализировать ваш объект после наследования.
#
# Вы можете не знаете, что скрыто в конструкторе базового класса и
# какие действия там выполняются.
# Даже если и знаете, **то не нужно их повторно воспроизводить**!!
# Вызывайте конструктор базового класса!



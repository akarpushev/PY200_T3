class PaperBook:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

class EBook(PaperBook):  # наследуемся от PaperBook
    ...

ebook = EBook("Букварь")
print(ebook)


class PaperBook:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f'PaperBook({self.name!r})'  # TODO переделать метод, чтобы унаследовать его

class EBook(PaperBook):  # наследуемся от PaperBook
    ...

print(PaperBook("Букварь"))  # PaperBook('Букварь')
print(EBook("Букварь"))  # EBook('Букварь')


class PaperBook:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r})'

class EBook(PaperBook):  # наследуемся от PaperBook
    ...

ebook = EBook("Букварь")
print(ebook)

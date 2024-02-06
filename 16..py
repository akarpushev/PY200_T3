class IdCounter:
    def __init__(self, id):
        self.id = id


class Password:
    def __init__(self, password):
        self.password = None
        self.check(password)

    def check(self, password):
        if not isinstance(password, str):
            raise TypeError
        if len(password) < 8:
            raise ValueError
        self.password = password


class Product(IdCounter):
    def __init__(self, id, name, price, rating):
        super().__init__(id)
        self.__id = id
        self.__name = name
        if not isinstance(price, float):
            raise TypeError
        if not isinstance(rating, int):
            raise TypeError
        self._price = price
        self.rating = rating

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    def __str__(self):
        return f"{self.__id}_{self.__name}"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.__id}, name={self.__name})"

class Cart:
    def __init__(self, id):

    cart = []
    def add_to_cart(self, id):
        if id:


    # def view_in_cart(request) -> dict:
    #     if os.path.exists('cart.json'):  # Если файл существует
    #         with open('cart.json', encoding='utf-8') as f:
    #             return json.load(f)
    #     # cart = {'products': {}}  # Создаём пустую корзину
    #     user = get_user(request).username
    #     cart = {user: {'products': {}}}
    #     with open('cart.json', mode='x', encoding='utf-8') as f:  # Создаём файл и записываем туда пустую корзину
    #         json.dump(cart, f)
    #     return cart

    # def add_to_cart(request, id_product: str):
    #     # cart = view_in_cart()
    #     cart_users = view_in_cart(request)
    #     cart = cart_users[get_user(request).username]
    #     if id_product in cart["products"]:
    #         if id_product in DATABASE.keys():
    #             cart['products'][id_product] += 1
    #     else:
    #         if id_product in DATABASE.keys():
    #             cart['products'][id_product] = 1
    #     with open('cart.json', mode='w', encoding='utf-8') as f:
    #         # json.dump(cart, f)
    #         json.dump(cart_users, f)
    #     return True
    #
    # def remove_from_cart(request, id_product: str) -> bool:
    #     # cart = view_in_cart()
    #     cart_users = view_in_cart(request)
    #     cart = cart_users[get_user(request).username]
    #     if id_product in cart["products"]:
    #         del cart['products'][id_product]
    #         with open('cart.json', mode='w', encoding='utf-8') as f:
    #             # json.dump(cart, f)
    #             json.dump(cart_users, f)
    #     else:
    #         return False
    #     return True

class User(Cart):
    def __init__(self, username, password):
        self.id = id
        self.__username = username
        self.password = password
        self.__cart = []



book = Product('1', '5', 6.0, 77)
print(book)
# print([PaperBook('a', 's', i) for i in range(1, 5, 1)])
book.__name = 'aa'
book.__name = 'aa'
# print(book)
book.price = 30
print(book._price)




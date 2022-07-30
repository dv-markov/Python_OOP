# Структура данных для ERP
from datetime import date


# def extract_object(obj, sep='\n', linebreak=True, tags=''):
#     return (tags[0] if tags else '') + \
#            sep.join(f'{key}: {value}' for key, value in obj.__dict__.items()) + \
#            (tags[1] if tags else '') + \
#            ('\n' if linebreak else '')


def extract_object(obj, sep='\n', linebreak=True, tag_open='', tag_close=''):
    return tag_open + \
           sep.join(f'{key}: {value}' for key, value in obj.__dict__.items()) + \
           tag_close + \
           ('\n' if linebreak else '')


class Cart:
    """Класс для описания "корзины", т.е. содержания счета или ТКП
    """
    __CART_NUMBER_COUNTER = 0

    def __init__(self, *items):
        self.cart_number = self.__get_cart_number()
        self.rev = 0
        self.cart_date = date.today()
        # self.cart_date = date.today().isoformat()
        self.item_list = list(items)
        self.cart_total = self.__get_cart_total()

    @classmethod
    def __get_cart_number(cls):
        cls.__CART_NUMBER_COUNTER += 1
        return f'{cls.__CART_NUMBER_COUNTER:09}'

    def __get_cart_total(self):
        total_sum = 0
        for item in self.item_list:
            total_sum += item.get_total()
        return total_sum

    def __repr__(self):
        return extract_object(self)

    def add_item(self, cart_item_object):
        if isinstance(cart_item_object, CartItem):
            self.item_list.append(cart_item_object)
            self.cart_total = self.__get_cart_total()

class CartItem:
    """Класс для описания позиции в счете или ТКП
    """
    def __init__(self, product: object, tag: str = '', qty: int = 0, price: int = 0, unit: str = 'pcs'):
        self.product = product
        self.tag = tag
        self.qty = qty
        self.unit = unit
        self.price = price
        self.total = self.qty * self.price

    def __str__(self):
        return extract_object(self, ' | ', False, '{', '}')

    def __repr__(self):
        return extract_object(self, ' | ', False, '\n{', '}')

    def get_total(self):
        return self.total


class Product:
    """Класс для описания продукта
    """
    __ART_CODE_COUNTER = 0

    def __init__(self, name=None, art_code=None, bom=None):
        self.name = name
        self.product_type = self.__class__.__name__
        self.art_code = art_code if art_code else self.__get_art_code()
        self.bom = list(bom) if bom else []

    @classmethod
    def __get_art_code(cls):
        cls.__ART_CODE_COUNTER += 1
        return f'{cls.__ART_CODE_COUNTER:08}'

    def __str__(self):
        return extract_object(self, ', ', False, '{', '}')


class Valve(Product):
    def __init__(self, name, DN, PN, art_code=None, bom=None):
        super().__init__(name, art_code, bom)
        self.DN = DN
        self.PN = PN


print(Product.__doc__)
pr1 = Product()
print(pr1.__dict__)
print(pr1)
print(extract_object(pr1))

pr2 = Product('Valve 3241 DN50 PN40')
print(extract_object(pr2))


print(CartItem.__doc__)
ci1 = CartItem(pr2, 'PCV-123', 5, 100)
print(ci1)
print(extract_object(ci1))

ci2 = CartItem(Product('8582-0310'), '-', 10, 2)
print(extract_object(ci2))

ci3 = CartItem(Valve('3251', 100, 160, bom=['body', 'bonnet', 'seat', 'plug']), 'FCV-3020', 1, 1000)
print(extract_object(ci3))

print(Cart.__doc__)
cart1 = Cart()
print(cart1.__dict__)
print(extract_object(cart1))

cart2 = Cart(ci1, ci2)
print(extract_object(cart2))

cart2.add_item(ci3)
print(cart2)

# как изменить порядок инициализации свойств в экземплярах дочерних классов?
# описание продукта клапан (Valve(Product)) нужно сделать: name, type, DN, PN, art_code, bom


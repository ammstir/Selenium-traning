import random
import string


class Generators:

    def __init__(self, app):
        self.app = app

    def email(self):
        symbols = string.ascii_letters + string.digits
        email = "".join([random.choice(symbols).lower() for i in range(1, 10)]) + "@me.ru"
        return email

    def password(self):
        symbols = string.ascii_letters + string.digits
        password = "".join([random.choice(symbols) for i in range(1, 10)])
        return password

    def name(self):
        symbols = string.ascii_letters
        name = ("".join([random.choice(symbols) for i in range(5, 10)])).capitalize()
        return name

    def address(self):
        symbols = string.ascii_letters
        address = ("".join([random.choice(symbols) for i in range(10, 15)])).capitalize()
        return address

    def phone(self):
        phone = "".join([random.choice(string.digits) for i in range(11)])
        return phone

    def postcode(self):
        postcode = "".join([random.choice(string.digits) for i in range(5)])
        return postcode

    def itemcode(self):
        symbols = string.ascii_letters + string.digits
        itemcode = "".join([random.choice(symbols) for i in range(5)])
        return itemcode

    def random_string(self, n):
        symbols = string.ascii_letters + string.digits
        random_string = "".join([random.choice(symbols) for i in range(1, n)])
        return random_string

    def random_numbers(self, n):
        random_numbers = random.choice(range(1, n))
        return random_numbers

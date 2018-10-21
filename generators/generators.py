import random
import string


def email():
    symbols = string.ascii_letters + string.digits
    s = "".join([random.choice(symbols).lower() for i in range(1, 10)]) + "@me.ru"
    return s


def password():
    symbols = string.ascii_letters + string.digits
    s = "".join([random.choice(symbols) for i in range(1, 10)])
    return s


def name():
    symbols = string.ascii_letters
    s = ("".join([random.choice(symbols) for i in range(5, 10)])).capitalize()
    return s


def address():
    symbols = string.ascii_letters
    s = ("".join([random.choice(symbols) for i in range(10, 15)])).capitalize()
    return s


def phone():
    s = "".join([random.choice(string.digits) for i in range(11)])
    return s


def postcode():
    s = "".join([random.choice(string.digits) for i in range(5)])
    return s


def itemcode():
    symbols = string.ascii_letters + string.digits
    s = "".join([random.choice(symbols) for i in range(5)])
    return s


def random_string(n):
    symbols = string.ascii_letters + string.digits
    s = "".join([random.choice(symbols) for i in range(1, n)])
    return s


def random_numbers(n):
    s = random.choice(range(1, n))
    return s

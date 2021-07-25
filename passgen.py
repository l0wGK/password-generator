import random
import string
import pyperclip

def generate(int):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + '@&_-*#£$€%+?!') for _ in range(int))

def copy(variable):
    pyperclip.copy(variable)

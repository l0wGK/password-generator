import random
import string
import pyperclip

while True:
    numChar = int(input("Password length: "))
    password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + '@&_-*#£$€%+?!') for _ in range(numChar))
    pyperclip.copy(password)
    print("Password copied to clipboard")

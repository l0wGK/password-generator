while True:
    numChar = input("# of characters in password:")
    numChar = int(numChar)
    password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + '@&_-*#£$€%+?!') for _ in range(numChar))
    print("Password copied to clipboard")

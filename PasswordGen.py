import passgen

p = passgen

while True:
    num = int(input("Password length: "))
    if num >= 51 or num <= 7:
        print("Password length must be between 8-50 characters")
    password = p.generate(num)
    p.copy(password)
    print("Password copied to clipboard")
correct_password = "1234"

while True:
    password = input("Введите четырехзначное число в качестве пароля: ")
    if password == correct_password:
        print("Пароль введен правильно.")
        break
    else:
        print("Неверный пароль. Попробуйте снова.")

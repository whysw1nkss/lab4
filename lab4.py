#задаем правильный пароль
correct_password = "1234"

#запускаем цикл проврки пароля
while True:
    password = input("Введите четырехзначное число в качестве пароля: ")
    if password == correct_password:
        print("Пароль введен правильно.")
        break
    else:
        print("Неверный пароль. Попробуйте снова.")

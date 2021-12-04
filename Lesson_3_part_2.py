def userinfo(name, family_name, city, birth, email, phone_number):
    print(
        f"Потльзователь {name} {family_name} живет в городе {city}, родился в {birth} году, номер телефона: {phone_number}, email: {email}.")


userinfo(family_name="Сидоров", email="ya@ya.ru", name="Иван", city="Москва", birth=1972, phone_number="+79232900252")

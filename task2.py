def gradusnik(a):
    if operator == "1":
        print(((peremennaya-32)/1.8), "Цельсий")
    elif operator == "2":
        print(((peremennaya*1.8)+32),"Фаренгейт")
print("Что вы желаете сделать?")
print("1.Фаренгейты в цельсий")
print("2.Цельсий в фаренгейты")
operator = input("(1 или 2):")
peremennaya = int(input("Введите ваше значение:"))
gradusnik(operator)
gradusnik(peremennaya)
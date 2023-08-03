

number = input("Введите число: ")
try:
    if float(number) > 7:
        print("Привет")
    else:
        print("Введенное число не больше чем 7")
except ValueError:
    print("Число введено некорректно")
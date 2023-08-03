

numbers = input('Введите числа через пробел: ')
try:
    numberArray = [int(number) for number in numbers.split()]
    resultMsg = str()
    for number in numberArray:
        if number % 3 == 0:
            resultMsg += (f'{number} ' '')
    print(resultMsg)
except ValueError:
    print('Нужно вводить только целые числа')
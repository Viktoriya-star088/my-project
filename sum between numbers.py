def sum_between_numbers(num1, num2):
    total_s = sum(range(num1, num2 + 1))
    return total_s

try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))

    result = sum_between_numbers(number1, number2)
    print(f"Сумма всех чисел между {number1} и {number2} равна {result}")
except ValueError:
    print("Пожалуйста, введите действительные целые числа.")

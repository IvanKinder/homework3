def my_func(a, b, c):
    digits = [a, b, c]
    digits = sorted(digits)
    return digits[1] + digits[2]


print("Сумма наибольших двух = ", my_func(float(input("Введите первое число: ")), float(input("Введите второе число: ")),
              float(input("Введите третье число: "))))

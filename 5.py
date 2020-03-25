def my_func():
    float_digits = []
    flag = False
    while True:
        print ("Введите Q чтобы выйти из программы!")
        digits = input("Введите числа через пробел: ").split()
        for digit in digits:
            if digit.isdigit():
                float_digits.append(float(digit))
            elif digit == 'Q' or digit == 'q':
                flag = True
        print (sum(float_digits))

        if flag == True:
            break

my_func()
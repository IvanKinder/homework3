def my_func(arg_1, arg_2):
    answer = 1 / arg_1
    if arg_1 > 0 and arg_2 < 0 and type(arg_2) == int:
        for i in range(abs(arg_2) - 1):
            answer *= 1 / (arg_1)
        print (answer)
    else:
        print ("Введите действительное положительное и целое отрицательное!!!!!")


my_func(float(input("Введите действительное полодительное число: ")), int(input("Введите целое отрицательное число: ")))

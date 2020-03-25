def d(arg_1, arg_2):
    if arg_2 != 0:
        print (arg_1 / arg_2)
    else:
        print ("Второе число не должно быть нулём!!!")

d(float(input("Введите первое число: ")), float(input("Введите второе число: ")))
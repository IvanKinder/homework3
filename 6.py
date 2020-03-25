def int_func(a):
    return a.upper()


words = input("Введите слова в любом регистре через пробел: ").split()
for word in words:
    if ord('a') <= ord(word[0]) <= ord('z'):
        print (int_func(word[0]) + word[1:], ' ', end = '')
    elif ord('A') <= ord(word[0]) <= ord('Z'):
        print (int_func(word[0].lower()) + word[1:], ' ', end = '')
    elif word[0].isdigit():
        print (word, ' ', end = '')
    else:
        print ("Сделайте хотябы первую букву латинской в этом слове... ", end = '')

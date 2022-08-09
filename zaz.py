i = True
print('\n---------------Калькулятор Senior Developer---------------')
print('\n1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')
print('5. Округление')
print('6. Квадратный корень')
while i == True:
    x = input("\nВыберите номер операции (Например: 1, 2, 3...): ")
    if x == '1' or x == '2' or x == '3' or x == '4':
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        if x == '1':
            print(a+b)
        elif x== '2':
            print(a-b)
        elif x == '3':
            print (a*b)
        elif x == '4':
            print (a/b)
        else:
            print ('Invald синтакс') 
    elif x == '5' or x == '6':
        c = float(input("Введите число: "))
        if x == '5':
            b = int(input("До сколько цифр после запятой?: "))
            print (float(round(c,b)))
        elif x == '6':
            print(round((c ** 0.5), 4))
        else:
            print ('Вы ввели какую-то хуйню') 
    else:
        print ("Вы ввели какую-то хуйню")
    calc_again = input("Считаем ещё раз? (Впишите 'да/нет'): ")
    if calc_again == "нет":
        i = False
        
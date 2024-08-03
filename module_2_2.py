first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if int(first) == int(second) == int(third) :
    print(3)
elif int(first) == int(second) or int(second) == int(third) or int(first) == int(third):
    print(2)
else: print('0')

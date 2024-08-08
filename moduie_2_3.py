my_list = [42, 69, 322, 13, 0, 99, 5, -9, 8, -7, 6, 5]
n = my_list.__len__()
x = 0
while my_list[x] >= 0:
    valy = my_list[x]
    print(valy)
    x = x + 1
    if x >= n:
        break
print('Конец')



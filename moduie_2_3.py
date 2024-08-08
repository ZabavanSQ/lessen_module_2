my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = my_list.__len__()
x = 0
while my_list[x] >= 0:
    valy = my_list[x]
    if my_list[x] > 0:
        print(valy)
        x = x + 1
    else:
        x = x + 1
        continue        
    if x >= n:
        break
print('Конец')

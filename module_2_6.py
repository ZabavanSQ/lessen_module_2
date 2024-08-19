import random

r = random.randint(3, 20)

print(r)
get = []
get2 = []
getx = list(range(1, r + 1))
for x in getx:
    for y in range(2, r):
        if r % (x + y) == 0 and x != y:
            if y in getx:
                get.append((x))
                get.append((y))
                get2.append((x, y))
                getx.remove(y)
            else:
                continue

print(get2)
print(get)

print(f'Случайное число {r} - ключ {get}')



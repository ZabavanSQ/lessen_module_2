import random

r = random.randint(3, 20)

print(r)
get = []
get1 = []
get2 = []

for x in range(1, r):

    for y in range(2, r):


        if r % (x+y) == 0 and x != y:
            get.append((x))
            get.append((y))
            get2.append((x, y))
for i in range(len(get)):
    if get[i] == get[i+1]:
        get1.append((get[i]))
        break
    get1.append((get[i]))


print(get2)
print(get)
print(get1)
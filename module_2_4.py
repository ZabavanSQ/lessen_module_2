numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    is_primes = True
    for j in range(2 , i) :
        if numbers[i] % j == 0 and numbers[i] == j:
            is_primes = True
            break
        if numbers[i] % j == 0:
                    is_primes = False
        if numbers[i] == 1:
            break
    if numbers[i] == 1:
        continue
    if is_primes == True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print(f'Простые числа = {primes}')
print(f'Не простые числа = {not_primes}')

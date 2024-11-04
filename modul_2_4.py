numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_prime = True
    if i == 1:
        continue
    for j in range(3, i, 2):
        if i % 2 == 0: # проверяем на четность (четные числа не являются простыми, кроме 2)
            is_prime = False
            break
        if i % j == 0: # проверяем остаток от деления только на нечетные числа (для ускорения)
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('Primes:', primes)
print('Not Primes:', not_primes)

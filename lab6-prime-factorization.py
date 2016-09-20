def prime_factorization(n):
    if n == 1:
        return [[1, 1]]
    result = []
    factor = 2
    while factor * factor <= n:
        power = 0
        while (n % factor) == 0:
            power += 1
            n //= factor
        if power > 0:
            result.append([factor, power])
        factor += 1
    if n > 1:
        result.append([n, 1])
    return result


print prime_factorization(1)
print prime_factorization(2)
print prime_factorization(10)
print prime_factorization(11)
print prime_factorization(12)
print prime_factorization(16)
print prime_factorization(1026)

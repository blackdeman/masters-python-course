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

tests = [1, 2, 10, 11, 12, 16, 1026]
for x in tests:
    print "Prime factorization for ", x, " : ", prime_factorization(x)

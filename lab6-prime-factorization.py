def prime_factorization(n):
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

tests = [17, 18]
for x in tests:
    print "Prime factorization for ", x, " : ", prime_factorization(x)

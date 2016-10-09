import itertools


def prime_numbers(n):
    return [x for x in xrange(2, n + 1) if all(x % i for i in xrange(2, x))]

tests = [5, 10, 30, 41]
for test in tests:
    print "Prime numbers for {} : {}".format(test, prime_numbers(test))

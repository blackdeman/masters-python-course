import itertools


def pythagorean_triple(n):
    return [x for x in itertools.permutations(xrange(1, n + 1), 3) if
            (x[0] ** 2 + x[1] ** 2 == x[2] ** 2)]

tests = [5, 10, 30]
for test in tests:
    print "Pythagorean triples for {} : {}".format(test, pythagorean_triple(test))
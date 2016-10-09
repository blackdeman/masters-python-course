import itertools


def pythagorean_triple(n):
    return [x for x in itertools.product(*[range(1, n + 1), range(1, n + 1), range(1, n + 1)]) if
            (x[0] ** 2 + x[1] ** 2 == x[2] ** 2)]
#  and x[0] <= x[1] if triples should be unique

tests = [5, 10, 30]
for n in tests:
    print "Pythagorean triples for {} : {}".format(n, pythagorean_triple(n))

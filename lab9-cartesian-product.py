class CartesianProductElement:
    def __init__(self, X, n):
        self.X = sorted(X)
        self.n = n
        self.value = [self.X[0] for i in xrange(0, n)]
        self.min_value = self.value[:]

    def __incr(self, i):
        if i < 0:
            return
        index = self.X.index(self.value[i]) + 1
        if index == len(self.X):
            self.__incr(i - 1)
            index = 0
        self.value[i] = self.X[index]

    def get_value(self):
        return self.value

    def get_min_value(self):
        return self.min_value

    def next_value(self):
        self.__incr(self.n - 1)


def cartesian_product(X, n):
    el = CartesianProductElement(X, n)
    yield el.get_value()[:]
    el.next_value()
    while el.get_value() != el.get_min_value():
        yield el.value[:]
        el.next_value()

tests = [[['e', 1, 'a'], 2]]
for X in tests:
    print "Input: {}\n Output:\n {}".format(X, list(cartesian_product(X[0], X[1])))

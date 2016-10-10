import numbers


class Vector:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return Vector([sum(x) for x in zip(self.data, other.data)])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Vector([x[0] - x[1] for x in zip(self.data, other.data)])

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum([x[0] * x[1] for x in zip(self.data, other.data)])
        elif isinstance(other, numbers.Real):
            return Vector([x * other for x in self.data])
        else:
            raise Exception("Can't multiply!")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return self.data == other.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __str__(self):
        return "Vector: {}".format(self.data)


v1 = Vector([1.0, 2, 3])
v2 = Vector([-5, 4, 5.0])

scalar = 3.5

print "v1: ", v1
print "v2: ", v2
print "scalar: ", scalar
print "v1 + v2: ", v1 + v2
print "v2 - v1: ", v2 - v1
print "v1 * v2: ", v1 * v2
print "v1 * scalar: ", v1 * 3.5
print "v1 == v1: ", v1 == v1
print "v1 == v2: ", v1 == v2
print "len(v1): ", len(v1)
for i in xrange(0, len(v1)):
    print "v[{}] : {},".format(i, v1[i]),

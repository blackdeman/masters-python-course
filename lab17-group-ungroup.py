from itertools import groupby, tee, izip, repeat


def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return izip(*[iter(iterable)] * n)


def group(data):
    for k, g in groupby(data):
        yield len(list(g))
        yield k


def ungroup(data):
    if len(data) % 2 != 0:
        raise TypeError("List has a odd length!")
    for k, v in grouped(data, 2):
        try:
            for _ in repeat(None, int(k)):
                yield v
        except ValueError:
            raise TypeError("List has an incorrect structure!")


testlist = ["a", "b", "b", "c", "b", "c", "c"]
print testlist
testlistgrpd = list(group(testlist))
print testlistgrpd
print list(ungroup(testlistgrpd))

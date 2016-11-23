# int, float, long, complex
# strings, unicode, tuples
# bytes
# frozen set


def printinfo(x, name):
    print "{0:25} : value = {1:20}, addr = {2:}".format(name, x, hex(id(x)))


def addrcmp(a, b):
    if hex(id(a)) == hex(id(b)):
        print "a and b addresses are equal"
    else:
        print "a and b addresses are not equal"

print "None test"
a = None
b = None
printinfo(a, "a")
printinfo(b, "b")
addrcmp(a, b)
print
print "Int test"
a = int(1)
b = int(2)
printinfo(a, "a")
printinfo(b, "b")
b -= 1
printinfo(b, "b after b-=1")
addrcmp(a, b)
print
print "Long test"
a = long(1)
b = long(2)
printinfo(a, "a")
printinfo(b, "b")
b -= 1
printinfo(b, "b after b-=1")
addrcmp(a, b)
print
print "Float test"
a = float(1)
b = float(2)
printinfo(a, "a")
printinfo(b, "b")
b -= 1
printinfo(b, "b after b-=1")
addrcmp(a, b)
print
print "String test"
a = str("B")
b = str("b")
printinfo(a, "a")
printinfo(b, "b")
b = b.capitalize()
printinfo(b, "b after capitalize")
addrcmp(a, b)
print
print "Tuple test"
a = ('a', 1, 'c', 'd')
b = ('a', 1, 'c')
printinfo(a, "a")
printinfo(b, "b")
b = b + ('d',)
printinfo(b, "b after b = b + ('d',)")
addrcmp(a, b)
print
print "List test"
a = ['a', 1, 'c', 'd']
b = ['a', 1, 'c']
printinfo(a, "a")
printinfo(b, "b")
b.append('d')
printinfo(b, "b after b.append('d')")
addrcmp(a, b)
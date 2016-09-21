def collatz_conjecture(x):
    s = set()
    print x,
    while x != 1 and x not in s:
        s.add(x)
        x = 3 * x + 1 if x % 2 else x / 2
        print " -> ", x,
    print
    return x == 1


x = input("Enter a natural number to test: ")
result = collatz_conjecture(x)
print "Collatz conjecture for ", x, " is ", result

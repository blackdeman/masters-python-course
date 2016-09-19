def collatz_conjecture(x):
    tmp = x
    print x,
    while tmp != 1:
        tmp = 3 * tmp + 1 if tmp % 2 else tmp / 2
        print " -> ", tmp,
        if tmp == x:
            break
    print
    return tmp == 1


x = input("Enter a natural number to test: ")
result = collatz_conjecture(x)
print "Collatz conjecture for ", x, " is ", result

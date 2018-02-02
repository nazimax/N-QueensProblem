n=10

def column(n):
    x = "|"

    i = 0
    while i < n:
        x = x + "\t|"
        i = i + 1
    return x

def line(n):
    y = "_"
    i=0
    while i<n:
        y=y+"____"
        i=i+1
    return y

def buildSquare(n):
    print line(n)
    i=0
    while i<n:
        print column(n)
        print line(n)
        i=i+1
    return 0

buildSquare(10)



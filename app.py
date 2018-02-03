import numpy as np
n=10
#for queens problem to draw column

def column(n,index):
    x = "|"
    i = 0
    if(index==-1):
        while i < n:
            x = x + "\t|"
            i = i + 1
    else:
        while i < n:
            if i!=index:
                x = x + "\t|"
            else:
                x=x+" X |"

            i = i + 1



    return x
# to draw line of chess table
def line(n):
    y = "_"
    i=0
    while i<n:
        y=y+"____"
        i=i+1
    return y

#for queen problem
def indexColumn(line,array):
    for i in array:
        if i[0]==line:
            return i[1]

    return -1

# draw chess table for queen problem n = dimension of table and array contains position of queens
def drawChessTable(n, array):

    print line(n)
    i=0
    while i<n:
        print column(n,indexColumn(i,array))
        print line(n)
        i=i+1
    return ""

def hourseMouve(n,actualPosition):
    allowedMoves=[]
    currentLine=actualPosition[0]
    currentCol=actualPosition[1]


    if currentLine+2<n and currentCol+1<n:
        allowedMoves.append([currentLine+2,currentCol+1])

    if currentLine+1<n and currentCol+2<n:
        allowedMoves.append([currentLine + 1, currentCol + 2])

    if currentLine -2 >=0 and currentCol - 1 >=0:
        allowedMoves.append([currentLine -2, currentCol -1])


    if currentLine -1 >=0 and currentCol -2 >=0:
        allowedMoves.append([currentLine - 1, currentCol - 2])

    if currentLine -2 >=0 and currentCol + 1 < n:
        allowedMoves.append([currentLine -2, currentCol +1])

    if currentLine -1 >=0 and currentCol + 2 < n:
        allowedMoves.append([currentLine - 1, currentCol + 2])

    if currentLine +1 <n and currentCol -2 >=0:
        allowedMoves.append([currentLine + 1, currentCol - 2])

    if currentLine +2 <n and currentCol -1 >=0:
        allowedMoves.append([currentLine + 2, currentCol -1])

    return allowedMoves

# print hourseMouve(5,[0,1])


def existInArray(e,array):

    for i in array:
        if (e == i).all():
            return True
    return False


def diffrenceTwo2DArrays(a,b):
    c=[]
    for i in a:
        if existInArray(i,b)==False:
            c.append(i)
    for i in b:
        if existInArray(i,a)==False:
            c.append(i)

    return c

def filterPositions(n,original):

    impossibl=[]
    possible=hourseMouve(n,original)
    possible=np.asarray(possible)
    for i in possible:
        if (i == original).any():
            impossibl.append(i)

    print impossibl
    print possible
    filtred=diffrenceTwo2DArrays(possible,impossibl)

    return filtred



def findQueenPositions(n):
    prohebitedLines = []
    prohebitedCol = []

    firstQueen=[2,0]
    possilePositions=hourseMouve(n,firstQueen)
    possilePositions.append(firstQueen)
    possilePositions
    drawChessTable(n,possilePositions)


# findQueenPositions(5)

pos=hourseMouve(5,[2,0])

print pos
filterPositions(5,[2,0])
# #drawChessTable(5,pos)
# print "======================================"
#drawChessTable(5,filterPositions(n,[2,0]))

a=np.asarray([[4, 1], [3, 2], [0, 1], [1, 2]])
c=np.asarray([[1,2],[4,1]])


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

positions=[[0,0],[2,3],[4,1]]
# print hourseMouve(6,[4,4])
print drawChessTable(2, positions)

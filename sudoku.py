A=[[[x for x in range(10)]for y in range(9)]for z in range(9)]
P=[[0 for x in range(3)]for y in range(81)]
def prio(x=0,y=0,n=0):
    P[n][0]=0
    if A[x][y][0]== 0:
        for i in range(9):
            if A[x][i][0]!=0 or A[i][y][0]!=0:
                A[x][y][A[x][i][0]]=0
                A[x][y][A[i][y][0]]=0
        for i in range((x//3)*3,((x//3)+1)*3):
            for j in range((y//3)*3,((y//3)+1)*3):
                if A[i][j][0]!=0:
                    A[x][y][A[i][j][0]]=0
        for i in range(1,10):
            if A[x][y][i]==0:
                P[n][0]+=1
    else:
        P[n][0]=0
    P[n][1],P[n][2]=x,y
    y+=1
    if y==9:
        x,y=x+1,0
    if x==9:
        return
    prio(x,y,n+1)
    return
def clear(x,y):
    for i in range(9):
        if A[x][i][0]==0 or A[i][y][0]==0:
            A[x][i][A[x][y][0]]=0
            A[i][y][A[x][y][0]]=0
    for i in range((x//3)*3,((x//3)+1)*3):
        for j in range((y//3)*3,((y//3)+1)*3):
            if A[i][j][0]==0:
                A[i][j][A[x][y][0]]=0
    return
def fill(x,y):
    z,w=0,0
    for i in range(1,10):
        if A[x][y][i]!=0:
            z,w=i,w+1
    if w==1:
        A[x][y][0]=z
        clear(x,y)
    return
def disp():
    c=0
    for x in range (9):
        if x in [0,3,6]:
            print('+ - - - '*3+'+')
        for y in range(9):
            if y in [ 0, 3, 6]:
                print ('| ',end='')
            if A[x][y][0]==0:
                c+=1
                print (' ', end=' ')
            else:
                print(A[x][y][0], end=' ')
        print('|')
    print('+ - - - '*3+'+')
    return c
def Psort():
    for i in range (80):
        m=i
        for j in range(i+1,81):
            if P[j][0]>P[m][0]:
                m=j
        a=P[m]
        P[m]=P[i]
        P[i]=a
    return
def ques():
    s=input('enter the entire sudoku')
    for x in range(9):
        for y in range(9):
                A[x][y][0]=int(s[(x*9)+y])
    return
def box(x=0,y=0):
    for z in range(1,10):
        c=[0 for i in range(3)]
        for i in range(x,x+3):
            for j in range(y,y+3):
                if A[i][j][0]==0 and A[i][j][z]==z:
                    c[0],c[1],c[2]=c[0]+1,i,j
        if c[0]==1:
            A[c[1]][c[2]][0]=z
            clear(c[1],c[2])
    y+=3
    if y==9:
        x,y=x+3,0
    if x==9:
        return
    box(x,y)
    return
def yline(y=0):
    for z in range(1,10):
        c=[0 for i in range(2)]
        for i in range(9):
            if A[i][y][0]==0 and A[i][y][z]==z:
                c[0],c[1]=c[0]+1,i
        if c[0]==1:
            A[c[1]][y][0]=z
            clear(c[1],y)
    if y==8:
        return
    yline(y+1)
    return
def xline(x=0):
    for z in range(1,10):
        c=[0 for i in range(2)]
        for i in range(9):
            if A[x][i][0]==0 and A[x][i][z]==z:
                c[0],c[1]=c[0]+1,i
        if c[0]==1:
            A[x][c[1]][0]=z
            clear(x,c[1])
    if x==8:
        return
    xline(x+1)
    return
def assume():
    for i in range(1,10):
        if A[P[0][1]][P[0][2]][i]!=0:
            A[P[0][1]][P[0][2]][0]=i
            return
ques()
disp()
n,m=[0 for x in range(2)],0
while True:
    prio()
    Psort()
    while P[m][0]>0:
        fill(P[m][1],P[m][2])
        m+=1
    box()
    xline()
    yline()
    n[0]=disp()
    if n[0]==0:
        print('Solved')
        break
    elif n[0]==n[1]:
        assume()
    n[1]=n[0]


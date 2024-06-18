def move(A,C):
    print("%s moves to %s"%(A,C))

def HT(n , A, B, C):
    if n == 1 :
        move(A,C)
    else:
        HT(n-1, A, C, B)
        move(A,C)
        HT(n-1, B, A, C)

HT(3,"A","B","C")
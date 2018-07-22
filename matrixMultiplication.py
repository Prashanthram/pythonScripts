def isMatrix(l):
    n=len(l[0])
    for i in range(1,len(l)):
        if len(l[i])==n:
            continue
        else:
            return False
    return True

def isMul(l1,l2):
    if not isMatrix(l1) and isMatrix(l2):
        print("Not a Matrix")
        return False
    if len(l1)==len(l2[0]):
        return True
    else:
        return False

def matmul(l1,l2):
    if not isMul(l1,l2):
        print("Dimension error")
        return
    lmul=[]
    for i in range(len(l1)):
        lmul.append([0 for i in range(len(l2[0]))])
    for i in range(len(l1)):
        for j in range(len(l2[0])):
            for k in range(len(l2)):
              lmul[i][j] += l1[i][k] * l2[k][j]
    return lmul


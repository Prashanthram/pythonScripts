def mcount(l):
    n = []                  #To store count of each elements
    for x in l:
        count = 0
        for i in range(len(l)):
            if x == l[i]:
                count+=1
        n.append(count)
    a = max(n)              #largest in counts list
    for i in range(len(n)):
        if n[i] == a:
            b = i
            return(l(b),a)  #element,frequency
    return                  #if something goes wrong

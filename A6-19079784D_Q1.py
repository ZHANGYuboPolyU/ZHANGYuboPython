def crypto(m,N,order):
    while len(m)%N!=0:
        m+='z'
    a=input('Please enter your choice (E/D):')
    c=[]
    while a not in ['E','e','D','d']:
        a=input('Invalid choice, please try again:')
    if a in['E','e']:
        b=[]
        for i in range(0,N):
            while i<len(m):
                b.append(m[i])
                i+=N
        for i in order:
            p=(i-1)*(len(m)//N)
            q=i*(len(m)//N)
            for j in b[p:q]:
                c.append(j)       
    #encryption
    else:
        l=len(m)//N
        b=[0]*len(m)
        i=0
        for n in order:
            j=0
            t=i
            for q in m[t:t+l]:
                b[j+(n-1)*l]=q
                i+=1
                j+=1
        for i in range(0,l):
            while i<len(m):
                c.append(b[i])
                i+=l
    #decryption
    return ''.join(c)     
print(crypto("hellohowdoyoudo",3,(1,2,3)))
# user inputs a b e in that order
print(crypto("hellohowdoyoudo",3,(2,3,1)))
# user inputs a b e in that order
print(crypto("eowydlhdoohloou",3,(2,3,1)))
# user inputs b C D in that order
print(crypto("ordpfhntanlntpoeeondtanayteimieaolrbffkz",4,(2,3,1,4)))
# user inputs b D in that order
print(crypto("harrypotterandvoldemort",5,(2,1,4,3,5)))
# user inputs e

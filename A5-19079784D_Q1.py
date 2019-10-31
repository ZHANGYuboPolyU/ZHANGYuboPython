def move(p,q):
    c,g,m,w=p[0],p[1],p[2],p[3]
    C,G,M,W=q[0],q[1],q[2],q[3]
    name=['Cabbage','Goat','Man','Wolf']
    d={'E':'east','W':'west'}
    t=0
    s=0
    if (M!=G and G==(C or W)) or (m!=g and g==(c or w)):
        print(p,q,'Illegal move')
        return
    for i in range(0,4):
        if p[i]!=q[i]:
            t+=1
    if t>2:
        print(p,q,'Illegal move')
        return
    elif t==1:
        for i in range(0,4):
            if p[i]!=q[i]:
                print(p,q,name[i],'moves from',d[p[i]],'to',d[q[i]])
    elif t==2:
        for i in range(0,4):
            if p[i]!=q[i]:
                s+=1
                if s==1:
                    j=str(name[i])
                else:
                    j=j+' '+'and'+' '+str(name[i])
                    break
        print(p,q,j,'move from',d[p[i]],'to',d[q[i]])
sol=("EEEE","EWWE","EWEE","WWWE","WEEE","WEWW","WEEW","WWWW")
for i in range(1,len(sol)):
     move(sol[i-1],sol[i])
sol=("EEEE","EWWE","EWEE","EWWE","EWEE","WWWE","WEEE","WEWW","WEEW","WWWW")
for i in range(1,len(sol)):
     move(sol[i-1],sol[i])
sol=("EEEE","EWWE","EWEE","WWWE","WWEE","WWWE","EWEE","WWWW")
for i in range(1,len(sol)):
     move(sol[i-1],sol[i])














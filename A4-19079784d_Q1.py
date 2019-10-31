def harry(a,b):
    j=97
    m,n=0,0
    r=True
    while j<123:
        for i in a:
            if ord(i)==j:
                m+=1
        for i in b:
            if ord(i)==j:
                n+=1
        if m==n:
            j+=1
            m,n=0,0
        else:
            r,m,n=False,0,0
            break
    print('Checking','"%s"'%a,'with','"%s"'%b,':',r)
    if r==False:
        j=97
        while j<123:
            for i in a:
                if ord(i)==j:
                    m+=1
            for i in b:
                if ord(i)==j:
                    n+=1
            if m<n:
                print('Too few',chr(j))
            elif m>n:
                print('Too many',chr(j))
            m,n=0,0
            j+=1
harry('a computer','our pet mac')
harry("harry potter", "my hero part")
harry("a computer", "our pet mac")

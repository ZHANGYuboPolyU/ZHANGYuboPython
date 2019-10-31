def genLegalStates():
    m,c,g,w=['E','W'],['E','W'],['E','W'],['E','W']
    r=[]
    for h in [0,1]:
        for i in [0,1]:
            for j in [0,1]:
                for k in [0,1]:
                    if (m[h]!=g[j])and(c[i]==g[j] or g[j]==w[k]):
                        continue
                    else:
                        r.append(m[h]+c[i]+g[j]+w[k])
    for i in r:
        if i!='WEEE':
            print(i)
genLegalStates()




def addTable():
    a=[]
    for p in range(0,10):
        b=[]
        for q in range(0,10):
            t=p+q
            if t<10:
                t=str(0)+str(t)
            b.append(str(t)) 
        a.append(b)
    return a
def main():
    table=addTable()
    for item in table:
        print(item)
main()






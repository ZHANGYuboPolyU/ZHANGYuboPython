#function passingAt:
def passingAt(f,t):
    p=pow(f,i-1)*(1-f)
    return p
#passingAt testing:
f,T = 0.1,4
for i in range(1,T+1):
    print('f=',f,'Pr(T=%d)='%i,passingAt(f,i))
f,T = 0.2,5
for i in range(1,T+1):
    print('f=',f,'Pr(T=%d)='%i,passingAt(f,i))
#function passingAt:
def passingBy(f,t):
    p=0
    r=1
    for i in range(1,t):     
        j=r*f+1
        r=j
    return r*(1-f)
#Using Horner's method to reducing numbers of multiplications
#passingAt testing:
print('f=0.1,Pr(T<=4)=',passingBy(0.1,4))
print('f=0.2,Pr(T<=5)=',passingBy(0.2,5))
#to compute Pr(T<=5)function passingAt need 10 multiplications
#to compute Pr(T<=5)function passingBy need 5 multiplications





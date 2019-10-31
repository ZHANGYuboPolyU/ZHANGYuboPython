
import math
def rootTwo(n):
    if n==1:
        return 1
    else:
        r=2
        for i in range(1,n):
            if i==n-1:
                r=1/r+1
            else:
                r=1/r+2
        return r
#rootTwo(n) Testing
print('RootTwo=',math.sqrt(2))
for i in range(1,6):
    print('Value with',i,'terms=',rootTwo(i),'error=',abs(math.sqrt(2)-rootTwo(i)))
#I found this method is similar to Horner's method
#first let r=2,then from innermost layer let r=1/r+2,then go to next layer let r=1/r+2...
#at the outermost layer let r=1/r+1
    

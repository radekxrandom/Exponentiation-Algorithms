def calcExp(a,b):
    if(b==1):
        return a
    if (b==0):
        return 1
    if (b==2):
        return a*a
   
    if (b%2==1):
        return a*calcExp(a,b-1)
    else:
        result = calcExp(a, b/2)
        return result*result
 
print(calcExp(3,3))

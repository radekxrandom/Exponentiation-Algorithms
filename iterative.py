def userInput():
    bo = True;
    while bo:
        a = input("Enter your base: ")
        if a.isdigit():
            bo = False
        else:
            print("This isn't a number, try again.")        
        b = input("Enter your exponent: ")
        if b.isdigit():
            bo = False    
        else:
            print("This isn't a number, try again.")  
    a = int(a)
    b = int(b)
    return calcExp(a,b)
 
 
def calcExp(a,b):
    result = 1
    while(b):
        if(b%2==1):
            result = result*a
            b = b-1
        else:
            b = b/2
            a = a*a
    return result
           
 
print(userInput())

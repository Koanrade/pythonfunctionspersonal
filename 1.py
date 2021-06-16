def main():
    x=int(input("Type in a base\n"))
    y=int(input("Now type in exponent\n"))
    print("\n"+str(x)+" to the power of "+str(y)+" equals " +str(myFunction(x,y)))

def myFunction(x,y):
   a=1
   b=1
   while a<y:
       if a==1:
           b=x
       x=x*b
       a+=1
   return x

main()





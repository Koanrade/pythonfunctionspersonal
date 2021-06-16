from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def powerrr():
    x=int(input("Type in a base\n"))
    y=int(input("Now type in exponent\n"))

    def pow(x,y):
        a=1
        b=1
        while a<y:
            if a==1:
                b=x
                x=x*b
                a+=1
        return x
    print("\n"+str(x)+" to the power of "+str(y)+" equals " +str(pow(x,y)))

def yorn(quest):
    answer = str(input(quest+" (y/n)")).lower().strip()
    if answer[0] == 'y':
        return True
    if answer[0] == "n":
        return False
    else:
        return yorn("Uhhhh... please enter ")

def avge():
    i=int(1)
    summ = int(0)
    numofnum = int(input("Type in number of numbers in your set: "))
    while i<=numofnum:
        provnum = int(input("Type in "+str(i)+" Number: "))
        i+=1
        summ+=provnum
    finalavg = float(summ/numofnum)
    print("The average of numbers in your set equals "+ str(finalavg))





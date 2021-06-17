from os import system, name
import random
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def powerrr():
    def pow(x,y):
        a=1
        b=1
        while a<y:
            if a==1:
                b=x
            x=x*b
            a+=1
        return x
    x=int(input("Type in a base\n"))
    y=int(input("Now type in exponent\n"))
    print(str(x)+" to the power of "+str(y)+" equals " +str(pow(x,y)))




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
def ranndom():
    x=int(input("Type in X\n"))
    y=int(input("Now type Y\n"))
    if x>y:
        rndm=random.randint(y,x)
    else:
        rndm=random.randint(x,y)
    print("Congrats!!! You rolled "+ str(rndm))
def genfib():
    finumprov = int(input("How many fibonnacci numbers you wish to display?"))
    new=finumprov
    if finumprov%2!=0:
        finumprov+=1
    i=0
    a=0
    b=1
    n=1
    cf=0
    fl=[]
    while i<finumprov/2:

        buffa=a #0 0    1 1    2 3    3 8    4 21   5 55
        buffb=b #0 1    1 2    2 5    3 13   4 34   5 89
        cf=a+b # 0 1   1 3
        a=a+b # 0 1   1 3
        b=b+cf # 0 2   1 59
        i+=1
        fl.append(buffa)
        fl.append(buffb)
    j=0
    while j<new:
        print("F_"+str(j)+" == "+str(fl[j]))



        j+=1


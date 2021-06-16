import functionsss
def returnto():
    retquest="Would you like to end?"
    if functionsss.yorn(retquest) == True:
        functionsss.clear()
        exit()
    else:
        functionsss.clear()
        main()
def main():
    functionsss.clear()
    print("1.Power\n2.Count the average\n3.Generate a random number from X to Y")
    pick=int(input("Pick an action:"))
    if pick==1:
        functionsss.clear()
        quest="Are you sure?"
        if functionsss.yorn(quest) == True:
            functionsss.clear()
            functionsss.powerrr()
            returnto()
        else:
            functionsss.clear()
            main()
    if pick==2:
        functionsss.clear()
        quest="Are you sure?"
        if functionsss.yorn(quest) == True:
            functionsss.avge()
            returnto()
        else:
            functionsss.clear()
            main()
    if pick==3:
        functionsss.clear()
        quest="Are you sure?"
        if functionsss.yorn(quest) == True:
            functionsss.powerrr()
            returnto()
        else:
            functionsss.clear()
            main()
    else:
        functionsss.clear()
        print("Wrong action number\n Try again")
        main()
main()

import random
count=0
while(count<=100):
    roll=input("press r to roll a dice")
    if  roll=='r':
        r=random.randint(1,6)
        count=count+r
        print("your random number is",r)
        print("you are in position",count)
        print(r)
        if  count==100:
            print("You win")
        elif count==8:
             count=37
             print ("up you go",count)
             print("Continue playing",count)
        elif count==11:
             count=2
             print ("oops")
        elif count==13:
             count=34
             print("up you go now ur count is",count)
        elif count==25:
             count=4
             print ("oops",count)
        elif count==38:
             count=9
             print ("oops",count)
        elif count==40:
             count=68
             print("up you go",count)
        elif count==52:
             count=81
             print("up you go",count)
        elif count==65:
             count=46
             print ("oops",count)
        elif count==76:
             count=97
             print("up you go",count)
        elif count==89:
             count=70
             print ("oops",count)
        elif count==93:
             count=64
             print ("oops",count)
        elif count==99:
             print ("your almost there",count)
        else:
             print("roll again")


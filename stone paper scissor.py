from random import randint
while(1):
        a = int(input("stone, paper, scissors? (1,2,3): "))-1
        l = ['stone','paper', 'scissors']
        c = randint(0,2) 
        if (a == c):
                result = "Draw"
        elif((a==0 and c==1) or (a==1 and c==2) or (a==2 and c==0)):
                result = "Computer Wins"
        else:
                result=("You Win")
        print("\nYou chose:",l[a], "\t||\tComputer chose:",l[c],"\nResult is: ", result  )
        p=input("\nNext game?(Y/N): ")
        if(p.lower()!="y"):
                break
        print("\n\n")
print("Thank you for playing :)")

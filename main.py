import random

elements = {1:"SNAKE",2:"WATER",3:"GUN"}
score={"WINS":0,"LOSES":0,"DRAWS":0}

def Play(): 
    #'''
    # First an input is taken from user 
    # But if the input is not valid(ValueError or not in [1,2,3]), 
    # then the iteration goes in the  except loop and appropriate message is displayed.
    #'''

    try:
        user = int(input("\nPlease Enter Your Move : "))
        if user not in elements :
            print("❌ Invalid input. Please enter 1, 2, or 3.")
            return Play()
    except ValueError:
        print("❌ Invalid input. Please enter 1, 2, or 3.")
        return Play()
    npc=random.randint(1,3)  
    Game(user,npc)
    
def Choice():
     #If user enters 'y', the Play() executes again 
     #Or else if 'n' is entered by user, the score is displayed and the game ends.
    ch=input("\nDo you wish to play more ?(y/n)").lower()
    if (ch=='y'):
        Play()
    elif ch=='n':
        print("!......Thank you for playing.......!")
        print(f"   ======>YOUR SCORE BOARD<===== \n {score} \n ")
    else:
        print("PLEASE ENTER EITHER 'y' OR 'n' ONLY......")
        return Choice()


def Game(user,npc):
    # conditions for draw match
    if (user==npc): 
        print(f"\n[[ You chose: {elements[user]} ]]")
        print(f"  [[ Computer chose: {elements[npc]} ]]")
        print("    --------> IT WAS A DRAW ! <--------")
        score["DRAWS"]+=1
        Choice()
    # conditions for winning 
    elif (user==1 and npc==2) or (user==3 and npc==1) or (user==2 and npc==3):
        print(f"\n[[ You chose : {elements[user]} ]]")
        print(f"  [[ Computer chose : {elements[npc]} ]]")
        print("     --------> YOU WIN ! <--------")
        score["WINS"]+=1
        Choice()   
    # conditions for losing
    else:
        print(f"\n[[ You chose: {elements[user]} ]]")
        print(f"  [[ Computer chose: {elements[npc]} ]]")
        print("    -------> YOU LOSE ! <--------")
        score["LOSES"]+=1
        Choice()

        
    ## Main game execution starts from here ##
print("\n+--------- WELCOME TO THE SNAKE WATER GUN GAME --------------+\n")
print("  ENTER  (1) FOR SNAKE    (2) FOR WATER     (3) FOR GUN")
Play() # Calling the Play() function

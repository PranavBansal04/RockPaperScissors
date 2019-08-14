import random

#below function takes one argument which is the points required for the user to win
def rock_paper_scissors(p):
    #values will be chosen randomly from this array for computer's moves
    a=['r','p','s']
    #count variable keeps track of number of rounds
    count=1
    user_win=0 #keeps track of no of times user has won
    comp_win=0 #keeps track of no of times computer has won

    #while loop
    while(True):
        #if user has won equal to the required number of times then game will end
        if(user_win==p):
            print("********************GAME OVER******************")
            print("You win!")
            break
        #If user wins are still less than the required count then next round will
        ##take place
        else:
            print("********************ROUND #"+str(count)+"******************")
            #if there is a tie between user choice and computer's choice then
            ##this loop will take input until there is no tie
            while(True):
                print("Pick your throw: [r]ock, [p]aper, or [s]cissors? ")
                t=input()
                comp=a[random.randint(0,2)]
                if(t==comp):
                    print("Tie!")
                    continue
                else:
                    break
            
            #now we have both the inputs and conditions will be check

            ##if user chose 'rock' and computer chose 'paper' then user looses
            if(t=='r' and comp=='p'):
                print("Computer threw paper, you lose!")
                #updating computer win variable as computer wins in this case
                comp_win+=1
                print("Your score: "+str(user_win))
                print("Computer's score: "+str(comp_win))
                count+=1
                continue #to next round

            ##if user chose 'rock' and computer chose 'scissors' then user wins
            if(t=='r' and comp=='s'):
                print("Computer threw scissors, you win!")
                #updating user win variable as user wins in this case
                user_win+=1
                print("Your score: "+str(user_win))
                print("Computer's score: "+str(comp_win))
                count+=1
                continue
            if(t=='p' and comp=='r'):
                print("Computer threw rock, you win!")
                user_win+=1
                print("Your score: "+str(user_win))
                print("Computer's score: "+str(comp_win))
                count+=1
                continue
            
            if(t=='p' and comp=='s'):
                print("Computer threw scissors, you lose!")
                comp_win+=1
                print("Your score: "+str(user_win))
                print("Computer's score: "+str(comp_win))
                count+=1
                continue
            if(t=='s' and comp=='r'):
                print("Computer threw rock, you lose!")
                comp_win+=1
                print("Your score: "+str(user_win))
                print("Computer's score: "+str(comp_win))
                count+=1
                continue
            if(t=='s' and comp=='p'):
                print("Computer threw paper, you win!")
                user_win+=1
                print("Your score: "+str(user_win))
                print("Computer's score: "+str(comp_win))
                count+=1
                continue
        
        



def main():
    print("ROCK PAPER SCISSORS in Python")
    print()
    print('Rules: 1) Rock wins over Scissors.')
    print('       2) Scissors wins over Paper.')
    print('       3) Paper wins over Rock')
    p=int(input("How many points does it take to win? "))
    rock_paper_scissors(p)

main()

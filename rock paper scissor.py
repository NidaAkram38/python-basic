import random
l=["ROCK","PAPPER","SCISSOR"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
                 Game start
                 1:YES
                 2:NO | EXIT
                 '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
                                1:ROCK
                                2:PAPER
                                3:SCISSOR'''))
            if userInput==1:
                uchoice="ROCK"
            elif userInput==2:
                uchoice="SCISSOR"
            elif userInput==3:
                uchoice="PAPPER"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="ROCK" and Cchoice=="SCISSOR") or (uchoice=="PAPPER" and Cchoice=="ROCK") or (uchoice=="SCISSOR" and Cchoice=="PAPPER"):
                print("Computer Value",Cchoice)
                print("User Value",uchoice)    
                print("YOU WIN")
                ucount=ucount+1
                
            else:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)    
                print("COMPUTER WIN")
                ccount=ccount+1
        if ucount==ccount:
            print("FINAL GAME DRAW....")   
            print("USER SCORE:",ucount)
            print("COMPUTER SCORE:",ccount)
        elif ucount>ccount:
            print("FINAL YOU WIN THE GAME....")   
            print("USER SCORE:",ucount)
            print("COMPUTER SCORE:",ccount)
        else:
            print("FINAL COMPUTER WIN THE GAME....")   
            print("USER SCORE:",ucount)
            print("COMPUTER SCORE:",ccount)
            
    else:
        break
# The game() function in a program lets a user play a 
# game and returns the score as an integer. You need to read
# a file hiscore.txt which is either blank or contains the previous 
# hi-score. You need to write a program to update the hi-score
# whenever game() breaks the hi-score. 

import random   # so that computer will choose any number
                # at random

def game(): # func definition 

    print("You're playing a game.....")
    # guessing starts
    score = random.randint(1,33)


# fetch the hiscore from the file, hiscore_game
    with open("hiscore_game.txt","r") as f:
        hiscore = f.read()

# storing the hiscore in the file if the file is not empty    
        if(hiscore != ""):
            hiscore = int(hiscore)

# if the file is empty, then storing 0 in it            
        else:
            hiscore = 0

    print(f"Your score is {score}")

# the hiscore in the file will be updated to score if 
# the condition is true     
    if(hiscore<score):
        with open("hiscore_game.txt","w") as f:
            f.write(str(score))
    # print(type(score),type(hiscore))        
    return score        

game() # func calling
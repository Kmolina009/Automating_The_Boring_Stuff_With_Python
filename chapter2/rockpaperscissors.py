import random

#From Chapter 2's Automating the Boring Stuff with Python.

#Welcome Message and instructions
print("Welcom to Rock, Paper, Scissors")
print('''When making your selection, input as follows
      Rock or R, Scissors or S, and Paper or R
      To display score, enter score
      To exit the game enter quit or q
       ''')

#Game variables
playerChoice = "This value will be reassigned with player input"
playerWins = 0
playerLosses = 0
cpuWins=0
cpuLosses = 0
draw = 0

#Player Selection and assignment
while (playerChoice != "q" or "quit"):
    playerInput = input('Make your selection!!!')
    if playerInput =='Rock' or 'R':
        playerChoice ="Rock"
        print("You have selected Rock") 
    elif playerInput =='Scissors' or 'S':
        playerChoice ="Scissors"
        print("You have selected Scissors") 
    elif playerInput =='Paper' or 'P':
        playerChoice ="Paper"
        print("You have selected Paper")
    elif playerInput =="score":
        print("""
              Current Score
            =======================
            |Score |Player |CPU   |
            =======================
            | Wins     %s  |  %s  |  
            | Losses   %s  |  %s  | 
            | Draw        %s      |
            =======================
               """ %(playerWins, cpuWins, playerLosses, cpuLosses,draw)
        )        
    elif playerInput =="quit" or playerInput =="q":
        print("""
                  Game Over
                 Final Scores
            =======================
            |Score |Player |CPU   |
            =======================
            | Wins     %s  |  %s  |  
            | Losses   %s  |  %s  | 
            | Draw        %s      |
            =======================
               """ %(playerWins, cpuWins, playerLosses, cpuLosses,draw)
        )
        break
    else:
        print("Invalid input.") 
        
    #CPU Selection and assignment
    cpuChoice = random.randint(1,3)
    if cpuChoice == 1:
        cpuChoice ="Rock"
        print("CPU has selected Rock") 
    elif cpuChoice == 2:
        cpuChoice ="Scissors"
        print("CPU has selected Scissors") 
    elif cpuChoice == 3:
        cpuChoice ="Paper" 
        print("CPU has selected Paper")
        
    # Interactions between R,P,S
    if(playerChoice == cpuChoice):
        print("Player has chosen %s while CPU has chosen %s It's a draw" % (playerChoice, cpuChoice))
        draw += 1
        # Rock interaction
    elif(playerChoice == "Rock " and  cpuChoice == "Paper"):
        cpuWins += 1
        playerLosses += 1
        print("Paper Beats Rock!\n Cpu Scores")
    elif(playerChoice == "Rock " and  cpuChoice == "Scissor"):
        playerWins += 1
        cpuLosses += 1
        print("Rock Beats Scissor!\n Player Scores")
        # Paper interaction
    elif(playerChoice == "Paper" and  cpuChoice == "Scissors"):
        cpuWins += 1
        playerLosses += 1
        print("Scissors Beats Paper!\n Cpu Scores")
    elif(playerChoice == "Paper" and  cpuChoice == "Rock"):
        playerWins += 1
        cpuLosses += 1
        print("Paper Beats Rock!\n Player Scores")
        # Scissor interaction
    elif(playerChoice == "Scissor" and  cpuChoice == "Rock"):
        cpuWins += 1
        playerLosses += 1
        print("Rock Beats Scissors!\n Cpu Scores")
    elif(playerChoice == "Scissor" and  cpuChoice == "Paper"):
        playerWins += 1
        cpuLosses += 1
        print("Scissors Beats Paper! \n Player Scores")
    else:
        pass

# ICE BOX -> Creating a Best Two out of Three scenario, or  
# giving the player the option at the start and after a round
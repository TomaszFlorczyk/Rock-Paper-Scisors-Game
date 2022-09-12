
import random, os

playerScore = 0
computerScore = 0
x = True
roundCounter = 0
figures = ["Rock", "Paper", "Scisors"]

while x == True:
    while (playerScore < 3 and computerScore < 3):
        playerFigure = str(input("Choose your figure from" + str(figures) + "\n"))

        while playerFigure not in figures:
                playerFigure = str(input("Wrong figure, choose figure from list" + str(figures) + "\n"))
        while playerFigure in figures:
                os.system('cls')
                print("You choosen: " + playerFigure)
                computerFigure = random.choice(figures)
                print("Computer choosen: " + computerFigure)

                if playerFigure == "Rock" and computerFigure == "Scisors":
                    playerScore += 1
                    print("Player score: ", playerScore)
                elif playerFigure == "Paper" and computerFigure == "Rock":
                    playerScore += 1
                    print("Player score: ", playerScore)
                elif playerFigure == "Scisors" and computerFigure == "Paper":
                    playerScore += 1
                    print("Player score: ", playerScore)
                elif playerFigure == computerFigure:
                    print("Tie! Keep going!")
                else:
                    computerScore += 1
                    print("Computer score: ", computerScore)
                if playerScore == 3 or computerScore == 3:
                    
                    if playerScore == 3:
                        print("Congrats you won!\n Do you wanna play again?\n")
                    else:
                        print("Computer won!\n Do you wanna play again?\n")
                        
                break
    reset = input("Y / N : ")
    if reset == "Y":
        playerScore = 0
        computerScore = 0
        os.system('cls')
        roundCounter += 1
        print("Round " + str(roundCounter) + " ended")
        print("Round " + str(roundCounter + 1) + " starting now!")
    else:
        break

    

















"""while playerScore or computerScore != 3:

    while playerFigure not in figures:
            playerFigure = str(input("Wrong figure, choose figure from list" + str(figures) + "\n"))
            break
    while playerFigure in figures:
            print("You choosen: " + playerFigure)
            print("Computer choosen: " + computerFigure)
            break """   




    



import random, time

fruits = ["pear", "apple","banana", "apricot", "pineapple","cantaloupe", "grapefruit","jackfruit","papaya" ]
dc  = ["batman","superman","flash","aquaman","darkseid","harley", "swamp thing", "green lantern", "wonder woman"]
#game variables to store the game statistics (in the background)
userGuesslist = []
usesrGuesses = []
playGame = True
category = ""
continueGame = "y"

#defining the user input(their name). Then saying the rules of the game and how long they can go for
name = input("What is your name bruh? ")
print("Hello", name.capitalize(),"Let's start playing this game hime!")
time.sleep(1)
print("Try and guess the word the computer picked. (like normal hangman)")
time.sleep(1)
print("You can only guess one letter at a time. Press enter key when chosen letter.")
time.sleep(2)
print("let us get started my guy!")
time.sleep(1)

while True:

     #Logic for allowing the computer to pick a word from any of the categories.
    while True:
        if category.lower() == "f":
            secretWord = random.choice(fruits)
            break
        elif category.lower() == "d":
            secretWord = random.choice(dc)
            break 
        else:
            category = input("Yo, select a valid category: f/F for fruits or D/d for DC; X to exit")

        if category.lower() == "x":
            print("TTYL gossip girl,XOXO")
            playGame = False
            break


    #adding blank spaces of the word that they must guess
    if playGame:
        secretWordList = list(secretWord)
        attempts = (len(secretWord) + 6)


        #Function for printing the UserGuesList
        def printGuessedLetter():
            print("The secret word is: "+"".join(userGuesslist))
            

        for n in secretWordList:
            userGuesslist.append("_")
        printGuessedLetter()
        print("The amount of allowed guesses for the word are: ", attempts)

        #Starting the game, literally enables you to start the game
        while True:
            print("Guess a letter:")
            letter = input()

            if letter in usesrGuesses: #is basically saying letter will be in userGuesses
                 print("You already guessed the letter, try something else.")

            else:
                attempts -= 1
                usesrGuesses.append(letter)
                if letter in secretWordList:
                    print("nice bruh")
                    if attempts > 0:
                        print("You have ", attempts, "guess left!")
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            letterIndex = i
                            userGuesslist[letterIndex] = letter.lower()
                    printGuessedLetter()
                else:
                    print("ahhh bruuuhh! try again.")
                    if attempts > 0:
                        print("You have ", attempts, "Guesses left!")
                    printGuessedLetter()

            #WIN/LOSE logic
            joinedList = "".join(userGuesslist)
            if joinedList.lower() == secretWord.lower():
                print("YOU WON BRUHHHH.")
                break
            elif attempts == 0:
                print("Unfortunately one too many guesses! sorry. (try again though).")
                print("The word was " + secretWord.lower())
                break

        # The Play again logic for the game
        continueGame = input("Do you want to play again? Y/y to continue, any other key to quit though")
        if continueGame.lower() == "y":
            category = input("Select a valid category: f/F for fruits or d/D for DC")
            userGuesslist = []
            usesrGuesses = []
            playGame = True
        else:
            print("Thanks for playing my guy bruh!. Catch you on the flip!")
            break
    else:
        break        
    
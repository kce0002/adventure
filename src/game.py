# Kyle Ehlers
# 7/26/19
# This script controls the gameflow

import Character

def welcome(needWelcome):
    # Define strings for the user-interface
    welcomeString = '\nWelcome to the adventure game! The object of the game is simple, ' \
        + 'using your chosen character\nalong with your randomly chosen team, you must ' \
        + 'attempt to pass all the challenges and\nobstacles preventing you from reaching ' \
        + 'the treasure at the end. Your team will consist of 3\nmembers, including yourself ' \
        + 'and if your character runs out of hitpoints, it is game over.\n'
    menuString = 'Choose an option:\n1 - View rules\n2 - Start game\n3 - Exit'

    # Print the strings and present the options
    if needWelcome:
        print(welcomeString)

    print(menuString)

    # Get the user's choice
    menuChoice = input('> ')

    # Validate the user's choice
    if menuChoice not in ['1', '2', '3']:
        while menuChoice not in ['1', '2', '3']:
            menuChoice = input('Error: invalid choice. Please try again.\n> ')
    
    # Choose next function based on the user's choice
    if menuChoice == '1':
        viewRules()
    elif menuChoice == '2':
        startGame()
    else:
        exit()

def viewRules():
    rulesString = ''
    print(rulesString)
    welcome(False)

def startGame():
    pass

welcome(True)

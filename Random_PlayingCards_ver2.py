#1-13 clubs 
#14-26 heatts
#27-39 spades
#40-52 Diamonds
# A,2,3,4,5,6,7,8,9,10,J,Q,K
import random


suits = ["Spades","Hearts","Diamond","Clubs"]
ranks = ["Ace","King","Queen","Jack",2,3,4,5,6,7,8,9,10]
indexOfCards = list(range(0,52))


def settingCardDeck():
    cardDeck = []
    for suit in suits:
        for rank in ranks:
            cardUnit = f"{rank} of {suit}"
            cardDeck.append(cardUnit)
    return cardDeck


def pickingCardIndex():
    listOfIndexOfCards = []
    while len(listOfIndexOfCards) != 5:
        pickCard = random.randint(0, 51)
        if pickCard in indexOfCards:
            listOfIndexOfCards.append(pickCard)
            indexOfCards.remove(pickCard)
        else:
            pickCard = random.randint(0,51)
    listOfIndexOfCards.sort()
    return listOfIndexOfCards
    

def settingCard():
    deck = settingCardDeck()
    indexList = pickingCardIndex()
    listOfCards = []
    for i in indexList:
        titleOfCard = deck[i]
        listOfCards.append(titleOfCard)
    return listOfCards    

def settingNameOfPlayer(answer, n):
    dataTypeChecker = False
    while dataTypeChecker == False:
        answer = answer.lower()
        if answer == "yes":
            name = []
            for i in range(n):
                nameOfPlayer = input(f"\nEnter a name for the player {i+1}: ")
                name.append(nameOfPlayer)
            dataTypeChecker = True
            return name
            
        elif answer == "no":
            name = []
            for j in range(n):
                nameOfPlayer = f"Player{j+1}"
                name.append(nameOfPlayer)
            dataTypeChecker = True
            return name
        else:
            answer = input(f"\nWrong word typed(\"{answer}\").\nPlease enter \"Yes\" or \"No\" to choose to set the name of players: ")
            
    

def settingNumberOfPlayer(): 
    dataTypeChecker = False
    nameOfPlayer = input("\nEnter a number between 1 to 5 to select the number of players: ")
    while dataTypeChecker == False:      
        try:
            nameOfPlayer = int(nameOfPlayer)
            if 1 <= nameOfPlayer <= 5:
                dataTypeChecker = True
                print(f"Player selected by user is {nameOfPlayer}")
            else: 
                nameOfPlayer = input(f"\nNumber({nameOfPlayer}) out of range selected.\nPlease enter a number between 1 to 5 to selct the number of players:")
        except ValueError:
            nameOfPlayer = input(f"\nThe user did not entered a number({nameOfPlayer})\nPlease enter a number between 1 to 5 to select the number of players:")
    return nameOfPlayer

def main():
    print("Welcom to the card game!")
    playerNumber = settingNumberOfPlayer()
    ask = input("\nDo you want to name the players?\nEnter \"Yes\" or \"No\" to proceed:")
    player = settingNameOfPlayer(ask,playerNumber)
    for i in range(playerNumber):
       cards = settingCard()
       displayingcard = "    ".join(cards)
       print(f"\n{player[i]}'s cards:\n\n{displayingcard}")



main()
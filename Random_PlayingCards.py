#1-13 clubs 
#14-26 Hearts
#27-39 Spades
#40-52 Diamonds
# A,2,3,4,5,6,7,8,9,10,J,Q,K
import random

card_deck = list(range(1,53))
Clubs = list(range(1,14))
Hearts = list(range(14,27))
Spades = list(range(27,40))
Diamonds = list(range(40,53))
unit_of_card = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]


def card_recognizer(number):
    if (number in Clubs):
        name_of_card = unit_of_card[number-1]
        card = (f"{name_of_card} of Clubs")
        return card
    
    if number in Hearts:
        number = number%13
        name_of_card = unit_of_card[number-1]
        card = (f"{name_of_card} of Hearts")
        return card
    
    if number in Spades:
        number = number%13
        name_of_card = unit_of_card[number-1]
        card = (f"{name_of_card} of Spades")
        return card

    if number in Diamonds:
        number = number%13
        name_of_card = unit_of_card[number-1]
        card = (f"{name_of_card} of Diamonds")
        return card

"""
def picking_card(number_of_player):
    for i in range(number_of_player):
        card_for_player = []
        while len(card_for_player) != 5:
            pick_card = random.randint(1, 52)
            if pick_card in card_deck:
                picked_up_card = card_recognizer(pick_card)
                card_for_player.append(picked_up_card)
                card_deck.remove(pick_card)
            else:
                pick_card = random.randint(1,52)
        cards_of_player1 = card_for_player[:]
"""
def picking_card(n):
    name = []
    for i in range(n):
      name_of_player = input(f"\nEenter a name for the player {i+1}: ")
      name.append(name_of_player)
    for j in range(n):      
        card_for_player = []
        while len(card_for_player) != 5:
            pick_card = random.randint(1, 52)
            if pick_card in card_deck:
                picked_up_card = card_recognizer(pick_card)
                card_for_player.append(picked_up_card)
                displaying_card = "\n".join(card_for_player)
                card_deck.remove(pick_card)
            else:
                pick_card = random.randint(1,52)
        print(f"\nCard for player {name[j]}:\n\n{displaying_card}")
    #return displaying_card

"""
def picking_card(n):
    name = ["Player1", "Player2", "Player3", "Player4", "Player5"]
    wants_name = input("Do you want to enter a name for the players? : ")
    if wants_name == "yes":
    for i in range(n):
      name_of_player = input(f"\nEenter a name for the player {i+1}: ")
      name.append(name_of_player)
    for j in range(n):      
        card_for_player = []
        while len(card_for_player) != 5:
            pick_card = random.randint(1, 52)
            if pick_card in card_deck:
                picked_up_card = card_recognizer(pick_card)
                card_for_player.append(picked_up_card)
                displaying_card = "\n".join(card_for_player)
                card_deck.remove(pick_card)
            else:
                pick_card = random.randint(1,52)
        print(f"\nCard for player {name[j]}:\n\n{displaying_card}")
    #return displaying_card
"""

def number_of_player(): 
    data_type_checker = False
    player = input("\nEnter a number between 1 to 5 to select the number of players: ")
    while data_type_checker == False:      
        try:
            player = int(player)
            if 1 <= player <= 5:
                data_type_checker = True
                print(f"Player selected by user is {player}")
            else: 
                player = input(f"Number({player}) out of range selected.\nPlease enter a number between 1 to 5 to selct the number of players:")
        except ValueError:
            player = input(f"The user did not entered a number({player})\nPlease enter a number between 1 to 5 to select the number of players:")
    return player

def main():
    print("Welcom to the card game!")
    player_number = number_of_player()
    picking_card(player_number)
main()

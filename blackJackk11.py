import random
import os
from art import logo
def deal_card():
    """ returns the random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    ''' take a list of cards and return the score calculated from the cards'''
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards  and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

def compare(userscore, computerscore):
    if userscore==computerscore:
        return " its a draw"
    elif computerscore==0:
        print("computer win")
    elif userscore==0:
        print("user win")
    elif userscore>21:
        print("you went over !!! user looses")
    elif computerscore>21:
        print("computer went over !!!!!!computer looses")
    elif userscore>computerscore:
        print("user win")
    else:
        print("computer wuin")


def play_game():
    print(logo)
    user_cards = []
    computer_cards=[]
    is_game_ovewr = False

    for  _ in range(2):
        print(user_cards.append(deal_card()))
        computer_cards.append(deal_card())
    while not is_game_ovewr:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)
        print(f"your cards {user_cards}, current scores : {user_score}")
        print(f"computer  cards {computer_cards[0]}")
        if user_score==0 or calculate_score==0 or user_score>21:
            is_game_ovewr=True

        else:
            ask_user = input("draw another card: \n")
            if ask_user=='y':
                user_cards.append(deal_card())
            else:
                is_game_ovewr=True
    while comp_score!=0 and comp_score<17:
        computer_cards.append(deal_card())
        comp_score=calculate_score(computer_cards )

    print(f" your final hand: {user_cards} , final score: {user_score}")
    print(f" computer final hand: {computer_cards} , computer final score: {comp_score}")
    compare(user_score,comp_score)

while input("do u wanna play a gameof Blackjack? 'y' or 'n' : \n")=='y':
    os.system('cls')
    play_game()


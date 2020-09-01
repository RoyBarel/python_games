import random

CARDS=['2','3','4','5','6','7','8','9',"J","Q","K","A"]
Dealer_cards= []
Dealer_value_cards=[]
Player_cards=[]
Player_value_cards=[]


def user_chice():
    choice = ""
    # validetion
    while True:
        choice = input("Choose Hit or Stand \n"
                       "h --> Hit\n"
                       "s --> Stand\n")
        if choice.lower() in ["s", "h"]:
            return choice.lower()
        else:
            print("you need to pick a choice from the options")

def print_cards(card_list,player):
    print("Here is {} card:".format(player))
    if player=="Dealer":
        print(card_list[1:])
    else:
        print(card_list)

def random_num():
    return random.randint(0, 11)

def card_type(random_index):
    card = CARDS[random_index]
    return card

def value_of_card(card):
    if card in ["j","Q","K"]:
        return 10
    if card == "A":
        return 11
    return int(card)

def get_card():
    return(card_type(random_num()))

def total_cards_value(list_cards):
    value =sum(list_cards)
    if value >21:
        if 11 in list_cards:
            list_cards[list_cards.index(11)]=1
            value =value -10

    return value,list_cards


"""
def dealer_gets_cards():
    card = card_type(random_num())
    value = value_of_card(card)
    Dealer_cards.append(card)
    Dealer_value_cards.append(value)
    if sum(Dealer_value_cards)>21 and :


"""
###player cards
for i in range(2):
    card=get_card()
    Player_cards.append(card)
    Player_value_cards.append(value_of_card(card))

###Dealer cards
for i in range(2):
    card = get_card()
    Dealer_cards.append(card)
    Dealer_value_cards.append(value_of_card(card))

print_cards(Player_cards,"Player")
total, Player_value_cards = total_cards_value(Player_value_cards)
print(total,Player_value_cards)
print_cards(Dealer_cards,"Dealer")
total,Dealer_value_cards=total_cards_value(Dealer_value_cards)
print(total,Dealer_value_cards)





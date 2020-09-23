import random


values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

playing = True


class Card:
    def __init__(self,suit,rank):

        self.suit=suit
        self.rank=rank
        #self.value = values[rank]
    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck=[]

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        card = self.deck.pop()
        return card


class Hand:
    def __init__(self):
        self.cards=[]
        self.value = 0
        self.aces = 0    # add an attribute to keep track of aces


    def __str__(self):
        hand =''
        for card in self.cards:
            hand += "\n"+ card.__str__()
        return "Hand cards has: "+hand

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank =="Ace":
            self.aces += 1


    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.aces -= 1
            self.value -= 10


class Chips:
    def __init__(self,total=100):
        self.total=total# This can be set to a default value or supplied by a user input
        self.bet =0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print("Please chose number")

        else:
            if chips.bet > self.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    pass


test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
print(test_player)
print(test_player.value)
take_bet()

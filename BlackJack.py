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
        self.value = values[rank]
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
            if chips.bet > chips.total:
                print(f"Sorry, your bet can't exceed, you have: {chips.total}")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        player_input=input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if player_input[0].lower() == "h":
            hit(deck,hand)
        elif player_input[0].lower() == "s":
            print("Player Stands Dealer's Turn")
            playing =False
        else:
            print("Enter correct input, Enter 'h' or 's' ")
            continue
        break


def show_some(player, dealer):

    print("\nDealer's Hand: \n <card hidden>", *dealer.cards[1:], sep='\n ')
    print("Dealer's Hand =", dealer.value - dealer.cards[0].value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def show_all(player, dealer):

    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and Player tie! It's a push.")



while True:
    # Print an opening statement
    print("welcome to BlackJack Game!")
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    dealer = Hand()
    player = Hand()

    for i in range(2):
        dealer.add_card(deck.deal())
        player.add_card(deck.deal())

    # Set up the Player's chips

    player_chips = Chips(500)
    # Prompt the Player for their bet

    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)


    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value >21:
            player_busts(player,dealer,player_chips)
            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <=21:

        while dealer.value< 17:
            hit(deck,dealer)

        # Show all cards
        show_all(player,dealer)

        # Run different winning scenarios
        if dealer.value >21:
            dealer_busts(player,dealer,player_chips)

        elif dealer.value > player.value:
            dealer_wins(player,dealer,player_chips)

        elif dealer.value <player.value:
            player_wins(player,dealer,player_chips)

        elif dealer.value == player.value:
            push(player,dealer)
        # Inform Player of their chips total

    print(f"Player you have {player_chips.total} Chips left.")
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")


    break

import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card():

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():


    def __init__(self):
        self.all_cards=[]

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)


    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()




class Player():

        def __init__(self,name):

            self.name = name
            self.all_cards = []

        def remove_one(self):
            return self.all_cards.pop(0)

        def add_cards(self,new_cards):
            if type(new_cards) == type([]):
                self.all_cards.extend(new_cards)
            else:
                self.all_cards.append(new_cards)

        def __str__(self):

            return f"Player {self.name} Have: {len(self.all_cards)} cards."




if __name__ == '__main__':

    p1 =Player("Player 1")
    p2 =Player("Player 2")

    deck =Deck()
    deck.shuffle()

    for c in range(26):
        p1.add_cards(deck.deal_one())
        p2.add_cards(deck.deal_one())

    game_on = True
    round_num =0

    while game_on:

        round_num +=1
        print(f"Round {round_num}")

        # Check to see if a player is out of cards:

        if len(p1.all_cards)==0:
            print("Player1 out fo cards!, \nPlayer 2 win!!!")
            game_on=False
            break
        if len(p2.all_cards) ==0:
            print("Player2 out fo cards!, \nPlayer 1 win!!!")
            game_on = False
            break

        # Otherwise, the game is still on!
        # Start a new round and reset current cards "on the table"

        player1_cards =[]
        player2_cards = []

        player1_cards.append(p1.remove_one())
        player2_cards.append(p2.remove_one())

        at_war = True

        while at_war:

            if player1_cards[-1].value < player2_cards[-1].value:
                # Player Two gets the cards
                p2.add_cards(player1_cards)
                p2.add_cards(player2_cards)
                at_war =False
                break

            elif player1_cards[-1].value > player2_cards[-1].value:
                # Player One gets the cards
                p1.add_cards(player1_cards)
                p1.add_cards(player2_cards)
                at_war = False
                break

            else:
                print("WAR!")
                # This occurs when the cards are equal.
                # We'll grab another card each and continue the current war.

                # First check to see if player has enough cards

                # Check to see if a player is out of cards:

                if len(p1.all_cards)<5:
                    print("Player 1 unable to declare war")
                    print("Player 2 win")
                    game_on = False
                    break
                elif len(p2.all_cards) < 5:
                    print("Player 2 unable to declare war")
                    print("Player 1 win")
                    game_on = False
                    break
                # Otherwise, we're still at war, so we'll add the next cards

                else:
                    for i in range(5):
                        player1_cards.append(p1.remove_one())
                        player2_cards.append(p2.remove_one())















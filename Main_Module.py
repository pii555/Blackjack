import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
faces = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
gamestatus = True

class Card:
#Assigns the suit/face to objects of card class
    def __init__(self,suit,face):
        self.suit = suit
        self.face = face

    #Prints out the card
    def __str__(self):
        return self.face + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for face in faces:
                self.deck.append(Card(suit,face))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += "\n " + card.__str__()
        return 'The deck has: ' + deck_comp

                    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def addcard(self,card):
        self.cards.append(card)
        self.value += values[card.face]
        if card.face == 'Ace':
            self.aces += 1

    def adjust_ace(self):
        if self.value > 21 and self.aces >= 1:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self,total):
        self.total = total
        self.bet = 0

    def winbet(self):
        self.total += self.bet

    def losebet(self):
        self.total -= self.bet

    def blackjackwin(self):
        self.total += (self.bet / 2)


def takebet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, print an integer ')
        else:
            if chips.bet > chips.total:
                print('Your bet can not exceed',chips.total)
            elif chips.bet <= 0:
                print('You must give a bet greater than 0')
            else:
                break


def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(deck.deal())
    hand.adjust_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:

        choice = input('Would you like to hit or stand? Enter hit or stand ')

        if choice.lower() == 'hit':
            hit(deck,hand)

        elif choice.lower() == 'stand':
            print ('Player stands. Dealers turn')

        else:
            print('Please enter a valid input')
            continue

        break

def hidden_card(player,dealer):
    print("\nDealer's Hand:")
    print('<Hidden Card>')
    print(dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print(player_hand.value)


def show_cards(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n')
    print(dealer_hand.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print(player_hand.value)


def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_blackjack_wins(player,dealer,chips):
    print("Player got blackjack! Player wins")
    chips.blackjackwin()
    

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
        
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")    


print("Welcome to Blackjack!")
starting_amount = int(input("How much would you like to start the game with "))

player_chips = Chips(starting_amount)

print("Lets play!")

while True:
    print("Betting time!")
    takebet(player_chips)

    deck = Deck()
    deck.shuffle()
        
    player_hand = Hand()
    player_hand.addcard(deck.deal())
    player_hand.addcard(deck.deal())

    dealer_hand = Hand()
    dealer_hand.addcard(deck.deal())
    dealer_hand.addcard(deck.deal())


    hidden_card(player_hand, dealer_hand)

    if player_hand.value == 21:
        player_blackjack_wins(player_hand,dealer_hand,player_chips)
        


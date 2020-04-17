#################### text base version of Stupid ####################

#import collections 
# =============================================================================
import random

# =============================================================================

# =============================================================================
# =============================================================================
# global num_players
# global D_pile
# global num_of_decks
# global players
# 
# 
# =============================================================================

class Player:
    def __init__(self,name, hand, ups, downs):
        self.name = name
        self.hand = hand
        self.ups = ups
        self.downs = downs
class Card:
    def __init__(self,suit,card_val,value):
        self.suit = suit
        self.card_val = card_val
        self.value= value
        self.name =  card_val+ ' of ' + suit

def Show_hand(full_deck):
    for x in full_deck:
        print x.name

def Deck():
    suits = ["Clubs","Diamonds","Spades","Hearts"]
    values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    full_deck = []
    for x in suits:
        for y in values:
           
            if y == 11:
                card_vals = 'J'
            elif y == 12:
                card_vals = 'Q'
            elif y == 13:
                card_vals = 'K'
            elif y == 14:
                card_vals = 'A'
            else:
                card_vals = str(y)
            if card_vals == '10':
                y = 1
                
            full_deck.append(Card(suit=x, card_val=card_vals, value = y))

    return full_deck



def Shuffle(deck):
    deck = random.shuffle(deck)
    return deck

def Order(hand):
    def get_card_val(card):
        return card.value
    hand.sort(key = get_card_val)
    return hand

        
def Deal(num_players, players, deck):
    for x in range(5):
        for y in range(num_players):
            players[y].downs.append(deck[-1])
            deck.pop()
            
        for y in range(num_players):
            players[y].ups.append(deck[-1])
            deck.pop()
            
        for y in range(num_players):
            players[y].hand.append(deck[-1])
            deck.pop()
        
def Set_up():

    players=[]

    num_players = 2 # The number of players. Default is 2.
    num_of_decks= 1 # The number of decks. Default is 1
    num_players = raw_input("enter the number of players(2-9): ") 
    num_players = int(num_players) 
    
    D_pile= (num_of_decks*52)-(15*num_players) 
    my_deck =[]
    
    
    while  D_pile <= 3*num_players:
         num_of_decks = num_of_decks + 1
         D_pile= (num_of_decks*52)-(15*num_players) 
    for x in range(num_players) :
        new_player =  Player(name = "Player "+ str(x+1),hand=[], ups=[], downs=[])
        players.append(new_player)
        print players[x].name

         
    
    for x in range(num_of_decks):
        new_deck = Deck()
        for y in new_deck:
            my_deck.append(y)
        
    Shuffle(my_deck)

        
#    print "Number of players: ", num_players 
#    print "Number of decks: ", num_of_decks 
#    print "Draw pile cards: ", D_pile
    return num_players, players, my_deck

def Draw(active_player, Deck):
    if Deck != []:
        active_player.hand.append(Deck[-1])
        Deck.pop()
        Order(active_player.hand)
        print active_player.name + "'s hand is:"
        for x in active_player.hand:
            print x.name
        
    else:
        pass
    
    
def Play_Hand(active_player, Discard):
    multi=0
    square=0
    multiple_list =[]
    new_hand = []
    while multi == 0:
        play_card = raw_input("What card value would you like to play? (2-A): ")
        
# =============================================================================
#         if play_card > Discard[-1].value:
# =============================================================================
            
        for x in active_player.hand:
            #print x.card_val
            if x.card_val == play_card:
                multi = multi + 1
                multiple_list.append(x)
                #active_player.hand.remove(x)
            #Show_hand(active_player.hand)
        
    if multi > 1:
       play_multi = raw_input("Do you want to play more than one card? (y or n): ") 
       if play_multi == 'y':
           how_manyS= raw_input("How many would you like to play? : ")
           how_many = int(how_manyS)
           if how_many > multi:
               while how_many > multi:
                   how_manyS= raw_input("Error: Number requested exceeds number in hand. How many would you like to play? : ")
                   how_many = int(how_manyS)
           if how_many < 0:
               while how_many < 0:
                   how_manyS= raw_input("Error: Number requested less than 0. How many would you like to play? : ")
                   how_many = int(how_manyS)
           for z in range(how_many):
               Discard.append(multiple_list[-1])
               multiple_list.pop()
           for z in multiple_list:
               active_player.hand.append(z)
                   
    elif multi == 1:
        how_many=1
        Discard.append(multiple_list[-1])
    else:
        print "Error!!! That card does not exist in your hand!"
    if how_many <multi:
        
        for x in active_player.hand:
            #print x.name
            if x.card_val != play_card:
                new_hand.append(x) 
            if x.card_val == play_card:
                if square< multi-how_many:
                    new_hand.append(x)
                    square =square+1
    else:
        for x in active_player.hand:
            print x.name
            if x.card_val != play_card:
                new_hand.append(x)
    active_player.hand = new_hand
    
def Start_game(num_players,current_players, Deck):
    Discard_pile =[]
    round_num=1
    Deal(num_players, current_players, Deck)
    
    for y in current_players:
        print "Cards in " + y.name + " up:"
        Show_hand(y.ups)
        print "------------------------------------------------------"

        print "Cards in " + y.name + " hand:"
        Order(y.hand)
        Show_hand(y.hand)
        print '************************************************************'
        
    while Deck !=[]:
        print "------------------------------------------------------"
        print "                       Round #"+ str(round_num) 
        print "------------------------------------------------------"
        
        for x in current_players:
            print x.name + "'s turn"
            Draw(x,Deck)
            Play_Hand(x,Discard_pile)
            print "------------------------------------------------------"
        round_num = round_num + 1


def Main():


#    Show_hand(players[0].hand)
    num_players, players, my_deck = Set_up()

    Start_game(num_players,players, my_deck)    
    
if __name__ == "__main__":
    Main()
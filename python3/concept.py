#################### text base version of Stupid Card Game ####################
# Python 2.7
# By Marcus Holden                
# =============================================================================
# Welcome to SCG. This is a card game I learned about from my Sister-in-Law's 
#Family. They affectionatly refered to it as the Stupid Card Game. For reasons,
# I changed it to SCG. 
# 
# The Basic rules are this:
# Set-up:
# Each player gets 15 cards 
# 5 go faced down on the table in front of you
# 5 go face up on top of the face downs
# 5 go into your hand.
# 
# The remaining deck becomes the draw pile.
# 
# Play:
# The active player draws in turn from the draw pile (until it is depleted) 
# The player than chooses a card to discard. This card must be equal to or lower 
# than the card on the discard (Ace being high). If the player can't play, the 
# discard pile goes into their hand.
# 
# There are 2 sets of wild cards:
# 2's : twos resets the pile such that the next player can play whatever they 
# want on the discard pile. The cards in the discard pile remain.
# 
# 10's : Tens eliminate the discard pile from the game. The next player may play what they want.
# 
# 4 of a kind: if 4 of a kind happens, the pile is discarded, like with a 10.
# 
# The goal of the game is to get rid of all cards in the players hand, and on 
#the table. Order of the cards which a player must get rid of is Hand, Ups, 
#Downs. If a player can't play while on their up's or downs, the discard goes 
#into their hand and the player must get rid of those cards before resuming 
#ridding of the ups or downs.

# The Downs are chosen completly at random.
# 
# The Game ends once any player has no cards in their hand.
# =============================================================================

import random
import sys
import pause
from os import system, name

#Define Player Attrubutes
class Player:
    def __init__(self,player_name, hand, ups, downs,pid):
        self.player_name = player_name
        self.hand = hand
        self.ups = ups
        self.downs = downs
        self.down_list = ['1','2','3','4','5']
        self.org_downs=[]
        self.pid=pid


#Define Card Attrubutes
class Card:
    def __init__(self,suit,card_val,value):
        self.suit = suit
        self.card_val = card_val
        self.value= value
        self.card_name =  card_val+ ' of ' + suit
        
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


# Function to show an array (hand, deck, ups, downs, etc.)
def Show_hand(full_deck):
    for x in full_deck:
        print(x.card_name)

# Fuction to create a deck of cards
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


# Fuction to shuffle a deck of cards
def Shuffle(deck):
    deck = random.shuffle(deck)
    return deck

# Fuction to order cards from low to high based on value
def Order(hand):
    def get_card_val(card):
        return card.value
    hand.sort(key = get_card_val)
    return hand

# Fuction to deal 15 cards to set number of players          
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
        
    for y in range(num_players):
            players[y].org_downs = players[y].downs

#Set up the game
            
def Set_up():

    players=[]

    num_players = 2 # The number of players. Default is 2.
    num_of_decks= 1 # The number of decks. Default is 1
    num_human = input("Enter the number of human players: ") 
    if num_human=='':
        num_human=1
    while int(num_human) < 0:
        num_human = input("Error: Invalid. Enter the number of human players: ") 
    num_human = int(num_human) 
    num_cpu = input("Enter the number of computer players: ") 
    if num_cpu=='':
        num_cpu=0
    while int(num_cpu) < 0:
        num_cpu = input("Error: Invalid. Enter the number of CPU players: ") 
    num_cpu = int(num_cpu) 
    num_players= num_cpu + num_human
    D_pile= (num_of_decks*52)-(15*(int(num_players) )) 
    my_deck =[]
    
    

    for x in range(num_human) :
        my_name= input("Enter Player #"+str(x+1) +"'s name and press enter: ")
        if my_name=="":
            my_name = "Player #"+str(x+1)
        new_player =  Player(player_name = my_name,hand=[], ups=[], downs=[], pid='human')
        players.append(new_player)
        #print players[x].player_name
        
    for x in range(num_cpu) :
        my_name= input("Enter Computer #"+str(x+1) +"'s name and press enter: ")
        if my_name=="":
            my_name = "Computer #"+str(x+1)
        new_player =  Player(player_name = my_name,hand=[], ups=[], downs=[], pid='cpu')
        players.append(new_player)
        #print players[x].player_name

    while  D_pile <= 3*num_players:
         num_of_decks = num_of_decks + 1
         D_pile= (num_of_decks*52)-(15*num_players)         
    
    for x in range(num_of_decks):
        new_deck = Deck()
        for y in new_deck:
            my_deck.append(y)
        
    Shuffle(my_deck)

        
#    print "Number of players: ", num_players 
#    print "Number of decks: ", num_of_decks 
#    print "Draw pile cards: ", D_pile
    return num_players, players, my_deck

# Fuction allowing a player to draw from the draw deck
def Draw(active_player, Deck):
    if Deck != []:
        active_player.hand.append(Deck[-1])
        Deck.pop()
        Order(active_player.hand)

        
    else:
        pass
    
# Fuction allowing a player to play from hand on to the discard deck

def Play_Hand(active_player, Discard):
############### Define new Params ############################################
    multi=0
    low_hand=[]
    multiple_list =[]
    new_hand = []
    values = {'10':1, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'J':11,'j':11,'Q':12,'q':12,'K':13,'k':13,'A':14, 'a':14}        

##################### Ask for a Card ###################    
    while multi == 0:
        if active_player.pid=='human':
            play_card = input("What card value would you like to play? (2-A): ")
        
            
            try:
                my_value = values[play_card]
            except:
                bad=1
                while bad==1:
                    
                    play_card = input("Error: Not a valid choice. What card value would you like to play? (2-A): ")
                    for k in values:
                        if play_card==k:
                            bad=0
################### Check the condition ################################
            if Discard!=[]:
                while my_value > Discard[-1].value:
                     play_card = input("Card must be less than on the discard. What card value would you like to play? (2-A): ")
                     my_value = values[play_card]
        else:
            if Discard!=[]:
                for s in active_player.hand:
                    if s.value<= Discard[-1].value:
                        low_hand.append(s)
                if low_hand==[]:
                    pass
                else:
                    my_value = low_hand[-1].value
                    print(active_player.player_name+ " played " + low_hand[-1].card_name)
                    pause.seconds(2)
            else:
                my_value = active_player.hand[-1].value
                print(active_player.player_name+ " played " + active_player.hand[-1].card_name)
                pause.seconds(2)

            
                
        for x in active_player.hand:
            #print x.card_val
            if x.value == my_value:
                multi = multi + 1
                multiple_list.append(x)
                #active_player.hand.remove(x)
            #Show_hand(active_player.hand)
        
    if multi > 1:
         if active_player.pid=='human':
            play_multi = input("Do you want to play more than one card? (y or n): ") 
         else:
            if my_value >2:   
               play_multi = 'y' 

            else:
               play_multi='n'
               how_many=1
                   
            if play_multi == 'y':                    
               how_many = len(multiple_list)  
         
         if play_multi == 'y':
             if active_player.pid=='human':
                 how_manyS= input("How many would you like to play? : ")
                 how_many = int(how_manyS)
                 if how_many > multi:
                   while how_many > multi:
                       how_manyS= input("Error: Number requested exceeds number in hand. How many would you like to play? : ")
                       how_many = int(how_manyS)
                 if how_many < 0:
                   while how_many < 0:
                       how_manyS= input("Error: Number requested less than 0. How many would you like to play? : ")
                       how_many = int(how_manyS)

                    
                    
             if how_many >= 4:
               Discard=[]
               for z in range(how_many%4):
                   Discard.append(multiple_list[-1])
                   for z in range(how_many):
                       multiple_list.pop()
             else:
               for z in range(how_many):
                   Discard.append(multiple_list[-1])
                   multiple_list.pop()
               
         elif play_multi == 'n':
           multi=1
           how_many =1
           Discard.append(multiple_list[-1])
           multiple_list.pop()
#           for x in active_player.hand:
            #print x.card_name
#            if x.value != my_value:
#                new_hand.append(x) 
           for x in multiple_list:
               new_hand.append(x) 
                   
    elif multi == 1:
        how_many=1
        Discard.append(multiple_list[-1])
        multiple_list.pop()
        
    else:
        print ("Error!!! That card does not exist in your hand!")
   
    if how_many <multi:
      
        for x in active_player.hand:
            #print x.card_name
            if x.value != my_value:
                new_hand.append(x) 
        for x in multiple_list:
            new_hand.append(x) 
                
    elif how_many == multi:
        for x in active_player.hand:
            
            if x.value != my_value:
                new_hand.append(x)
                
    active_player.hand = new_hand

    return Discard
# Fuction allowing a player to play from ups on to the discard deck
    
def Play_ups(active_player, Discard):
############### Define new Params ############################################
    multi=0
    multiple_list =[]
    new_hand = []
    if active_player.pid == 'cpu':
        order_comp=[]
        low_hand=[]
        order_comp = active_player.ups
        order_comp =Order(order_comp)
    values = {'10':1, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'J':11,'j':11,'Q':12,'q':12,'K':13,'k':13,'A':14, 'a':14}        

##################### Ask for a Card ###################    
    while multi == 0:
        if active_player.pid=='human':
            play_card = input("What card value would you like to play? (2-A): ")
            my_value = values[play_card]

################### Check the condition ################################
            if Discard!=[]:
                while my_value > Discard[-1].value:
                     play_card = input("Card must be less than on the discard. What card value would you like to play? (2-A): ")
                     my_value = values[play_card]
        else:
            if Discard!=[]:
                for a in order_comp:
                    if a.value<= Discard[-1].value:
                        low_hand.append(a)
                my_value = low_hand[-1].value  
                print(active_player.player_name+ " played " + low_hand[-1].card_name)
                pause.seconds(2)
            else:
                my_value = order_comp[-1].value
                print(active_player.player_name+ " played " + order_comp[-1].card_name)
                pause.seconds(2)

            
        for x in active_player.ups:
            #print x.card_val
            if x.value == my_value:
                multi = multi + 1
                multiple_list.append(x)
                #active_player.hand.remove(x)
            #Show_hand(active_player.hand)
        
        if multi > 1:
            if active_player.pid=='human':
                play_multi = input("Do you want to play more than one card? (y or n): ") 
            else:
                if my_value >2:   
                    play_multi = 'y' 

                else:
                    play_multi='n'
                    how_many=1
        else:
            play_multi='n'
            how_many=1
                   
         
        if play_multi == 'y':
             if active_player.pid=='human':
                 how_manyS= input("How many would you like to play? : ")
                 how_many = int(how_manyS)
                 if how_many > multi:
                   while how_many > multi:
                       how_manyS= input("Error: Number requested exceeds number in hand. How many would you like to play? : ")
                       how_many = int(how_manyS)
                 if how_many < 0:
                   while how_many < 0:
                       how_manyS= input("Error: Number requested less than 0. How many would you like to play? : ")
                       how_many = int(how_manyS)
             else:
                        
                 if play_multi == 'y':                    
                    how_many = len(multiple_list)  
                    
                    
             if how_many >= 4:
               Discard=[]
               for z in range(how_many%4):
                   Discard.append(multiple_list[-1])
                   for z in range(how_many):
                       multiple_list.pop()
             else:
               for z in range(how_many):
                   Discard.append(multiple_list[-1])
                   if active_player.pid=='cpu':
                       print(active_player.player_name + " played "+ multiple_list[-1].card_name)
                   multiple_list.pop()
               
        elif play_multi == 'n':
           multi=1
           how_many =1
           Discard.append(multiple_list[-1])
           multiple_list.pop()
#           for x in active_player.hand:
            #print x.card_name
#            if x.value != my_value:
#                new_hand.append(x) 
           for x in multiple_list:
               new_hand.append(x) 
                   


        else:
            print ("Error!!! That card does not exist in your hand!")
   
    if how_many <multi:
      
        for x in active_player.hand:
            #print x.card_name
            if x.value != my_value:
                new_hand.append(x) 
        for x in multiple_list:
            new_hand.append(x) 
                
    elif how_many == multi:
        for x in active_player.ups:
            
            if x.value != my_value:
                new_hand.append(x)
                
    active_player.ups = new_hand

    return Discard

# Fuction allowing a player to play from hand on to the discard deck
def Play_downs(active_player, Discard):
############### Define new Params ############################################
    
    card_list ={'1':0,'2':1,'3':2,'4':3,'5':4}
    my_Discard=0
    new_downs=[]
    new_dl=[]
    player = active_player
    same_card=0
##################### Ask for a Card ###################    
# =============================================================================
#     for x in player.org_downs:
#         print x.card_name
#     print "len(org_down):", len(player.org_downs)
# =============================================================================
    if active_player.pid=='human':
        play_card = input("What card value would you like to play from the downs? (1-5): ")
        while play_card not in active_player.down_list:
            play_card = input("Error: Card not in list. What card value would you like to play from the downs? (1-5): ")
    else:
        play_card = random.choice(active_player.down_list)
    
    my_card=card_list[play_card]

    my_card_name=active_player.org_downs[my_card].card_name
    if active_player.pid=='human':
        print ("you played: ", my_card_name)
    #print (player.org_downs[my_card].card_name)
    elif active_player.pid == 'cpu':
            print(active_player.player_name+ " chose " + play_card)
            print(active_player.player_name+ " played " + my_card_name)
            pause.seconds(2)

    if Discard != []:
        if active_player.org_downs[my_card].value <= Discard[-1].value:
            Discard.append(active_player.org_downs[my_card])
            for x in active_player.downs:
                if same_card==0:
                    if x.card_name == my_card_name:
                        same_card+=1
                        pass
                    else:
                        new_downs.append(x)
                else:
                    new_downs.append(x)
            player.downs=new_downs
            
            #active_player.down_list.remove(play_card)

        else:
            Discard.append(active_player.org_downs[my_card])
            
            for x in Discard:
                if x.value == 15:
                    x.value = 2
                active_player.hand.append(x)
            Order(active_player.hand)
            my_Discard=1
            for x in active_player.downs:
                if same_card==0:
                    if x.card_name == my_card_name:
                        same_card+=1
                        pass
                    else:
                        new_downs.append(x)
                else:
                    new_downs.append(x)
            player.downs=new_downs
# =============================================================================
#             print "You must pick up the discard pile"
# =============================================================================

    else:
        Discard.append(active_player.org_downs[my_card])
        for x in active_player.downs:
            if same_card==0:
                if x.card_name == my_card_name:
                    same_card+=1
                    pass
                else:
                    new_downs.append(x)
            else:
                new_downs.append(x)
        
        active_player.downs=new_downs
    for x in active_player.down_list:
        if x== play_card:
            pass
        else:
            new_dl.append(x)
    
    active_player.down_list = new_dl
        

    return my_Discard





################### Check the condition ################################

# Fuction starting the game            
def Start_game(num_players,current_players, Deck):
    Discard_pile =[]

    round_num=1
    
    Deal(num_players, current_players, Deck)

#=============================================================================
    # Deck = []
    # for x in current_players:
    #     x.hand=[]
    #     x.ups=[]
#=============================================================================

    
    won=0
    

    #print '*****************************************************************************'
        
    while won==0:

    
        for x in current_players:
            pause.seconds(1)
            clear()
            
            for y in range(15):
                print('')
                
            print( '                                             '+x.player_name + "'s turn")
            input('                                             Press enter to continue:')
            clear()
            
            my_hand=''
            my_discard =''
            my_ups = ''
            my_downs=''
            check=0
            play=0
            if Discard_pile !=[]:
                
                if Discard_pile[-1].value == 1:
                    Discard_pile=[]
                elif Discard_pile[-1].value==2:
                    Discard_pile[-1].value=15
                try:
                    if Discard_pile[-1].value == Discard_pile[-2].value:
                        if Discard_pile[-2].value == Discard_pile[-3].value:
                            if Discard_pile[-3].value == Discard_pile[-4].value:
                                Discard_pile=[]
                except:
                    pass
            
            #print x.player_name + "'s turn"
            clear()
            Draw(x,Deck)

            print ('###########################################################')
            print ('                           Round #'+ str(round_num) )
            print ('                      '+x.player_name + "'s turn")
            print ('')
            if x.pid=='human':
                print ('  1: Play a card ')
                print ('  2: Pick up the discard pile ')
                print ('  3: Quit ')
            print ('')
            print ("-----------------------------------------------------------")
            for s in Discard_pile:
                my_discard =  my_discard +' | '+ s.card_name
            if Discard_pile ==[]:
                print (" Discarded Pile: " )
            else:
                print (" Discarded Pile: " ,my_discard + ' |')
        
            print ('')
            print ('' ) 
            

            
        
            print (" Cards in draw pile: ", len(Deck))
            print ("")
            print ("-----------------------------------------------------------")
            for s in x.hand:
                my_hand = my_hand +' | '+ s.card_name
            for s in x.ups:
                my_ups = my_ups +' | '+ s.card_name
            for s in x.down_list:
                my_downs = my_downs +' | '+ s
            if x.pid=='human':    
                if x.hand != []:
                    print (' '+ x.player_name + '\'s hand: ' + my_hand +' |')
                    print( "-------------------------------------------------------")
                    print( '')
                    print (' '+ x.player_name + '\'s up: ' + my_ups +' |')
                    print ('')
                    print ("")
            
                elif x.ups != []:
                    print (' '+ x.player_name + '\'s up: ' + my_ups +' |')
                    print ('')
                else:
                    print (' '+ x.player_name + '\'s downs: ' + my_downs + ' |')
            else:
                # if x.hand != []:
                #     print (' '+ x.player_name + '\'s hand: ' + my_hand +' |')
                #     print( "-------------------------------------------------------")
                #     print( '')
                #     print (' '+ x.player_name + '\'s up: ' + my_ups +' |')
                #     print ('')
                #     print ("")
            
                if x.ups != []:
                    print (' '+ x.player_name + '\'s up: ' + my_ups +' |')
                    print ('')
                else:
                    print (' '+ x.player_name + '\'s downs: ' + my_downs + ' |')
            print ('###################################################################')
        
            if x.pid=='human':
                my_choice = input('Choose an option: ')
            else:
                my_choice = '1'
                
            if my_choice =='1':
                check=1
            elif my_choice =='2':
                check=1
            elif my_choice =='3':
                endit=input("Are you sure you want to quit? (y or n):")
                if endit=='y':
                    print ("Goodbye!")
                    pause.seconds(2)
                    sys.exit()
                else:
                    new_choice=0
                    while new_choice != 1:
                        
                        my_choice = input('Choose a main option: ')
                        if my_choice =='1':
                            check=1
                            new_choice = 1
                        elif my_choice =='2':
                            check=1
                            new_choice = 1
                        elif my_choice =='3':
                            print ("Goodbye!")
                            pause.seconds(2)
                            sys.exit()
            while check != 1:
                print( 'not a valid option')
                my_choice = input('Choose an option: ')
                
                if my_choice =='1':
                    check=1
                elif my_choice =='2':
                    check=1
                elif my_choice =='3':
                    check=1
                else:
                    pass
            if my_choice == '1':
                if Discard_pile !=[]:
                    if x.hand !=[]:
                        for y in x.hand:
                             if y.value <= Discard_pile[-1].value:
                                Discard_pile= Play_Hand(x,Discard_pile)
                                break
        
                        
                             else:
                                 clear()
                                 for y in range(15):
                                     print('')
                                
                                 print( '                                             '+x.player_name + "'s turn")
                            
                                 print( '                                             You must pick up the Discard!!!!!!')
                                 pause.seconds(1)
                                 clear()
                                 
                                 for z in Discard_pile:
                                     if z.value == 15:
                                         z.value = 2
                                     x.hand.append(z)
                                 Order(x.hand)
                                 Discard_pile=[]
                                 break
                         
                    elif x.ups !=[]:
                        for y in x.ups:
                             if y.value <= Discard_pile[-1].value:
                                 Play_ups(x,Discard_pile)
                                 play=1
                                 break
        
                        
# =============================================================================
#                              else:
#                                  too_big.append(y)
# =============================================================================

                        if play ==0:
                            
                             clear()
                             for y in range(15):
                                print('')
                                
                             print( '                                             '+x.player_name + "'s turn")
                            
                             print( '                                             You must pick up the Discard!!!!!!')
                             pause.seconds(1)
                             clear()
                             for z in Discard_pile:
                                 if z.value == 15:
                                     z.value = 2
                                 x.hand.append(z)
                             Order(x.hand)
                             Discard_pile=[]
                             break
                    else:
                         my_discard=Play_downs(x, Discard_pile)
                         if my_discard ==1:
                            Discard_pile=[]
                            clear()
                            for y in range(15):
                                print('')
                                
                            print( '                                             '+x.player_name + "'s turn")
                            
                            print( '                                             You must pick up the Discard!!!!!!')
                            pause.seconds(1)
                            clear()
                        
                             
                else:
                    if x.hand != []:
                        Play_Hand(x,Discard_pile)
                    elif x.ups != []:
                        Play_ups(x,Discard_pile)
                    else:
                        Play_downs(x,Discard_pile)
                    
            elif my_choice == '2':
                 print ('You must pick up the Discard pile!!!!!!')
                 clear()
                 for y in range(15):
                     print('')
                   
                 print( '                                             '+x.player_name + "'s turn")
               
                 print( '                                             You must pick up the Discard!!!!!!')
                 pause.seconds(1)
                 clear()
                 for z in Discard_pile:
                     if z.value == 15:
                         z.value = 2
                     x.hand.append(z)
                 Order(x.hand)
                 Discard_pile=[]

            
            elif my_choice == '3':
                print ("Goodbye!")
                pause.seconds(2)
                sys.exit()
            print ("-----------------------------------------------------------")
            if x.downs==[]:
                if x.hand==[]:
                    print( x.player_name + " WINS!!!!!!!!!!!!!!!!")
                    replay=input("Want to play again? (y or n): ")
                    won=1
                    break
                else:
                    pass        
        


            
                
        round_num = round_num + 1
    
    return replay

def Main():
    
    clear()
    print ('###################################################################')
    print ('#                        Welcome to SCG v0.5                      #')

    menu=5
    while menu!=4:
        print ('###################################################################')
        print ('#                             1: Play!                            #')
        print ('#                             2: Rules                            #')
        print ('#                             3: About                            #')
        print ('#                             4: Exit                             #')
        print ('###################################################################')
        menu=input('choose an option (1-4): ')
        if menu=='1':
            replay='y'
            while replay == 'y':
            #    Show_hand(players[0].hand)
                num_players, players, my_deck = Set_up()
            
                replay = Start_game(num_players,players, my_deck)    
            input('Thanks for playing! Press enter to close:')
        elif menu=='2':
            print('                        Rules')
            print('''                        Set-up:
 Each player gets 15 cards
 5 go faced down on the table in front of you
 5 go face up on top of the face downs
 5 go into your hand.
 
 The remaining deck becomes the draw pile.
 
                         Play:
 The active player draws in turn from the draw pile (until it is depleted) 
 The player than chooses a card to discard. This card must be equal to or lower 
 than the card on the discard (Ace being high). If the player can't play, the 
 discard pile goes into their hand.
 
 There are 2 sets of wild cards:
 2's : twos resets the pile such that the next player can play whatever they 
 want on the discard pile. The cards in the discard pile remain.
 
 10's : Tens eliminate the discard pile from the game. The next player may play what they want.
 
 4 of a kind: if 4 of a kind happens, the pile is discarded, like with a 10.
 
 The goal of the game is to get rid of all cards in the players hand, and on 
the table. The order of the cards which a player must get rid of is: Hand, Ups, 
Downs. If a player can't play while on their up's or downs, the discard goes 
into their hand and the player must get rid of those cards before resuming 
ridding of the ups or downs.

 The cards facing down (Downs) are chosen completly at random.

 The game ends once any player has no cards in their hand.''')
        elif menu=='3':
            print('                        About')
#            print('                        Stupid Card Game')
            print('''
Welcome to SCG. This is a card game I learned about from my Sister-in-Law's 
family. They affectionatly refer to it as the Stupid Card Game.
            
                    App Developed by Marcus Holden
                          Version 0.5''')
        elif menu=='4':
            print('Goodbye')
            sys.exit()
        else:
            menu=input('choose an option (1-4): ')
if __name__ == "__main__":
    Main()

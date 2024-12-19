import random
import streamlit as st
import os

##################################################################################################################################################################

                                                # # # Black Jack # # #

# this script runs a basic version of the game Black Jack (this means that advanced features such as "split", "doubling down", "insurance" etc. are not present)
# the script leverages the Streamlit library to seamless integrate the game with a visual component
# the ruls of the game can be found at (https://www.venetianlasvegas.com/resort/casino/table-games/how-to-play-blackjack.html)

##################################################################################################################################################################




######################################################################################################

# # # Function Section # # #

######################################################################################################

#define a function to build and return a shuffled deck of cards
def build_deck():
    suits = {'Hearts': 'H', 'Diamonds': 'D', 'Clubs': 'C', 'Spades': 'S'}           #dictionary of suits with their abbreviations
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']     #lists of card values
    deck = [f"{value} of {suit}" for suit in suits for value in values]             #vuild a list for the full deck 
    random.shuffle(deck)                     #shuffle deck to randomize order
    return deck                              #returns the shuffled deck 

#defined a function to get the image file path for a given card
def get_card_image_path(card):
    suits_abbreviation = {'Hearts': 'H', 'Diamonds': 'D', 'Clubs': 'C', 'Spades': 'S'}      #dictionary to map suit names to abbreviations
    value, suit = card.split(" of ")            #split card string into value and suit
    card_filename = value + suits_abbreviation[suit] + ".jpg"   #build card image filename
    return os.path.join("cards", card_filename)                 #return the path by joning directory and filename

#this function is crucial for the whole game and it returns the last card in the shuffled deck 
def draw_card(deck):
    return deck.pop() if deck else None 

#Creating a specific function for calculating the hand value of both player and dealer:
def calculate_hand_value(hand):
    value = 0                           #we create a variable which contains the card's summed value
    aces = 0                            #and another variable which contains the value of aces as in blackjack they can have different values.            
    for card in hand:                   #creating a For loop to associate the right value to the right card:
        rank = card.split(" ")[0]       #creating a variable called rank which contains cards splitted by space
        if rank in ['J', 'Q', 'K']:     #we create if condition with a list of card name J, Q, K
            value += 10                 #Giving them the value of 10
        elif rank == 'A':               #if it's an ace it can value eiter 11 or 1
            aces += 1
            value += 11
        else:
            value += int(rank)          #if the card is neither an ace or a face card, then the value will be the exact same as the card showed. (i.e. value = 10;  rank = 3; value printed = 13)

    while value > 21 and aces:         #If the value is over 21, determining user's loss, the aces can be decreased to the value:
        value -= 10                    # of 1 (as it can be = 11 or 1). so we create a While loop that can decrease the value
        aces -= 1                      # of the aces by 10 (=1) while the variable value is greater than 21. (Aces in the deck
    return value                        


#######################################################################################################

# # # Streamlit Section # # # 

#######################################################################################################

# Streamlit UI
st.title("Blackjack Game")                      #title

st.image("Images/Blackjack_img.webp")         #image
st.divider() 

st.subheader("Click here to start the game")

# Session State
if 'deck' not in st.session_state:              #check if deck is not in sessionstate
    st.session_state.deck = build_deck()        #if not, initialize the deck by calling function "build_deck"
if 'player_hand' not in st.session_state:       #check if "player_hand" is not in session state
    st.session_state.player_hand = []           #if not, initialize "player_hand" as empty list
if 'dealer_hand' not in st.session_state:       #check if "dealer_hand" is not in session state
    st.session_state.dealer_hand = []           #if not, initialize dealer's hand as empty list
if 'game_over' not in st.session_state:         #check if "game_over" is not in session state
    st.session_state.game_over = False          #if not, set "game over" to FALSE
if 'player_value' not in st.session_state:      #check if "player_value" is not in session state
    st.session_state.player_value = 0           #if not, initialize "player_value" as 0
if 'dealer_value' not in st.session_state:      #check if "dealer_value" is not in session state
    st.session_state.dealer_value = 0           #if not, initialize dealer_value as 0
if 'game_started' not in st.session_state:      #check if "game_started" is not in session state
    st.session_state.game_started = False       #if not, set game_started to FALSE
if 'drawn_card' not in st.session_state:        #check if "drawn_card" is not in session state
    st.session_state.drawn_card = None          #if not, initialize "drawn_card" as None


# Start game
if not st.session_state.game_started:           #checks if the game has not started yet
    if st.button("Start Game"):                 #display a button, and if clicked: 
        st.session_state.game_started = True    #set "game_started" to TRUE
        st.session_state.player_hand = [draw_card(st.session_state.deck), draw_card(st.session_state.deck)]     #deal two cards to player
        st.session_state.dealer_hand = [draw_card(st.session_state.deck), draw_card(st.session_state.deck)]     #deal two cards to dealer
        st.session_state.player_value = calculate_hand_value(st.session_state.player_hand)                      #calculate player's initial hand value
        st.session_state.dealer_value = calculate_hand_value(st.session_state.dealer_hand)                      #caluclated dealer's initial hand value



# Display player and dealer hands
if st.session_state.game_started:       #if the game ahs started
    st.subheader("Your Hand")           #display player's hand section
    st.write(f"Value: {st.session_state.player_value}")                 # Display player's current hand value
    player_card_cols = st.columns(len(st.session_state.player_hand))    #create columns for each player's card for better visualization
    for idx, card in enumerate(st.session_state.player_hand):           #iterate over palyer's cards
        with player_card_cols[idx]:                                     #place each card image in its own col
            st.image(get_card_image_path(card), width=100)              #display card image for the player's card

    if st.session_state.drawn_card:                                     #if a card was recently drawn: 
        st.write(f"You drew: {st.session_state.drawn_card}")            #display the drawn card

    st.subheader("Dealer's Hand")                                       #display the dealer's hand section   
    dealer_card_cols = st.columns(len(st.session_state.dealer_hand))    #create cols for each dealer's card
    for idx, card in enumerate(st.session_state.dealer_hand):           #iterate over dealer's cards
        with dealer_card_cols[idx]:                                     #place each card image in its own col
            st.image(get_card_image_path(card), width=100)              #display card image for the dealer's card
    st.write(f"Value: {st.session_state.dealer_value}")                 #display the dealer's current hand value



# Player actions
if st.session_state.game_started and not st.session_state.game_over:   #if the game is started and not over yet:
    col1, col2 = st.columns(2)                                         #create two cols for "Hit" and "Stand" buttons
    with col1:                      #in the first column
        if st.button("Hit"):        #if player clicks "Hit":
            new_card = draw_card(st.session_state.deck)                #draw new card for the player
            st.session_state.player_hand.append(new_card)              #append new card to player's hand
            st.session_state.player_value = calculate_hand_value(st.session_state.player_hand)      #recalculate new player's hand value
            st.session_state.drawn_card = new_card  #store the drawn card for display

            if st.session_state.player_value > 21:  #check if palyer value exceed 21 (burst)
                st.session_state.game_over = True   #if so, game is over because player burst

            st.experimental_rerun()  #force rerun to immediately update UI

    with col2:
        if st.button("Stand"):                  #in the second column, if player click "stand":
            while st.session_state.dealer_value < 17:    #dealer must draw until hand value is at least 17 (game rules)
                st.session_state.dealer_hand.append(draw_card(st.session_state.deck))   #dealer draws a card
                st.session_state.dealer_value = calculate_hand_value(st.session_state.dealer_hand)    #recalculate dealer's value
            st.session_state.game_over = True           #after the dealer finishes, the game is over   
            st.experimental_rerun()                     #return to update UI



# Determine winner
if st.session_state.game_over:                          #if the game is over
    if st.session_state.player_value == 21:
        st.success("BLACK JACK")
    if st.session_state.player_value > 21:              #if player "busted"
        st.error("Bust! You lose.")                     #inform player that he has lost
    elif st.session_state.dealer_value > 21 or st.session_state.player_value > st.session_state.dealer_value:   #if dealer bust or player value is closer to 21
        st.success("You win!")                          #player wins
    elif st.session_state.player_value == st.session_state.dealer_value:    #if tie
        st.warning("It's a tie!")                       #announce tie         
    else:
        st.error("You lose!")                           #otherwise, dealer wins

    if st.button("Restart Game"):                       #if player wants to restart.
        st.session_state.deck = build_deck()            #rebuild the deck
        st.session_state.player_hand = []               #reset player's hand
        st.session_state.dealer_hand = []               #reset dealer's hand
        st.session_state.game_over = False              #set game over to FALSE
        st.session_state.player_value = 0               #reset player value
        st.session_state.dealer_value = 0               #reset dealer value
        st.session_state.game_started = False           #set game started to FALSE
        st.session_state.drawn_card = None              #clear the drawn cards

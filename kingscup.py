import os
import random #import random to randomise the deck of cards in build_deck
import streamlit as st

# Function to build and shuffle the deck
def build_deck(): #A function that builds a classic deck of 52 cards
    suits = {'Hearts': 'H', 'Diamonds': 'D', 'Clubs': 'C', 'Spades': 'S'} #A dictionary that references the 4 card suits in a classic deck of cards
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] #A dictionary that references the values of the cards in a classic deck of cards
    deck = [f"{value} of {suit}" for suit in suits for value in values] #A list that adds 52 cards - 13 different values over 4 different suits
    random.shuffle(deck) #randomises the deck
    return deck #returns a shuffled deck of 52 cards (or 54 if include_jokers=True)

# Card Image Path Helper, this function 
def get_card_image_path(card):
    """Convert full card name to the corresponding image path."""
    suits_abbreviation = {'Hearts': 'H', 
                          'Diamonds': 'D',
                          'Clubs': 'C',
                          'Spades': 'S'} #Dictionary that calls the suit of the card's image to match naming of .jpg cards in the "cards"folder
    value, suit = card.split(" of ") #e.g. 3 of Spades
    card_filename = value + suits_abbreviation[suit] + ".jpg"  # e.g., '3S.jpg'
    return os.path.join("cards", card_filename)

# Initialize Streamlit Session State to save cards in the streamlit session state
if 'deck' not in st.session_state:
    st.session_state.deck = build_deck()         #if "deck" is not present in the current session, run buld_deck() function
if 'kings_drawn' not in st.session_state:        #if "kings_drawn" is not in session state, the value of kings_drawn will start from 0
    st.session_state.kings_drawn = 0
if 'last_card' not in st.session_state:         #if the last card is not in the session state, return none
    st.session_state.last_card = None

# Actions for cards
actions = { #A dictionary that calls an action for the corresponding value of the card
    '2': "Pick someone to drink!", #The action when the card's value is 2
    '3': "You drink!", #The action when the card's value is 3
    '4': "All GUYS drink!", #The action when the card's value is 4
    '5': "Play Five Ten!", #The action when the card's value is 5
    '6': "All LADIES drink!", #The action when the card's value is 6
    '7': "Last person to stand up drinks!", #The action when the card's value is 7
    '8': "Pick someone to drink with you!", #The action when the card's value is 8
    '9': "Say a word, next person must rhyme. Loser drinks!", #The action when the card's value is 9
    '10': "Pick a category. Go around until someone can't answer. They drink!", #The action when the card's value is 10
    'J': "Never Have I Ever - Everyone puts up 3 fingers. First to drop all fingers drinks!", #The action when the card's value is J
    'Q': "Silent Queen - No one can talk to you until the next Queen. Rule-breakers drink!", #The action when the card's value is Q
    'K': "King's Cup! Pour a bit of your drink into the cup. The 4th King drinks it all!", #The action when the card's value is K
    'A': "Set a new rule that lasts the game! Be creative!" #The action when the card's value is A
}

# Streamlit UI
st.title("Card Game Web App")                        #display title
st.subheader("Draw a card and see what happens!")    #display subheader
    
if st.button("Draw a Card"):                        #visual button to trigger exection
    if st.session_state.deck:                       #if there is a deck in the current session_state:
        card = st.session_state.deck.pop()          #remove the last card from the card  
        st.session_state.last_card = card
        st.write(f"You drew: **{card}**")

        # Display card action
        card_value = card.split()[0]
        if card_value == 'K':
            st.session_state.kings_drawn += 1
            st.write(f"King drawn! Kings so far: {st.session_state.kings_drawn}")
            if st.session_state.kings_drawn == 4:
                st.write("🎉 The 4th King has been drawn! Game over! 🎉")
        else:
            st.write(actions.get(card_value, "No action for this card."))

        # Display card image
        card_image_path = get_card_image_path(card)
        if os.path.exists(card_image_path):
            st.image(card_image_path, caption=f"{card}", width=150)
        else:
            st.write("Card image not found!")
    else:
        st.write("No more cards left! Reset the deck to play again.")

if st.button("Reset Deck"):
    st.session_state.deck = build_deck()
    st.session_state.kings_drawn = 0
    st.session_state.last_card = None
    st.write("The deck has been reset. Let's play!")

# Display Remaining Cards
st.write(f"Cards remaining: {len(st.session_state.deck)}")



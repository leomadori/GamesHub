import os
import random
import streamlit as st

# Function to build and shuffle the deck
def build_deck(include_jokers=False):
    suits = {'Hearts': 'H', 'Diamonds': 'D', 'Clubs': 'C', 'Spades': 'S'}
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{value} of {suit}" for suit in suits for value in values]
    if include_jokers:
        deck.extend(['Joker', 'Joker'])
    random.shuffle(deck)
    return deck

# Card Image Path Helper
def get_card_image_path(card):
    """Convert full card name to the corresponding image path."""
    suits_abbreviation = {'Hearts': 'H', 'Diamonds': 'D', 'Clubs': 'C', 'Spades': 'S'}
    value, suit = card.split(" of ")
    card_filename = value + suits_abbreviation[suit] + ".jpg"  # e.g., '3S.jpg'
    return os.path.join("cards", card_filename)

# Initialize Streamlit Session State
if 'deck' not in st.session_state:
    st.session_state.deck = build_deck()
if 'kings_drawn' not in st.session_state:
    st.session_state.kings_drawn = 0
if 'last_card' not in st.session_state:
    st.session_state.last_card = None

# Actions for cards
actions = {
    '2': "Pick someone to drink!",
    '3': "You drink!",
    '4': "All GUYS drink!",
    '5': "Play Five Ten!",
    '6': "All LADIES drink!",
    '7': "Last person to stand up drinks!",
    '8': "Pick someone to drink with you!",
    '9': "Say a word, next person must rhyme. Loser drinks!",
    '10': "Pick a category. Go around until someone can't answer. They drink!",
    'J': "Never Have I Ever - Everyone puts up 3 fingers. First to drop all fingers drinks!",
    'Q': "Silent Queen - No one can talk to you until the next Queen. Rule-breakers drink!",
    'K': "King's Cup! Pour a bit of your drink into the cup. The 4th King drinks it all!",
    'A': "Set a new rule that lasts the game! Be creative!"
}

# Streamlit UI
st.title("Card Game Web App")
st.subheader("Draw a card and see what happens!")

if st.button("Draw a Card"):
    if st.session_state.deck:
        card = st.session_state.deck.pop()
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



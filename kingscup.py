# -*- coding: utf-8 -*-
#Coding project
#to do: 
    #Fix documentation
    #come up with more games
    #improve length
import random

def build_deck(include_jokers=False):
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{value} of {suit}" for suit in suits for value in values]
    if include_jokers:
        deck.extend(['Joker', 'Joker']) #do we really need jokers?
    random.shuffle(deck)
    return deck

def draw_card(deck):
    return deck.pop() if deck else None #

def reset_deck(include_jokers=False):
    return build_deck(include_jokers) # do we need jokers? maybe recode

def play_kings_cup(deck): #dictionary, too long though
    actions = {
        '2': "Pick someone to drink!",
        '3': "You drink!",
        '4': "All GUYS drink!",
        '5': "Play Five Ten",
        '6': "All LADIES drink!",
        '7': "Last person to stand up drinks!",
        '8': "Pick someone to drink with you!",
        '9': "Say a word, next person must rhyme. Loser drinks!",
        '10': "Pick a category. Go around until someone can't answer. They drink!",
        'J': "Everyone puts up 3 fingers. Go around with 'Never Have I Ever' statements. Whoever drops all fingers first drinks!",
        'Q': "Until the next Queen is drawn, no one can talk to you. Anyone who does, drinks!",
        'K': "King's Cup - Pour a bit of your drink into the King's Cup. The person who draws the 4th King drinks it!",
        'A': "Set a new rule that lasts the entire game! Rules can stack >:)" ##add multiple queens
    }
    kings_drawn = 0
    game_over = False

    while not game_over and deck:
        input("Press Enter to draw a card...")
        card = draw_card(deck)
        if not card:
            print("No more cards left. The game is over!")
            break

        card_value = card.split()[0]
        print(f"\nYou drew: {card}")

        if card_value == 'K':
            kings_drawn += 1
            print(f"{actions[card_value]} (Kings drawn so far: {kings_drawn})")
            if kings_drawn == 4:
                print("\nThe fourth King has been drawn! The game is over!")
                game_over = True
        else:
            print(actions.get(card_value, "No action for this card."))

def play_higher_lower(deck):
    current_card = draw_card(deck)
    print("Starting card is:", current_card)

    while deck:
        guess = input("Will the next card be 'higher' or 'lower'? ").strip().lower()
        if guess not in ['higher', 'lower']:
            print("Invalid input. Please enter 'higher' or 'lower'.")
            continue  
        next_card = draw_card(deck)
        print("Next card is:", next_card)

        if (guess == 'higher' and next_card > current_card) or (guess == 'lower' and next_card < current_card):
            print("You guessed correctly!")
        else:
            print("Wrong guess! Take a shot! Game over.")
            break     
        current_card = next_card

def play_card_guess(deck):
    print("Welcome to Card Guess! Try to guess the value or suit of the next card.")
    score = 0

    while deck:
        guess_type = input("Do you want to guess the 'value' or 'suit' of the card? ").strip().lower()
        if guess_type not in ['value', 'suit']:
            print("Invalid input. Please enter 'value' or 'suit'.")
            continue

        card = draw_card(deck)
        card_value, card_suit = card.split(" of ")
        guess = input(f"Guess the card's {guess_type}: ").strip().capitalize()

        if (guess_type == 'value' and guess == card_value) or (guess_type == 'suit' and guess == card_suit):
            print(f"Correct! The card was {card}.")
            score += 1
        else:
            print(f"Incorrect. The card was {card}.")
            break

    print(f"Game over! Your score: {score}")

def choose_game():
    deck = reset_deck(include_jokers=False)
    game_options = {
        "kings cup": play_kings_cup,
        "higher lower": play_higher_lower,
        "card guess": play_card_guess
    }

    while True:
        choice = input("\nChoose a game (Kings Cup, Higher Lower, Card Guess): ").strip().lower()
        if choice in game_options:
            print(f"\nStarting {choice.title()}!")
            game_options[choice](deck)
            break
        elif choice == "quit":
            return ("No worries, have a good one!")
        else:
            print("Invalid choice. Please enter one of the provided game names.")

# Run the game selector
choose_game()

#add two players via clases, use github to make the  UI nice (selfstudy) 
#trivia.blackjack
#commenting - (see any other github readme) - try to
# come up with this (follow a template and look into it)
#button to restart game or a menu button.
#/sd. !!! - 14 november
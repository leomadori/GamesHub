# Games Hub
![Local Image](./Images/GH_logo.webp)

# 1. Program Description
Thanks for visiting our page!

Our code offers a platform for fun and exiting games to play when you are bored. Using Streamlit, we created an easy-access interface from which to choose your games from. Enjoy your time trying our games! :)

# 2. Features

Our application features streamlit, therefore it is imperative that Streamlit is installed on your machine.  

Run `pip install streamlit` to install streamlit in your working environment

In our script we also used other libraries. In order to run the application, please run the following commands:  

- `pip install random`  

- `pip install os` 

- `pip install json`  

- `pip install requests`  

- `pip install html`  

### Running the code

After having installed all the libraries, go to the terminal and run:  

`streamlit run Home.py` 

You will be redirected to your preferred browser to the homepage!

## 2.1 King's Cup

### Game Description 
King' Cup is a card-based game where players take turns to draw cards and follow prompts. Each unique value of a card has a prompt associated with it, and the prompts remain the same regardless of the suit of the card (i.e., there are 13 different prompts * 4 different card suits). As the name suggests, the game revolves around the cards with the "King" value, with the game ending when the 4th King has been drawn.

### Game Flow 
Designate an empty cup as the "King's Cup". After deciding who draws the cards first (i.e. via drawing lots or whichever method the players are comfortable with), the players will take turns drawing a card every turn. After each card's prompt has been played out, the next player in order (clockwise or anti-clockwise) will draw their card. Rinse and repeat. 

### Card Values and Prompts 
In this version of the game, the card's values have the following associated prompts.   
  
- **'2': "Pick someone to drink!"**  
When any card with the value of 2 is drawn, the person who draws it can nominate someone to drink their beverage.  
  
- **'3': "You drink!"**  
When any card with the value of 3 is drawn, the person who draws it must drink their beverage.  
  
- **'4': "All GUYS drink!"**  
When any card with the value of 4 is drawn, all male players will have to drink their beverage, regardless of whether they drew the card or not.  
  
- **'5': "Play Five Ten!"**  
When any card with the value of 5 is drawn, a mini-game of "Five Ten" begins. "Five Ten" requires all players to put up a hand, and for each turn in the game, all players can choose to leave their hand open (indicating a value of 5) or closed in a fist (indicating a value of 0). Players will take turns guessing the sum of all players' hands and the first to do so correctly will force the rest of the players to drink their beverage.   
  
- **'6': "All LADIES drink!"**  
When any card with the value of 6 is drawn, all female players will have to drink their beverage, regardless of whether they drew the card or not.  
  
- **'7': "Last person to stand up drinks!"**  
When any card with the value of 7 is drawn, all players must stand up from their seats (or sit down if they are standing for some reason). The last person to do so must drink their beverage.  
  
- **'8': "Pick someone to drink with you!"**  
When any card with the value of 8 is drawn, the person who draws it can pick another player to drink their beverage with whenever they are called upon to drink their beverage within the rules of the game.   
  
- **'9': "Say a word, next person must rhyme. Loser drinks!"**  
When any card with the value of 9 is drawn, the player who draws it can choose a word. All players that follow must say words that rhyme with the chosen word, and this continues until one person fails to rhyme with the chosen word. The said person must drink their beverage.  
  
- **'10': "Pick a category. Go around until someone can't answer. They drink!"**  
When any card with the value of 10 is drawn, the player who draws it can choose a category. All players that follow must name objects that fit into the category, and this continues until one person fails to do so. The said person must drink their beverage.  
  
- **'J': "Never Have I Ever - Everyone puts up 3 fingers. First to drop all fingers drinks!"**  
When any card with the value of J is drawn, a mini-game of "Never Have I Ever" begins. "Never Have I Ever" requires all players to put up 3 fingers. For each turn in the game, players will say something that they have never done before (e.g. "Never have I ever travelled to Sweden"). Players who have done the said thing before (e.g. If they have travelled to Sweden / live in Sweden) will put a finger down. The first player(s) who put all their fingers down will have to drink their beverage.  
  
- **'Q': "Silent Queen - No one can talk to you until the next Queen. Rule-breakers drink!"**  
When any card with the value of Q is drawn, the person who drew the card can not be spoken to throughout the game until the next card with the value of Q is drawn. Anyone who speaks to the said player must drink their beverage.  
  
- **'K': "King's Cup! Pour a bit of your drink into the cup. The 4th King drinks it all!"**   
When any card with the value of K is drawn, the person who drew the card can pour something into a cup. When the 4th King (card with the value of K) is drawn, the game ends and the person who draws the 4th King must drink the entire cup regardless of what is inside the cup.  
  
- **'A': "Set a new rule that lasts the game! Be creative!"**  
When any card with the value of A is drawn, the person who drew the card can set a new rule that all players must adhere to until the next card with the value of A is drawn (e.g. All conversations must now be in Swiss-German). Anyone who breaks this rule must drink their beverage.  
  
    
### Disclaimer
*Do note that we do not promote irresponsible drinking and that our version of "King's Cup" does not revolve around the ingestion of alcoholic beverages. The game mainly revolves around the ingestion of a beverage, which can include non-alcoholic drinks, sauces/condiments (i.e. spicy Siracha sauces), and can even include non-liquids (where the person who draws the 4th King will still have to eat what is in the cup). If the player(s) chooses to consume alcohol during the game, it is at their own risk and choice.*

### How to Play 
To play the game, the user must first run the code in the terminal. Once done, they must select the tab that has the words "King's Cup" and click "Play" to begin the game. The game will automatically end when the tab is exited or when the 4th King has been drawn, and the user can choose to quit or play the game again.
   
## 2.2 Blackjack

### Game Description

Blackjack is a popular card game with the objective to reach a summed card value equal or as close as possible to 21 without exceeding it. The main rules are:

### Card Values
   - **Numbers from 2 to 10:** Their value is equal to their nominal value (i.e. 2 = 2).
   - **Face cards (J, Q, K):** Each has a value of 10.
   - **Aces (A):** Can have a value of either 1 or 11, depending on the player’s choice during the game.

### Game Flow
1. **Dealing cards:** The dealer gives two cards to each player and to themselves. Both of the dealer's cards will be visible.
   
2. **Choices of the players:**
   - The player's goal is to get as close to 21 as possible without exceeding it, as exceeding 21 (called "busting") results in an automatic loss.
   - It’s important to play around the dealer's hand and come up with a good strategy in order to win.
   - Then players can choose between the following actions:
     - **Hit:** Request an additional card.
     - **Stand:** Decline additional cards and keep their current hand value.

4. **Dealer’s turn:**
   - The dealer will draw cards until their hand reaches a minimum value of 17.
   - If the dealer's hand exceeds 21, they automatically lose, and all reamaining players win. 

5. **Win conditions:**
   - **Instant Blackjack:** If a player's initial two cards are an Ace paired with a face card or a 10 (called "Blackjack"), they win automatically, unless the dealer also has a Blackjack, in which case it is a tie.
   - **Higher Total than the Dealer:** Players win if their hand total is higher than the dealer's without exceeding 21.
   - **Bust:** If the dealer exceeds 21, all remaining players automatically win.



## 2.3 Trivia Quiz Game

### Game Description
This Game is an interactive general knowledge quiz where players answer ten questions in their chosen difficulty level. Each question offers four different answers to choose from. Each correct answer will count towards your final score with a highscore of 10. Let's see if you can reach it!

### Game Flow
1. **Choose a Difficulty:**
   - Players begin by selecting a difficulty level: Easy, Medium, or Hard.

2. **Answer Questions:**
   - Players answer ten randomized trivia questions, with shuffled answer options to ensure fairness.

3. **Score Evaluation:**
   - At the end of the game, players are scored based on the number of correct answers, and a performance message is provided.

4. **Replay Option:**
   - Players can choose to restart the quiz or exit after each game.

### Features
1. **Dynamic Questions**
   - Trivia questions are fetched from the Open Trivia Database (OpenTDB) API, ensuring variety with every new game.

2. **Error Handling**
   - Built-in validation for user input ensures smooth gameplay, even if invalid choices are entered.

3. **Shuffled Answer Options**
   - Answer options are randomized for each question to avoid any predictable patterns.

4. **Performance Feedback**
   - Players receive customized feedback based on their quiz results:


5. **Replayability**
   - Players can replay the game endlessly, with new questions fetched each time.

### How to Play
1. **Run the Script:**
   - Execute the Python script in your terminal or IDE

2. **Select Difficulty:**
   - Choose from Easy, Medium, or Hard difficulty levels.

3. **Answer Questions:**
   - Answer each question by typing the number corresponding to your selected choice.

4. **View Results:**
   - Your score will be displayed after all questions are answered.

5. **Replay or Exit:**
   - Choose whether to play again or exit the game.


# 3. Outlooks 

We based our project on some popular card games like Blackjack and King's Cup, known also for their entertainment value. Our focus was mainly on single-player mode, making them accessible and enjoyable even when playing alone. Even if the project could be finished, we would like to expand our collection of games while improving the code quality at the same time.




## New Games

1. **Implementing Multiplayer mode:**
   - Adding a multiplayer mode would allow players to challenge their friends online or via local network. This could include additional features to make the game more competitive and entertaining. 

2. **New Cards Games and Trivia:**
   - **Beginner's Poker:** A simplified version of Poker could be fun and easy to learn. This version could include simulated actions such as betting, checking, and raising (similar to a real Poker game).
     - *Disclaimer: Do note that we do not promote irresponsible playing. Our version of “Beginner’s Poker” would not involve real money or gambling. The game is intended to be played with the sole purpose of entertainment. If any player chooses to gamble with real money at any point of the game, it is at their own risk and discretion.*
   - **Memory card game:** A simple game that can be played solo or with friends, providing both entertainment and an opportunity to enhance memory skills.
   - **Expanded Trivia Games:** Introduce new genres to our trivia game to expand the set of playable topics and questions.


## Contribute to our page  
Our project framework is built to allow adding any number of new games to it. If you'd like to contribute a game to our platform, simply follow these steps:
1. Fork this repository
2. Clone the repository
   `git clone https://github.com/leomadori/GamesHub` 
4. Add your game to the folder "pages" 
5. Commit and push your changes to your forked repository.
6. Create a Pull Request to propose your changes to the main repositor




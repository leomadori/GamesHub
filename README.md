# Xcoding

possible table of content
# 1. program description (what is it about, goals)
# 2. features (describe how the works, don't explain the code here, do that on the actual code)
## 2.1 kingscup

### Game Description 
Kingscup is a card-based game where players take turns to draw cards and follow prompts. Each unique value of a card has a prompt associated to it, and the prompts remain the same regardless of the suit of the card (i.e., there are 13 different prompts * 4 different card suits). As the name suggests, the game revolves around the cards with the "King" value, with the game ending when the 4th King has been drawn.

### Card Values and Prompts 
In this version of the game, the card's values have the following associated prompts.   
  
**'2': "Pick someone to drink!"**  
When any card with the value of 2 is drawn, the person who draws it can nominate someone to drink their beverage.  
  
**'3': "You drink!"**  
When any card with the value of 3 is drawn, the person who draws it must drink their beverage.  
  
**'4': "All GUYS drink!"**  
When any card with the value of 4 is drawn, all male players will have to drink their beverage, regardless of whether they drew the card or not.  
  
**'5': "Play Five Ten!"**  
When any card with the value of 5 is drawn, a mini-game of "Five Ten" begins. "Five Ten" requires all players to put up a hand, and for each turn in the game, all players can choose to leave their hand open (indicating a value of 5) or closed in a fist (indicating a value of 0). Players will take turns guessing the sum of all players' hands and the first to do so correctly will force the rest of the players to drink their beverage.   
  
**'6': "All LADIES drink!"**  
When any card with the value of 6 is drawn, all female players will have to drink their beverage, regardless of whether they drew the card or not.  
  
**'7': "Last person to stand up drinks!"**  
When any card with the value of 7 is drawn, all players must stand up from their seats (or sit down if they are standing for some reason). The last person to do so must drink their beverage.  
  
**'8': "Pick someone to drink with you!"**  
When any card with the value of 8 is drawn, the person who draws it can pick another player to drink their beverage with whenever they are called upon to drink their beverage within the rules of the game.   
  
**'9': "Say a word, next person must rhyme. Loser drinks!"**  
When any card with the value of 9 is drawn, the player who draws it can choose a word. All players that follow must say words that rhyme with the chosen word, and this continues until one person fails to rhyme with the chosen word. The said person must drink their beverage.  
  
**'10': "Pick a category. Go around until someone can't answer. They drink!"**  
When any card with the value of 10 is drawn, the player who draws it can choose a category. All players that follow must name objects that fit into the category, and this continues until one person fails to do so. The said person must drink their beverage.  
  
**'J': "Never Have I Ever - Everyone puts up 3 fingers. First to drop all fingers drinks!"**  
When any card with the value of J is drawn, a mini-game of "Never Have I Ever" begins. "Never Have I Ever" requires all players to put up 3 fingers. For each turn in the game, players will say something that they have never done before (e.g. "Never have I ever travelled to Sweden"). Players who have done the said thing before (e.g. If they have travelled to Sweden / live in Sweden) will put a finger down. The first player(s) who put all their fingers down will have to drink their beverage.  
  
**'Q': "Silent Queen - No one can talk to you until the next Queen. Rule-breakers drink!"**  
When any card with the value of Q is drawn, the person who drew the card can not be spoken to throughout the game until the next card with the value of Q is drawn. Anyone who speaks to the said player must drink their beverage.  
  
**'K': "King's Cup! Pour a bit of your drink into the cup. The 4th King drinks it all!"**   
When any card with the value of K is drawn, the person who drew the card can pour something into a cup. When the 4th King (card with the value of K) is drawn, the game ends and the person who draws the 4th King must drink the entire cup regardless of what is inside the cup.  
  
**'A': "Set a new rule that lasts the game! Be creative!"**  
When any card with the value of A is drawn, the person who drew the card can set a new rule that all players must adhere to until the next card with the value of A is drawn (e.g. All conversations must now be in Swiss-German). Anyone who breaks this rule must drink their beverage.  
  
    
### Disclaimer
*Do note that we do not promote irresponsible drinking and that our version of "King's Cup" does not revolve around the ingestion of alcoholic beverages. The game mainly revolves around the ingestion of a beverage, which can include non-alcoholic drinks, sauces/condiments (i.e. spicy Siracha sauces), and can even include non-liquids (where the person who draws the 4th King will still have to eat what is in the cup). If the player(s) chooses to consume alcohol during the game, it is at their own risk and choice.*

### Operational Guide (tbc on the 17th/18th when we meet up)
To play the game, the user must first run the code in the terminal. Once done, they must select the tab that has the words "King's Cup" and click "Play" to begin the game. The game will automatically end when the tab is exited or when the 4th King has been drawn, and the user can choose to quit or play the game again.
   
## 2.2 blackjack

### Intro

Blackjack is a popular cards game with the objective to obtain a summed card value equal or as closest as possible to 21, without exceeding it. The main rules are:

### Cards value:
   - Number from 2 to 10: their value is equal to their nominal value (i.e. 2 = 2).
   - Figures (J,Q, K): each has a value of 10.
   - Asses (A): it can have a value of both 1 or 11 based on the player’s choice during the game.

### Game process:
1. Dealing cards: Dealer will give a pair of card to each player and to themselves, leaving one of them faced down.
2. Choices of the players:
   - The player has the target to get as closer as possible to 21 without exceeding this value, otherwise he/her will automatically lose         (known as “busting”).
   - It’s important to make guesses of the point that the dealer could have in their hands in order to follow a good strategy.
   - Then player can either:
     - Hit: player is asking for an additional card.
     - Stand: player will pass and he/she is fine with the amount of card they have.
4. Dealer’s turn:
   - They have to wait until all the players made their choices.
   - Dealer has to draw cards until they reach at least 17.
   - If they exceed 21, they will lose and all the other player that are still in the game will win. 
5. Win conditions:
   - Instant Blackjack: If the player obtains an Ace and a figure or a ten with the first two cards, he/she will win automatically unless        dealer doesn’t have a blackjack too, in that case it’ll be a tie.
   - Higher point than dealer’s: player will win.
   - Bust: if the dealer will hit cards and overtakes 21, he will lose automatically.



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
     - 10/10: “WOW HIGHSCORE! Congratulations!”
     - 8–9: “Great Job, you did really good!”
     - 4–7: “You're on a good path to become a Pro!”
     - 0–3: “Well... let's just say you might want to rethink your career as a trivia master.”

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

## 2.4 etc.
# 4. outloooks 
xd



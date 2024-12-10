import json
import requests
import html
import random
# Base API URL : database for trivia-questions
API_URL = "https://opentdb.com/api.php"

# Function to get questions in correct quantity and category
def fetch_questions(difficulty):
    params = {
        "amount": 10,   # Amount of fetched questions
        "category": 9,  # Category "General Knowledge"
        "difficulty": difficulty # Difficulty for Questions passed as argument)
    }
    # Make the GET request to the trivia API with the specified parameters
    response = requests.get(API_URL, params=params)
    # Parse the response JSON text into a Python dictionary
    data = json.loads(response.text)
    # Return the list of questions from the response data
    return data["results"]

# Quiz Logic
def start_quiz():
    # Welcome message and first user information
    print("Welcome to our Quiz Game! You will be presented with ten different questions. How many can you beat?")

    # Information for different difficulty levels
    print("Please Select a Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    # Loop to handle difficulty selection with error handling
    while True:
        try:
            # Prompt the user to enter a difficulty choice as a number
            difficulty_choice = int(input("Enter the number of your choice: "))

            # Check if the input is a valid option (1, 2 or 3)
            if difficulty_choice in [1, 2, 3]:
                # Map the numerical choice to the corresponding difficulty level
                difficulty = ["easy", "medium", "hard"][difficulty_choice - 1]
                break # Exit the loop after a valid choice
            else:
                # Notify the user if the input is outside the valid range
                print("Please choose a valid option (1, 2, or 3).")
        except ValueError:
            # Handle cases where the input is not an integer
            print("Invalid input. Only enter the number of your desired answer.")

    # Confirm the selected difficulty level and start the game
    print(f"You selected '{difficulty.title()}' difficulty. Let's begin, Good Luck!")
    print("") # Print a blank line for readability

    # Creating Storage for score counter
    correct_answers = 0

    # Fetch questions based on difficulty
    questions = fetch_questions(difficulty)
    # Loop through the list of questions with their index and content
    for idx, question in enumerate(questions):
        # Print the question number (1-based index) for better readability
        print(f"Question {idx + 1}:")
        #Print the actual question text after decoding any HTML entities (e.g., converting &amp; to &)
        print(html.unescape(question["question"]))

        # Combine incorrect answers with the correct answer and shuffle the options
        options = question["incorrect_answers"] + [question["correct_answer"]]
        #Decode HTML entities in the options for proper display
        options = [html.unescape(opt) for opt in options]
        # Shuffle the options randomly to avoid any pattern in the answers
        random.shuffle(options)

        # Display shuffled options to the user with numbered choices
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        # Get user input and error handling
        while True:
            try:
                # Get the user's answer choice as an integer
                user_answer = int(input("Enter the number of your answer: "))
                # Check if the selected answer is within the valid range of options
                if 1 <= user_answer <= len(options):
                    break  # Exit the loop if a valid choice is made
                else:
                    # Notify the user if the choice is out of range
                    print("Please select a valid option.")
            except ValueError:
                # Handle invalid input if the user enters something that is not an integer
                print("Invalid input. Only enter the number of your desired answer.")

        # Check if the user's answer matches the correct answer
        if options[user_answer - 1] == html.unescape(question["correct_answer"]):
            # If the answer is correct, congratulate the user and increase score
            print("Correct!")
            correct_answers += 1  # Add 1 to the score count
            print("")  # Print a blank line for readability
        else:
            # If the answer is incorrect, display the correct answer to the user
            print(f"Incorrect. The correct answer was '{html.unescape(question['correct_answer'])}'")
            print("")  # Print a blank line for readability

    # Final feedback based on the user's performance
    print(f"You got {correct_answers} out of {len(questions)} questions correct.")
    # Custom feedback based on final score
    if correct_answers == 10:
        print("WOW HIGHSCORE! Congratulations!")  # Perfect score
    elif correct_answers >= 8:
        print("Great Job, you did really good!")  # High score
    elif correct_answers >= 4:
        print("You're on a good path to become a Pro!")  # Moderate score
    else:
        print("Well... let's just say you might want to rethink your career as a trivia master.")  # Low score

# Function to prompt the user to restart the quiz
def ask_restart():
    while True:
        # Ask the user if they want to play again and clean the input (strip whitespace, convert to lowercase)
        restart_choice = input("Do you want to play again? (type yes/no): ").strip().lower()

        # If the user enters "yes", restart the quiz
        if restart_choice == "yes":
            print("")  # Print a blank line for readability
            start_quiz()  # Call the function to start the quiz again
        # If the user enters "no", thank them and exit the loop
        elif restart_choice == "no":
            print("Thanks for playing! Have a great day!")  # Display a thank-you message
            break  # Exit the loop, ending the function and the program
        # If the user enters anything other than "yes" or "no", ask them to enter a valid input
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Start the quiz when the program is run
start_quiz()

# After the quiz ends, ask if the user wants to restart
ask_restart()
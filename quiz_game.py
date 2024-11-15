import json
import requests
import html
import random

# Base API URL
API_URL = "https://opentdb.com/api.php"

# Function to get questions
def fetch_questions(difficulty):
    params = {
        "amount": 10,
        "category": 9,  # General Knowledge
        "difficulty": difficulty
    }
    response = requests.get(API_URL, params=params)
    data = json.loads(response.text)
    return data["results"]

# Quiz Logic
def start_quiz():
    print("Welcome to our Quiz Game! You will be presented with ten different questions. How many can you beat?")

    # Difficulty selection with error handling
    print("Please Select a Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        try:
            difficulty_choice = int(input("Enter the number of your choice: "))
            if difficulty_choice in [1, 2, 3]:
                difficulty = ["easy", "medium", "hard"][difficulty_choice - 1]
                break
            else:
                print("Please choose a valid option (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Only enter the number of your desired answer.")

    print(f"You selected '{difficulty.title()}' difficulty. Let's begin, Good Luck!")
    print("")

    # Storage for score counter
    correct_answers = 0

    # Fetch questions based on difficulty
    questions = fetch_questions(difficulty)

    for idx, question in enumerate(questions):
        print(f"Question {idx + 1}:")
        print(html.unescape(question["question"]))

        # Combine answers and shuffle
        options = question["incorrect_answers"] + [question["correct_answer"]]
        options = [html.unescape(opt) for opt in options]
        random.shuffle(options)

        # Display options
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        # Get user input and error handling
        while True:
            try:
                user_answer = int(input("Enter the number of your answer: "))
                if 1 <= user_answer <= len(options):
                    break
                else:
                    print("Please select a valid option.")
            except ValueError:
                print("Invalid input. Only enter the number of your desired answer.")

        # Check answer
        if options[user_answer - 1] == html.unescape(question["correct_answer"]):
            print("Correct!")
            correct_answers += 1
            print("")
        else:
            print(f"Incorrect. The correct answer was '{html.unescape(question['correct_answer'])}'")
            print("")

    # Final feedback and personalized messages for different scores
    print(f"You got {correct_answers} out of {len(questions)} questions correct.")
    if correct_answers == 10:
        print("WOW HIGHSCORE! Congratulations!")
    elif correct_answers >= 8:
        print("Great Job, you did really good!")
    elif correct_answers >= 4:
        print("You're on a good path to become a Pro!")
    else:
        print("Well... let's just say you might want to rethink your career as a trivia master.")

# Creating Function to restart the quiz quickly
def ask_restart():
    while True:
        restart_choice = input("Do you want to play again? (type yes/no): ").strip().lower()
        if restart_choice == "yes":
            print("")
            start_quiz()
        elif restart_choice == "no":
            print("Thanks for playing! Have a great day!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Start the quiz
start_quiz()

# Ask if the user wants to restart
ask_restart()
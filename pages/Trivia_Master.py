import json
import requests
import html
import random
import streamlit as st

###############################################################################################
                            # # # Quiz Game # # #
# The following is a script for a Trivia Game that uses the Open Database Trivia API to fetch questions.
# Firstly, the user can select the difficulty of the game.
# After choosing the difficulty, the user starts with the questions.
# All questions are single-choice.
###############################################################################################

# Base API URL: database for trivia questions
API_URL = "https://opentdb.com/api.php"

###############################################################################################

# # # Function Section

###############################################################################################

# Function to get questions in correct quantity and category
def fetch_questions(difficulty):
    params = {
        "amount": 10,  # Amount of fetched questions
        "category": 9,  # Category "General Knowledge"
        "difficulty": difficulty,  # Difficulty for Questions passed as argument
    }
    # Make the GET request to the trivia API with the specified parameters
    response = requests.get(API_URL, params=params)
    # Parse the response JSON text into a Python dictionary
    data = json.loads(response.text)
    # Return the list of questions from the response data
    return data["results"]

def trivia_app():
    st.title("Trivia Master")

    st.image("Images/Trivia_game.webp")

    # Difficulty selection
    st.write("Welcome to Trivia Master! Select a difficulty level to begin.")
    difficulty = st.selectbox("Choose Difficulty:", ["Easy", "Medium", "Hard"], index=0)
    start_game = st.button("Start Game")

    if start_game:
        # Begin game
        st.session_state["difficulty"] = difficulty.lower()                 #save the selected dificulty level in sessions tate as lowercase
        st.session_state["questions"] = fetch_questions(difficulty.lower()) #Fetch trivia questions form the API based on the selected difficulty and save them in session state
        st.session_state["current_question"] = 0                            # initialize the index for the current question to 0 (first question)
        st.session_state["score"] = 0                                       #initialize user's score to 0
        st.session_state["game_started"] = True                             # mark the game as started by setting this flag to TRUE
        st.session_state["shuffled_options"] = None                         #initialize placeholder for shuffled options for the current qeustions. this will be set later

    if st.session_state.get("game_started", False):                         #check if the game has been started (this is the case if the flag is set to TRUE in sessions state)
        current_question_index = st.session_state["current_question"]       #retrieve the current question index form sessions state
        questions = st.session_state["questions"]                           #retrieve the list of questions fetched from the API

        if current_question_index < len(questions):                         #check if there are still unanswered question (this happens when the curernt index is less than the total number of questions)
            question = questions[current_question_index]                    #retrieve the current question from the questions list based on the current index
            st.subheader(f"Question {current_question_index + 1}:")         #display the current question number as a subheader
            st.write(html.unescape(question["question"]))                   #display the question text, decoding any HTML for proper formatting

            # Options
            if st.session_state["shuffled_options"] is None:          #check if options fot the current question have NOT been shuffled yet

                #combined correct and incorrect answers into one list, decoding HTML 
                st.session_state["shuffled_options"] = [
                    html.unescape(opt) for opt in question["incorrect_answers"] + [question["correct_answer"]]
                ]
                random.shuffle(st.session_state["shuffled_options"])            #suffle the optins randomly and store them in sessions state

            options = ["Select an answer"] + st.session_state["shuffled_options"]   #adds a placeholder  "select answer" to the beginning of the shuffled option list
            selected_option = st.radio("Choose your answer:", options, index=0)     #display the options as radio button, starting with the placeholder as the default selection
            submit_answer = st.button("Submit Answer")                              #add a "submit answer" button for the user to submit their selection

            #if user clicks on "Submit answer"
            if submit_answer:                               
                if selected_option == "Select an answer":           #this checks if the user has selected a valid option, "select answer" is just a placeholder            
                    st.warning("Please select an answer before submitting.")    #warning to select an option
                else:
                    correct_answer = html.unescape(question["correct_answer"])  #retrieve and decode the correct answer for comparison.
                    if selected_option == correct_answer:                       #checks if selected answer matches the actual correct answer
                        st.success("Correct!")                                  #success message if there is a match
                        st.session_state["score"] += 1                          #increment score count in session state
                    else:
                        st.error(f"Incorrect. The correct answer was: {correct_answer}")        #message if answer is incorrect

                    # Move to next question
                    st.session_state["current_question"] += 1    #increment current question index to move ot the next question
                    st.session_state["shuffled_options"] = None  # Reset shuffled options for the next question
        else:
            st.success(f"Game Over! You scored {st.session_state["score"]} out of {len(questions)}.") #if there are no more questions, display a message showing user's final score

            #Feedbacks based on user's score
            if st.session_state["score"] == 10: 
                    st.write("AMAZING! you are a Trivia Master indeed!")
                    st.write("Try to increase the difficulty")
            elif 8 <= st.session_state["score"] < 10:
                    st.write("Nicely Done! You are on you way to become a Trivia Master!")
            elif 4 <= st.session_state["score"] < 8: 
                    st.write("Good Job! Keep up the good work")

            elif st.session_state["score"] < 4:
                    st.write("Well… I'd suggest you pick up a book …or two")
                    st.write("Try to decrease the difficulty")


# Run the trivia app
trivia_app()

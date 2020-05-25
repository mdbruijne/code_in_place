# Libraries used to run programs
from simpleimage import SimpleImage
import tkinter
from PIL import ImageTk
import time
import random

# Constants used in the programs
CANVAS_HEIGHT = 800
CANVAS_WIDTH = 1000
DELAY = 1 / 10
FONT_TYPE = 'courier'
GOODBYE = 'images/goodbye.png'
INCORRECT_ANSWER_MAX = 3
KAREL = 'images/karel.png'
LETTERS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seventh', 8: 'eight', 9: 'nine',
           10: 'ten', 11: 'elevn', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen'}
LETTERS_TH = {2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh',
              8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth'}
LETTER_GUESS_FILE = 'textfiles/random_word_guess.txt'
MATH_ANS_FILE = 'textfiles/math_word_games_answers.txt'
MATH_QUES_FILE = 'textfiles/math_word_games_questions.txt'
MAX_ASKED_QUESTIONS = 5
MAX_LETTER_GUESS = 10
NORTHERN_LIGHTS = 'images/northern_lights.png'
PARTY_LEFT = 'images/party_left.png'
PARTY_RIGHT = 'images/party_right.png'
SUFFICIENT_WHITE = 3 * 245
REMINDER_MSG = ['HI THERE!!', 'REMEMBER TO CLOSE', 'THIS WINDOW']
WELCOME_IMAGE = 'images/welcome_sign.png'
WELCOME_MSG = ['WELCOME TO MY CODE IN PLACE 2020',
               'FINAL PROJECT!!!!',
               'I AM SO EXCITED TO TAKE YOU',
               'ON THIS AWESOME JOURNEY!',
               'I HOPE YOU WILL ENJOY EVERY',
               'SECOND OF IT!',
               'PLEASE CLOSE THIS WINDOW AND NAVIGATE TO THE PYTHON TERMINAL']
WORDS_ANS_FILE = 'textfiles/word_definition_answers.txt'
WORD_QUES_FILE = 'textfiles/word_definition_questions.txt'


def main():
    close_welcome_screen_msg()
    welcome_screen()
    game_terminal_welcome_msg()
    user_input = user_chooses_game_option(1, 2)
    while user_input != "exit":
        if user_input == 1:
            math_game_simulator()
        else:
            word_game_simulator()
        retry_another_problem()
        user_input = user_chooses_game_option(1, 2)
    print_goodbye_terminal()
    goodbye_screen()


# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---
# -------------------------------
# SET-UP GOODBYE CONSOLE SCREEN
# -------------------------------
def print_goodbye_terminal():
    """
    Print goodbye message to terminal
    """
    print("")
    print("-----------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------")
    print("Thanks for visiting! Goodbye!!!")
    print("-----------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------")


def goodbye_screen():
    """
    Creates the goodbye screen of my final Code in Place project
    """
    # Read in karel image
    karel_image = SimpleImage(KAREL)
    karel_height = karel_image.height
    karel_width = karel_image.width
    nr_karel_y = 8
    nr_karel_x = 10
    # Create Canvas
    canvas_width = nr_karel_x * karel_width
    canvas_height = nr_karel_y * karel_height
    canvas = make_canvas(canvas_width, canvas_height, 'Goodbye! Hope you enjoyed my final project')
    canvas.update()
    # Create rectangle
    canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill='white', outline='white')
    # Place Karel on bottom
    pil_karel_image = ImageTk.PhotoImage(karel_image.pil_image)
    karel = canvas.create_image(0, nr_karel_y * karel_height, anchor='sw', image=pil_karel_image)
    canvas.update()
    # Move Karel vertically up
    colour = karel_vertically_up(nr_karel_y, karel_height, karel_width, karel, canvas)
    # Move Karel horizontally right
    colour = karel_horizontally_right(nr_karel_x, karel_height, karel_width, karel, canvas, colour)
    # Move Karel vertically down
    colour = karel_vertically_down(nr_karel_y, karel_height, karel_width, karel, canvas, canvas_width, colour)
    # Move Karel horizontally left
    karel_horizontally_left(nr_karel_x, karel_height, karel_width, karel, canvas, canvas_height, colour)
    # Read in goodbye image
    goodbye_image = SimpleImage(GOODBYE)
    pil_goodbye_image = ImageTk.PhotoImage(goodbye_image.pil_image)
    canvas.create_image(canvas_width/2, canvas_height/2, image=pil_goodbye_image)
    canvas.update()
    canvas.mainloop()


def karel_vertically_up(nr_karel_y, karel_height, karel_width, karel, canvas):
    """
    Karel moves vertically up
    """
    for i in range(nr_karel_y - 1):
        time.sleep(DELAY)
        canvas.move(karel, 0, -karel_height)
        if i % 2 == 0:
            colour = 'blue'
        else:
            colour = 'red'
        y1 = (nr_karel_y - (i - 1)) * karel_height
        y2 = (nr_karel_y - i) * karel_height
        canvas.create_rectangle(0, y1, karel_width, y2, fill=colour)
        canvas.update()
    if colour == 'red':
        colour = 'blue'
    else:
        colour = 'red'
    canvas.create_rectangle(0, y1 - karel_height, karel_width, y2 - karel_height, fill=colour)
    canvas.update()
    return colour


def karel_horizontally_right(nr_karel_x, karel_height, karel_width, karel, canvas, colour):
    """
    Karel moves horizontally right
    """
    for i in range(nr_karel_x - 1):
        time.sleep(DELAY)
        canvas.move(karel, karel_width, 0)
        canvas.update()
        if colour == 'red':
            colour = 'blue'
        else:
            colour = 'red'
        x1 = i * karel_width
        x2 = (i + 1) * karel_width
        canvas.create_rectangle(x1, 0, x2, karel_height, fill=colour)
        canvas.update()
    return colour


def karel_vertically_down(nr_karel_y, karel_height, karel_width, karel, canvas, canvas_width, colour):
    """
    Karel moves vertically down
    """
    for i in range(nr_karel_y - 1):
        time.sleep(DELAY)
        canvas.move(karel, 0, karel_height)
        if colour == 'red':
            colour = 'blue'
        else:
            colour = 'red'
        y1 = i * karel_height
        y2 = (i + 1) * karel_height
        canvas.create_rectangle(canvas_width - karel_width, y1, canvas_width, y2, fill=colour)
        canvas.update()
    return colour


def karel_horizontally_left(nr_karel_x, karel_height, karel_width, karel, canvas, canvas_height, colour):
    """
    Karel moves horizontally left
    """
    for i in range(nr_karel_x - 1):
        time.sleep(DELAY)
        canvas.move(karel, -karel_width, 0)
        canvas.update()
        if colour == 'red':
            colour = 'blue'
        else:
            colour = 'red'
        x1 = (nr_karel_x - i) * karel_width
        x2 = (nr_karel_x - (i + 1)) * karel_width
        canvas.create_rectangle(x1, canvas_height - karel_height, x2, canvas_height, fill=colour)
        canvas.update()


# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---
# -------------------------------
# SET-UP WORD GAME STIMULATOR
# -------------------------------
def word_game_simulator():
    """
    The user has chosen to do the word games and this function contains all functions related to the word games
    """
    word_game_choices()
    user_input = user_chooses_game_option(1, 2)
    # Tell the user to get ready for the first question
    print("-----------------------------------------------------------------------------------------------------")
    print("Are you ready for some ", end="")
    if user_input == 1:
        print("letter guessing? :> :D :> ")
        print("First, some rules to explain:")
        print("You will need to guess the letters of {} words correctly to win this game"
              .format(LETTERS.get(MAX_ASKED_QUESTIONS)))
        print("You have a total of {} lives available".format(LETTERS.get(INCORRECT_ANSWER_MAX)))
        print("You will loose a life, if you made {} wrong guesses per word".format(LETTERS.get(MAX_LETTER_GUESS)))
        print("")
        print("Ready, set, go! Here is your first word:")
        guess_the_letter()
    else:
        print("word guessing? :> :D :> ")
        print("First, some rules to explain:")
        print("You will need to guess the {} words correctly to win this game"
              .format(LETTERS.get(MAX_ASKED_QUESTIONS)))
        print("You have a total of {} lives available".format(LETTERS.get(INCORRECT_ANSWER_MAX)))
        print("You will be given a definition and you need to guess the word. Please make sure your spelling is correct"
              "and ensure that is in lower case")
        print("")
        print("Ready, set, go! Here is your first definition:")
        guess_the_word()
    print("-----------------------------------------------------------------------------------------------------")


# ---
def guess_the_word():
    """
    Guess the word. The user will be given a definition and they need to guess the word
    """
    # Initial values and dictionaries
    incorrect_answers = 0
    questions_asked = 0
    definition_nr = 1
    # Get the words and definitions
    questions = open_load_files_into_dict(WORD_QUES_FILE, 0)
    answers = open_load_files_into_dict(WORDS_ANS_FILE, 0)
    # Create tracker for questions asked, to ensure question only asked once
    tracker = create_question_tracker(questions.keys())
    while questions_asked < MAX_ASKED_QUESTIONS and incorrect_answers < INCORRECT_ANSWER_MAX:
        if definition_nr > 1:
            print("")
            print("Here is your {} definition: (remember to check your spelling and give the answer in lower case)"
                  .format(LETTERS_TH.get(definition_nr)))
        outcome = user_guess_word(questions, tracker, answers)
        if outcome:
            questions_asked += 1
        else:
            incorrect_answers = user_live_left(incorrect_answers)
        definition_nr += 1
    # Tell the user if they failed or succeed
    fail_or_succeed_game(incorrect_answers, "word guessing", "wordsmith")


def user_guess_word(questions, tracker, answers):
    """
    The user gets the definition and gets asked for an answer
    """
    question = get_question_for_user(questions, tracker)
    print(questions.get(question))
    user_answer = input("What is your answer? ")
    ans = answers.get(question)
    if user_answer == ans:
        print("Well done that is the correct answer!")
    else:
        print("That is the incorrect answer! The correct answer is", ans)

    return user_answer == ans


# --- GUESS THE LETTER
def guess_the_letter():
    """
    Guess the letter. The user will be given a word, but will only know the length and they need to guess the letter
    """
    # Initial values and dictionaries
    incorrect_answers = 0
    questions_asked = 0
    word_nr = 1
    # Get words list and create tracker dictionary
    words = open_load_files_into_list(LETTER_GUESS_FILE)
    tracker = create_question_tracker(words)
    # The first word for user to guess
    question = get_question_for_user(words, tracker)
    passed = user_guess_letters_of_word(question)
    word_nr += 1
    if passed == 0:
        incorrect_answers = user_live_left(incorrect_answers)
    else:
        questions_asked += 1
    print("-------------------------")
    while questions_asked < MAX_ASKED_QUESTIONS and incorrect_answers < INCORRECT_ANSWER_MAX:
        print("")
        print("Here is your {} word: ".format(LETTERS_TH.get(word_nr)))
        question = get_question_for_user(words, tracker)
        passed = user_guess_letters_of_word(question)
        word_nr += 1
        if passed == 0:
            incorrect_answers = user_live_left(incorrect_answers)
        else:
            questions_asked += 1
        print("-------------------------")
    # Tell the user if they failed or succeed
    fail_or_succeed_game(incorrect_answers, "letter guessing", "wordsmith")


def user_guess_letters_of_word(word):
    """
    User to guess the letters, they get a total of seven total allowed mistakes
    word: the word whose letters needs to be guessed
    """
    incorrect = 0
    finish = 0
    guess_list = setup_guess_word(word)
    guessed_letters = []
    while incorrect < MAX_LETTER_GUESS and finish == 0:
        print("You have {} guesses left. ".format(MAX_LETTER_GUESS - incorrect), end="")
        correct = user_guess_letter(guess_list, word, guessed_letters)
        finish = check_guess_status(guess_list)
        # Increment incorrect counter if wrong guess has been made
        if not correct:
            incorrect += 1
        # Print either next letter to guess or end of guessing
        print("")
        if incorrect == MAX_LETTER_GUESS:
            print("Sorry you have no more tries left and you failed :< The word was:", word)
        elif finish == 0:
            print_guess_word(guess_list)
            print("Letters guessed so far:", guessed_letters)
        else:
            print("Well done! You have guessed the letters an your word is: {} :>".format(word))

    return finish


def check_guess_status(guess_list):
    """
    Check to see if the entire word has been guessed or not
    """
    guessed = 0
    len_guess = len(guess_list)
    for item in guess_list:
        if item != '_':
            guessed += 1
    if guessed == len_guess:
        return 1
    else:
        return 0


def print_guess_word(guess_list):
    """
    Print the updated guessed for with latest correct guesses where applicable
    """
    print("Here is your word again: ", end="")
    for item in guess_list:
        print(item, " ", end="")
    print("")


def user_guess_letter(guess_list, word, guessed_letters):
    """
    The user gets the change to guess a letter
    guess_list: the list that saves the letters correctly guessed by user
    word: the word that needs to be guessed
    """
    correct = 0
    guess = input("Please guess a letter: ")
    guessed_letters.append(guess)
    for i in range(len(word)):
        letter = word[i]
        if letter == guess:
            guess_list[i] = guess
            correct += 1
    if correct == 0:
        print("Wrong guess! The letter {} is not in this word".format(guess))
        return False
    else:
        print("Good guessing! The letter {} has been added".format(guess))
        return True


def setup_guess_word(word):
    """
    The word is being set-up and ready for the user to guess
    word: the word whose letters needs to be guessed
    """
    guess_list = []
    word_length = len(word)
    print("This word consists out of {} letters: ".format(word_length), end="")
    for i in range(word_length):
        guess_list.append("_")
        print(" _ ", end="")
    print("")
    return guess_list


def open_load_files_into_list(file_name):
    """
    Open and load the files and create a list
    file_name: is the file that needs to be open an read into a list
    """
    list_new = []
    with open(file_name) as file:
        for line in file:
            word = line.strip()
            list_new.append(word)
    return list_new


# --- SET-UP WORD GAME CHOICES AVAILABLE FOR USERS TO CHOOSE FROM
def word_game_choices():
    """
    Explanation of word games available
    """
    print("-----------------------------------------------------------------------------------------------------")
    print("You chose to attempt a word game, so let's test your word skills!")
    print("-----------------------------------------------------------------------------------------------------")
    print("With the word games, we have created two games to test your skills.")
    print("In order to win a game you need to play at least {} rounds successfully."
          .format(LETTERS.get(MAX_ASKED_QUESTIONS)))
    print("But don't fear you have {live} lives, so you can make fail at most {live} rounds before you loose."
          .format(live=LETTERS.get(INCORRECT_ANSWER_MAX)))
    print("You have a choice between the following two word games (explanation below):")
    print("Option 1 - Guess the letter")
    print("Option 2 - Guess the word")
    print("-----------------------------------------------------------------------------------------------------")
    print("Guess the letter -> it is like hangman, you will know how many letters to guess to make up a word")
    print("Guess the word -> you will be given a definition and need to guess the word")
    print("-----------------------------------------------------------------------------------------------------")
    print("GOOD LUCK WORDSMITH")
    print("Words have energy and power with the ability to help, to heal, to hinder, to hurt, to harm, to ")
    print("humiliate, and to humble")
    print("-----------------------------------------------------------------------------------------------------")


# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---
# -------------------------------
# SET-UP MATH GAME STIMULATOR
# -------------------------------
def math_game_simulator():
    """
    The user has chosen to do the math games and this function contains all functions related to the math games
    """
    math_games_choices()
    user_input = user_chooses_game_option(1, 4)
    # Tell the user to get ready for the first question
    print("-----------------------------------------------------------------------------------------------------")
    print("Are you ready for some ", end="")
    if user_input == 1:
        print("addition & subtraction? :> :D :> ")
        print("")
        print("Ready, set, go! Here is your first question:")
        basic_add_sub()
    elif user_input == 2:
        print("multiplication & division?")
        print("")
        print("Ready, set, go! Here is your first question: :> :D :> ")
        basic_multi_div()
    elif user_input == 3:
        print("addition & subtraction AND multiplication & division? :> :D :> ")
        print("")
        print("Ready, set, go! Here is your first question:")
        all_four()
    else:
        print("word games to test your analytical skills? :> :D :> ")
        print("")
        print("Ready, set, go! Here is your first question:")
        math_word_game()
    print("-----------------------------------------------------------------------------------------------------")


# --- MATH WORD GAME
def math_word_game():
    """
    This reads in a file with the word games and the relevant answer and then randomly prints one of the questions
    to the user. This repeats until all five questions have been answered correctly or the user lost all lives
    """
    # Initial values and dictionaries
    incorrect_answers = 0
    questions_asked = 0
    # Read in answers and questions for the user
    answers = open_load_files_into_dict(MATH_ANS_FILE, 1)
    questions = open_load_files_into_dict(MATH_QUES_FILE, 0)
    # Create tracker for questions asked, to ensure question only asked once
    tracker = create_question_tracker(questions.keys())
    # Get question to ask user
    while questions_asked < MAX_ASKED_QUESTIONS and incorrect_answers < INCORRECT_ANSWER_MAX:
        question = get_question_for_user(questions, tracker)
        correct = ask_user_math_problem(question, answers, questions)
        if correct:
            questions_asked += 1
        else:
            incorrect_answers = adjust_incorrect_answers(answers.get(question), incorrect_answers)
        # Prepare user for next question
        if questions_asked < MAX_ASKED_QUESTIONS:
            print_ready_for_next_question(questions_asked, incorrect_answers)
    # Tell the user if they failed or succeed
    fail_or_succeed_game(incorrect_answers, "word problems", "math magician")


def ask_user_math_problem(question, answers, questions):
    """
    The user gets asked question that they will need to answer
    question: the question number to be asked
    answers: the dictionary with all the answers
    questions: the dictionary with all the questions
    """
    print(questions.get(question))
    user_answer = input("Please enter your answer: ")
    user_answer = check_valid_input(user_answer)
    ans = answers.get(question)
    if ans == user_answer:
        print("Well done! That answer is correct!")
    return ans == user_answer


# --- ALL FOUR OPERATORS: ADDITION, SUBTRACTION, MULTIPLICATION AND DIVISION
def all_four():
    """
    This game is played if the user chooses multiplication and division. This repeats until all five questions have
    been answered correctly or the user lost all lives
    """
    # Initial values
    incorrect_answers = 0
    questions_asked = 0
    while questions_asked < MAX_ASKED_QUESTIONS and incorrect_answers < INCORRECT_ANSWER_MAX:
        # Determine what difficulty level question to ask
        hard_level = random.randint(1, 4)
        # Call relevant function based on difficulty level
        if hard_level == 4:
            ans = all_four_hard_question(incorrect_answers)
        elif hard_level == 3:
            ans = all_four_medium_question(incorrect_answers)
        else:
            ans = all_four_low_question(incorrect_answers)
        # Check if the answer is correct to iterate the correct variable
        if ans:
            questions_asked += 1
        else:
            incorrect_answers += 1
        # Prepare user for next question
        if questions_asked < MAX_ASKED_QUESTIONS:
            print_ready_for_next_question(questions_asked, incorrect_answers)
    # Tell the user if they failed or succeed
    fail_or_succeed_game(incorrect_answers, "additions, subtractions, multiplication & division", "math magician")


def all_four_hard_question(incorrect_answers):
    """
    User gets asked the most difficult level question for the combination including all four operators question
    """
    begin_incorrect = incorrect_answers
    # Generate numbers and answer for subtraction
    num1 = random.randint(1, 600)
    num2 = random.randint(1, 400)
    num3 = random.randint(2, 100)
    num4 = random.randint(49, 300)
    num5 = random.randint(51, 100)
    num6 = random.randint(1, 50)
    ans1 = (num1 + num2) / num3
    ans2 = num4 / (num5 - num6)
    # Ensure that answer 1 is an integer
    while int(ans1) != ans1:
        num1 = random.randint(1, 600)
        num2 = random.randint(1, 400)
        num3 = random.randint(2, 100)
        ans1 = (num1 + num2) / num3
    # Ensure that answer 2 is an integer
    while int(ans2) != ans2:
        num4 = random.randint(49, 300)
        num5 = random.randint(51, 100)
        num6 = random.randint(1, 50)
        ans2 = num4 / (num5 - num6)
    ans = ans1 * ans2
    # Ask user for answer
    answer_from_user = input(
        "What is ({0} + {1}) / {2} * {3} / ({4} - {5})? ".format(num1, num2, num3, num4, num5, num6))
    user_answer = check_valid_input(answer_from_user)
    # Check answer and do actions accordingly
    if ans != user_answer and incorrect_answers < INCORRECT_ANSWER_MAX:
        incorrect_answers = adjust_incorrect_answers(ans, incorrect_answers)
    elif ans == user_answer:
        print("Well done! That answer is correct!")

    return begin_incorrect == incorrect_answers


def all_four_medium_question(incorrect_answers):
    """
    User gets asked a medium level question for the combination including all four operators question
    """
    begin_incorrect = incorrect_answers
    # Generate numbers and answer for subtraction
    num1 = random.randint(1, 999)
    num2 = random.randint(2, 998)
    num3 = random.randint(2, 450)
    num4 = random.randint(50, 300)
    num5 = random.randint(1, 49)
    num6 = random.randint(2, 151)
    # Ensure that division answer is an integer
    while int(num1 / num2) != num1 / num2 or num1 == num2:
        num1 = random.randint(1, 999)
        num2 = random.randint(2, 998)
    ans = num1 / num2 + num3 - (num4 - num5) * num6
    # Ask user for answer
    answer_from_user = input("What is {0} / {1} + {2} - ({3} - {4}) * {5}? ".format(num1, num2, num3, num4, num5, num6))
    user_answer = check_valid_input(answer_from_user)
    # Check answer and do actions accordingly
    if ans != user_answer and incorrect_answers < INCORRECT_ANSWER_MAX:
        incorrect_answers = adjust_incorrect_answers(ans, incorrect_answers)
    elif ans == user_answer:
        print("Well done! That answer is correct!")

    return begin_incorrect == incorrect_answers


def all_four_low_question(incorrect_answers):
    """
    User gets asked a low level question for the combination including all four operators question
    """
    begin_incorrect = incorrect_answers
    option = random.randint(1, 3)
    # Generate numbers and answer for subtraction
    num1 = random.randint(1, 999)
    num2 = random.randint(2, 998)
    num3 = random.randint(2, 450)
    num4 = random.randint(50, 300)
    num5 = random.randint(1, 49)
    num6 = random.randint(2, 151)
    # Ensure that division answer is an integer
    while int(num1 / num2) != num1 / num2 or num1 == num2:
        num1 = random.randint(1, 999)
        num2 = random.randint(2, 998)
    # Ensure that number 4 is not 0.98 greater than number 3 for subtraction part of equation
    while num4 / num3 > 0.98:
        num3 = random.randint(2, 450)
        num4 = random.randint(50, 300)
    # Get an equation for the user to determine
    if option == 1:
        ans = num1 / num2 + num5 * num6
        # Ask user for answer
        answer_from_user = input("What is {0} / {1} + {2} * {3}? ".format(num1, num2, num5, num6))
    elif option == 2:
        ans = (num1 + num2) * (num3 - num4)
        # Ask user for answer
        answer_from_user = input("What is ({0} + {1}) * ({2} - {3})? ".format(num1, num2, num3, num4))
    else:
        ans = num3 - num4 + num1 / num2
        # Ask user for answer
        answer_from_user = input("What is {0} - {1} + {2} / {3}? ".format(num3, num4, num1, num2))
    user_answer = check_valid_input(answer_from_user)
    # Check answer and do actions accordingly
    if ans != user_answer and incorrect_answers < INCORRECT_ANSWER_MAX:
        incorrect_answers = adjust_incorrect_answers(ans, incorrect_answers)
    elif ans == user_answer:
        print("Well done! That answer is correct!")

    return begin_incorrect == incorrect_answers


# --- MULTIPLICATION AND DIVISION
def basic_multi_div():
    """
    This game is played if the user chooses multiplication and division. This repeats until all five questions have
    been answered correctly or the user lost all lives
    """
    # Initial values
    incorrect_answers = 0
    questions_asked = 0
    while questions_asked < MAX_ASKED_QUESTIONS and incorrect_answers < INCORRECT_ANSWER_MAX:
        # First two questions are addition
        if questions_asked < 2:
            ans = multiplication_questions(incorrect_answers)
        # Next two questions are division
        elif questions_asked < 4:
            ans = division_questions(incorrect_answers)
        # Next question is combination
        else:
            ans = multi_div_question(incorrect_answers)
        # Check if the answer is correct to iterate the correct variable
        if ans:
            questions_asked += 1
        else:
            incorrect_answers += 1
        # Prepare user for next question
        if questions_asked < MAX_ASKED_QUESTIONS:
            print_ready_for_next_question(questions_asked, incorrect_answers)
    # Tell the user if they failed or succeed
    fail_or_succeed_game(incorrect_answers, "multiplication & division", "math magician")


def multi_div_question(incorrect_answers):
    """
    User gets asked a combination of multiplication and division question
    """
    begin_incorrect = incorrect_answers
    # Generate numbers and answer for subtraction
    num1 = random.randint(10, 400)
    num2 = random.randint(2, 299)
    num3 = random.randint(1, 99)
    # Ensure that ans only have one decimal place
    while int(num1 / num2) != (num1 / num2) or num1 == num2:
        num1 = random.randint(10, 499)
        num2 = random.randint(2, 299)
    ans = num1 / num2 * num3
    # Ask user for answer
    answer_from_user = input("What is " + str(num1) + " / " + str(num2) + " * " + str(num3) + "? ")
    user_answer = check_valid_input(answer_from_user)
    # Check answer and do actions accordingly
    if ans != user_answer and incorrect_answers < INCORRECT_ANSWER_MAX:
        incorrect_answers = adjust_incorrect_answers(ans, incorrect_answers)
    elif ans == user_answer:
        print("Well done. You have answered the last question correctly!")

    return begin_incorrect == incorrect_answers


def division_questions(incorrect_answers):
    """
    User gets asked subtraction questions
    """
    begin_incorrect = incorrect_answers
    # Generate numbers and answer for subtraction
    num1 = random.randint(10, 999)
    num2 = random.randint(2, 650)
    ans = num1 / num2
    # Ensure that ans only have one decimal place
    while int(ans) != ans or num1 == num2:
        num1 = random.randint(10, 900)
        num2 = random.randint(2, 650)
        ans = num1 / num2
    # Ask user for answer
    answer_from_user = input("What is " + str(num1) + " / " + str(num2) + "? ")
    user_answer = check_valid_input(answer_from_user)
    # Check answer and do actions accordingly
    if ans != user_answer and incorrect_answers < INCORRECT_ANSWER_MAX:
        incorrect_answers = adjust_incorrect_answers(ans, incorrect_answers)
    elif ans == user_answer:
        print("Well done! That answer is correct!")

    return begin_incorrect == incorrect_answers


def multiplication_questions(incorrect_answers):
    """
    User gets asked multiplication questions
    """
    begin_incorrect = incorrect_answers
    # Generate numbers and answer for addition
    num1 = random.randint(1, 49)
    num2 = random.randint(2, 20)
    ans = num1 * num2
    # Ask user for answer
    answer_from_user = input("What is " + str(num1) + " * " + str(num2) + "? ")
    user_answer = check_valid_input(answer_from_user)
    # Check answer and do actions accordingly
    if ans != user_answer and incorrect_answers < INCORRECT_ANSWER_MAX:
        incorrect_answers = adjust_incorrect_answers(ans, incorrect_answers)
    elif ans == user_answer:
        print("Well done! That answer is correct!")

    return begin_incorrect == incorrect_answers


# --- ADDITION AND SUBTRACTION
def basic_add_sub():
    """
    This game is played if the user chooses addition and subtraction. This repeats until all five questions have been
    answered correctly or the user lost all lives
    """
    # Initial values
    incorrect_answers = 0
    questions_asked = 0
    while questions_asked < MAX_ASKED_QUESTIONS and incorrect_answers < INCORRECT_ANSWER_MAX:
        # First two questions are addition
        if questions_asked < 2:
            ans = addition_questions(incorrect_answers)
        # Next two questions are division
        elif questions_asked < 4:
            ans = subtract_questions(incorrect_answers)
        # Next question is combination
        else:
            ans = sub_add_question(incorrect_answers)
        # Check if the answer is correct to iterate the correct variable
        if ans:
            questions_asked += 1
        else:
            incorrect_answers += 1
        # Prepare user for next question
        if questions_asked < MAX_ASKED_QUESTIONS:
            print_ready_for_next_question(questions_asked, incorrect_answers)
    # Tell the user if they failed or succeed
    fail_or_succeed_game(incorrect_answers, "additions & subtractions", "math magician")


def sub_add_question(incorrect_answers):
    """
    User gets asked addition and subtraction question
    """
    begin_incorrect = incorrect_answers
    # Generate numbers and answer for subtraction
    num1 = random.randint(50, 650)
    num2 = random.randint(100, 350)
    num3 = random.randint(0, 350)
    ans = num1 - num2 + num3
    # Ask user for answer
    answer_from_user = input("What is " + str(num1) + " - " + str(num2) + " + " + str(num3) + "? ")
    user_answer = check_valid_input(answer_from_user)
    # Check answer and do actions accordingly
    if ans != user_answer and incorrect_answers < INCORRECT_ANSWER_MAX:
        incorrect_answers = adjust_incorrect_answers(ans, incorrect_answers)
    elif ans == user_answer:
        print("Well done. You have answered the last question correctly!")

    return begin_incorrect == incorrect_answers


def subtract_questions(incorrect_answers):
    """
    User gets asked subtraction questions
    """
    begin_incorrect = incorrect_answers
    # Generate numbers and answer for subtraction
    num1 = random.randint(0, 900)
    num2 = random.randint(50, 650)
    # Still allow for negative answers, but it should not be smaller than -50
    while num1 - num2 < -50:
        num2 = random.randint(50, 650)
    ans = num1 - num2
    # Ask user for answer
    answer_from_user = input("What is " + str(num1) + " - " + str(num2) + "? ")
    user_answer = check_valid_input(answer_from_user)
    # Check answer and do actions accordingly
    if ans != user_answer and incorrect_answers < INCORRECT_ANSWER_MAX:
        incorrect_answers = adjust_incorrect_answers(ans, incorrect_answers)
    elif ans == user_answer:
        print("Well done! That answer is correct!")

    return begin_incorrect == incorrect_answers


def addition_questions(incorrect_answers):
    """
    User gets asked addition questions
    """
    begin_incorrect = incorrect_answers
    # Generate numbers and answer for addition
    num1 = random.randint(0, 350)
    num2 = random.randint(50, 650)
    ans = num1 + num2
    # Ask user for answer
    answer_from_user = input("What is " + str(num1) + " + " + str(num2) + "? ")
    user_answer = check_valid_input(answer_from_user)
    # Check answer and do actions accordingly
    if ans != user_answer and incorrect_answers < INCORRECT_ANSWER_MAX:
        incorrect_answers = adjust_incorrect_answers(ans, incorrect_answers)
    elif ans == user_answer:
        print("Well done! That answer is correct!")

    return begin_incorrect == incorrect_answers


# --- FUNCTIONS USED IN MATH GAME
def check_valid_input(user_answer):
    """
    Check that the user has entered an answer that is of type integer or float
    """
    try:
        user_answer = int(user_answer)
        return user_answer
    except ValueError:
        try:
            user_answer = float(user_answer)
            return user_answer
        except ValueError:
            user_answer = input("Please enter a number as an answer: ")
            return check_valid_input(user_answer)


def adjust_incorrect_answers(ans, incorrect_answers):
    """
    If the answer is incorrect, the incorrect questions variable is incremented and the user get told what the correct
    answer is
    """
    print("Incorrect! The correct answer is: ", ans)
    incorrect_answers = user_live_left(incorrect_answers)
    return incorrect_answers


def print_ready_for_next_question(questions_asked, incorrect_answers):
    """
    Tells user to get ready for next question
    """
    if incorrect_answers < INCORRECT_ANSWER_MAX:
        print("")
        print("Get ready for question number", questions_asked + 1, " of", MAX_ASKED_QUESTIONS)


# --- SET-UP MATH GAME CHOICES AVAILABLE FOR USERS TO CHOOSE FROM
def math_games_choices():
    """
    Explanation of math games available
    """
    print("-----------------------------------------------------------------------------------------------------")
    print("You chose to attempt a math game, so let's test your math skills!")
    print("-----------------------------------------------------------------------------------------------------")
    print("With the math games, we have created four different levels to test your skills.")
    print("In order to win a game you need to get answer at least {} answers correctly."
          .format(LETTERS.get(MAX_ASKED_QUESTIONS)))
    print("But don't fear you have {live} lives, so you can make up to {live} mistakes before you loose."
          .format(live=LETTERS.get(INCORRECT_ANSWER_MAX)))
    print("You have a choice between the following four math games:")
    print("Option 1 - Addition and subtraction of numbers")
    print("Option 2 - Multiplication and division of numbers")
    print("Option 3 - Addition, subtraction, multiplication and division of numbers ")
    print("Option 4 - Math word problems")
    print("-----------------------------------------------------------------------------------------------------")
    print("GOOD LUCK MATH MAGICIAN")
    print("Mathematics may not teach us to add love or subtract hate, but it gives us hope that every problem ")
    print("has a solution")
    print("-----------------------------------------------------------------------------------------------------")


# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---
# -------------------------------
# FUNCTIONS FOR GAME SIMULATOR
# -------------------------------
# --- FUNCTIONS USED IN BOTH WORD AND MATH GAMES
def get_question_for_user(questions, tracker):
    """
    Picks a question from all questions available and to ensure question has not been asked before
    questions: the dictionary or list with all the questions
    tracker: the dictionary that keeps track of all questions asked
    """
    total_questions = len(questions)
    question = random.randint(1, total_questions)
    if isinstance(questions, dict):
        while tracker.get(question) != 0:
            question = random.randint(1, total_questions)
    else:
        ques = questions[question - 1]
        while tracker.get(ques) != 0:
            question = random.randint(1, total_questions)
            ques = questions[question - 1]
        question = ques
    tracker[question] = 1
    return question


def create_question_tracker(key_list):
    """
    Creates a dictionary to keep track of the questions asked, based on the total question number
    key_list: the list with all the keys
    """
    dict_new = {}
    for key in key_list:
        dict_new[key] = 0
    return dict_new


def open_load_files_into_dict(file_name, type_elem):
    """
    Open and load the files and create a dictionary
    file_name: is the file that needs to be open an read into a dictionary
    type_elem: identify if number or string. 1 == number and 0 == string
    """
    item = 1
    dict_new = {}
    with open(file_name) as file:
        for line in file:
            line = line.strip()
            # If the value should be a number, type will be 1 and the following code will convert it to int / float
            if type_elem == 1:
                line = float(line)
                if int(line) == line:
                    line = int(line)
            dict_new[item] = line
            item += 1
    return dict_new


def user_live_left(incorrect_answers):
    """
    Determine how many lives the user have left
    """
    incorrect_answers += 1
    live_left = INCORRECT_ANSWER_MAX - incorrect_answers
    if live_left == 2:
        print("You just lost a life and only have", live_left, "lives left.")
    elif live_left == 1:
        print("You just lost a life and only have", live_left, "live left.")
    else:
        print("You just lost a life and have no more lives left... :/")
        print("")
    return incorrect_answers


def fail_or_succeed_game(incorrect_answers, game_name, game_type):
    if incorrect_answers == 3:
        print("You have failed at {} :<".format(game_name))
    else:
        print("")
        print('Well done you clever {0}! You just showed "{1}" who is boss! :>'.format(game_type, game_name))


# --- USER CHOOSES WHAT GAME THEY WANT TO PLAY
def user_chooses_game_option(min_option, max_option):
    """
    Ask the user for their choice of game and make sure it is the correct choice
    min_option: smallest int that the user can choose
    max_option: largest int that the user can choose
    """
    user_input = input("What is your preferred choice?: ")
    # Check that option entered is an integer
    if user_input != 'exit':
        try:
            user_input = int(user_input)
            # Check that option is in range
            user_input = check_user_made_correct_choice(user_input, min_option, max_option)
            return user_input
        # When user did not enter an int option, tell the user and ask again
        except ValueError:
            print("Please enter a integer to continue")
            return user_chooses_game_option(min_option, max_option)
    else:
        return user_input


# --- CHECK THAT THE USER MADE CORRECT CHOICES WHEN CHOOSING GAMES
def check_user_made_correct_choice(user_input, min_option, max_option):
    """
    Check to make sure the user did make the right decision - in other words entered 1, 2, etc. depending on
    stage of games
    user_input: the choice the user has made
    min_option: smallest int that the user can choose
    max_option: largest int that the user can choose
    """
    # Create list of all options available
    options = []
    loop_range = max_option - min_option + 1
    elem = min_option
    for i in range(loop_range):
        options.append(elem)
        elem += 1
    # Check if option in range, if not in range keep on asking until option in range is given
    while user_input < min_option or user_input > max_option:
        print("You can only choose any of the following values", options,
              ", nothing else is accepted, please try again!")
        user_input = user_chooses_game_option(min_option, max_option)
    return user_input


# --- GIVE THE USER AN OPTION TO PLAY ANOTHER GAME
def retry_another_problem():
    """
    Give the user the option to stop the game or try another shot
    """
    print("-----------------------------------------------------------------------------------------------------")
    print("Do you want to continue playing games?")
    print("If you do not want to continue, you can enter 'exit' when prompted")
    print("-----------------------------------------------------------------------------------------------------")
    print("You have the option to play two types of games and we will be testing your logic skills.")
    print("If you want us to test your math skills, you can choose option 1 for math games!")
    print("If you want us to test your word skills, you can choose option 2 for word games!")
    print("-----------------------------------------------------------------------------------------------------")


# --- EXPLAIN WHAT WILL HAPPEN IN THIS GAME SIMULATOR
def game_terminal_welcome_msg():
    """
    Print the welcome message to game terminal and explain options between math and word games
    """
    print("-----------------------------------------------------------------------------------------------------")
    print("Hello, are you ready for some fun?")
    print("-----------------------------------------------------------------------------------------------------")
    print("You have the option to play two types of games and we will be testing your logic skills.")
    print("If you want us to test your math skills, you can choose option 1 for math games!")
    print("If you want us to test your word skills, you can choose option 2 for word games!")
    print("-----------------------------------------------------------------------------------------------------")


# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---
# -------------------------------
# SET-UP WELCOME CONSOLE SCREEN
# -------------------------------
def welcome_screen():
    """
    Creates the welcome screen to my final Code in Place project
    """
    # Create Canvas
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Welcome to my Final Project')
    canvas.update()
    # Read in welcome and change sufficient white pixels
    welcome_image = replace_white_pixels(SimpleImage(WELCOME_IMAGE), SimpleImage(NORTHERN_LIGHTS))
    pil_welcome_image = ImageTk.PhotoImage(welcome_image.pil_image)
    canvas.create_image(CANVAS_WIDTH / 2 - welcome_image.width / 2, 10, anchor='nw', image=pil_welcome_image)
    canvas.update()
    # Get the welcome image height and width for alignment of all other images and shapes
    image_height = welcome_image.height
    image_width = welcome_image.width
    # Add left celebrations picture
    left_image = replace_white_background_pixels(SimpleImage(PARTY_LEFT))
    pil_left_image = ImageTk.PhotoImage(left_image.pil_image)
    x = (CANVAS_WIDTH / 2 - image_width / 2 - left_image.width) / 2
    canvas.create_image(x, image_height / 2 - left_image.height / 2, anchor='nw', image=pil_left_image)
    time.sleep(DELAY * 5)
    canvas.update()
    # Add right celebrations picture
    right_image = replace_white_background_pixels(SimpleImage(PARTY_RIGHT))
    pil_right_image = ImageTk.PhotoImage(right_image.pil_image)
    time.sleep(DELAY * 5)
    x = (CANVAS_WIDTH / 2 - image_width / 2 - right_image.width) / 2
    canvas.create_image(CANVAS_WIDTH - x, image_height / 2 - right_image.height / 2,
                        anchor='ne', image=pil_right_image)
    canvas.update()
    # Create line to break pictures from message
    time.sleep(DELAY * 5)
    canvas.create_line(10, image_height + 30, CANVAS_WIDTH - 10, image_height + 30, fill='purple', width=5)
    canvas.update()
    # Create welcome message to the users
    print_welcome_message(canvas, image_height)
    canvas.update()
    # Create reminder if user forgets to exit window for program to carry on
    # time.sleep(DELAY*10)
    # print_reminder_message(canvas)
    canvas.mainloop()


def print_reminder_message(canvas):
    """
    This codes only run as a  reminder message for the user to closed to close the window to see the rest of the
    program. The message is displayed in the center of the console as a purple box with white text
    """
    exit_width = CANVAS_WIDTH / 8
    exit_height = CANVAS_HEIGHT / 8
    # Create rectangle in center
    canvas.create_rectangle(exit_width, exit_height, exit_width * 7, exit_height * 7, fill='purple', outline='purple')
    # Display the reminder message
    for i in range(len(REMINDER_MSG)):
        line = REMINDER_MSG[i]
        x = (CANVAS_WIDTH - len(line) * 30) / 2
        y = exit_height * (2 + 2 * i)
        canvas.create_text(x, y, anchor='w', font=(FONT_TYPE, 40), text=line, fill='white')
    return canvas


def print_welcome_message(canvas, image_height):
    """
    Print the welcome message to the users
    canvas: the canvas created and used for welcome message
    image_height: the height of the welcome image, used for alignment of message
    """
    time.sleep(DELAY * 5)
    canvas.update()
    y = image_height + 60
    # Print the welcome message
    for i in range(len(WELCOME_MSG)):
        line = WELCOME_MSG[i]
        if i == (len(WELCOME_MSG) - 1):
            x = (CANVAS_WIDTH - len(line) * 10) / 2
        else:
            x = (CANVAS_WIDTH - len(line) * 30) / 2
        # Printing it line for line
        for j in range(len(line)):
            # Instruction after welcome message
            if i == (len(WELCOME_MSG) - 1):
                if j == 0:
                    y -= 10
                canvas.create_text(x, y, anchor='w', font=(FONT_TYPE, 12), text=line[j])
                time.sleep(DELAY / 20)
                canvas.update()
                x += 10
            # Welcome message lines
            else:
                canvas.create_text(x, y, anchor='w', font=(FONT_TYPE, 32), text=line[j])
                time.sleep(DELAY)
                canvas.update()
                x += 30
        y += 50
    return canvas


def replace_white_pixels(image, background_image):
    """
    Change all sufficient white pixels in an image to the pixels from the background image
    image: the image whose white pixels needs to be replaced
    background_image: the image whose background will be used to replaced white pixels in image
    """
    for pixel in image:
        # Get RGB value for pixel in image
        rgb_value = pixel.red + pixel.green + pixel.blue
        # If pixel is sufficiently white change it to the background image pixel
        if rgb_value >= SUFFICIENT_WHITE:
            x = pixel.x
            y = pixel.y
            image.set_pixel(x, y, background_image.get_pixel(x, y))
    return image


def replace_white_background_pixels(image):
    """
    Change all sufficient white pixels in an image to a peach pink colour pixel
    image: the image whose white pixels needs to be changed to peach pink
    """
    for pixel in image:
        # Get RGB value for pixel in image
        rgb_value = pixel.red + pixel.green + pixel.blue
        # If pixel is sufficiently white change it to peach pink
        if rgb_value >= SUFFICIENT_WHITE:
            pixel.green = 218
            pixel.blue = 185
    return image


def close_welcome_screen_msg():
    """
    Message to remind user to close welcome screen, if they have not done it
    """
    print("-----------------------------------------------------------------------------------------------------")
    print("Please close the 'welcome screen' window, in order to be able to play the game :>")
    print("-----------------------------------------------------------------------------------------------------")


# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---# ---
# -------------------------------
# CODE IN PLACE PROVIDED CODE
# ------------------------------

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()

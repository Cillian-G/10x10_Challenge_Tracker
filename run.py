import os
import gspread
from os import system, name
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('10x10_challenge_tracker')


welcome_message = "--------------------------------------------------------"\
    "------------\nWelcome to the 10x10 challenge tracker, a handy tool for "\
    "keeping track \nof your 10x10 challenge as you complete it\n-----------"\
    "---------------------------------------------------------"

description_request = "Enter a brief description of the result of the game:\n"

choice_prompt = "\nEnter 1 for an overview of your progress across all games"\
    "\nEnter 2 for a detailed view of your progress with this game"\
    "\nEnter 3 to return to the start menu"

start_menu = "\nTo see an overview of your progress in the "\
    "challenge, enter 1\nTo log a play, enter 2"\
    "\nTo see data about a particular game, enter 3"\
    "\nTo view a guide to the use of this application, enter 4\n"

guide = "Upon running this program, the user is presented with three options"\
    " as to how they may proceed. This guide will offer some clarification"\
    " regarding each of these three options and their correct use\n"\
    "\n1. Challenge overview\n Selecting this option will present the user "\
    "with an overview of their progress in the challenge. This overview "\
    "takes the form of ten graphs, one for each game. The '█' characters on "\
    "the graphs indicate the number of times a given game has been played, "\
    "while the '░' characters indicate how many 'plays' remain until the "\
    "challenge is complete.\nFor example, the following graph indicates a "\
    "game that has been played 6 times, and shows that 4 games remain to be "\
    "played before the challenge is complete\n '█  █  █  █  █  █  ░  ░  ░  ░'"\
    "\n\n2. Logging session data\nThis option will allow "\
    "the user to log details of a game they played as part of the challenge."\
    " After indicating which game is being logged, the user will be asked "\
    " to input the duration of the session in minutes, the winner's score "\
    "(if applicable), as well as a brief description of the game's result. "\
    "Upon submitting this data, the user will be presented with a summary "\
    "of the details they just entered, as well as a graph of the same type "\
    "shown above which will display their progress in that particular game.\n"\
    "\n3. Single-game overview\nThis option allows players to view a"\
    "a summary of the data they have entered for a particular title, as "\
    "well as some statistics relevant to they type of game in question. "\
    "Players will be presented with a comparison of the durations "\
    "of the first play they recorded with that their most recent games."\
    "\n- It should be noted that that the progress graphs and accompanying "\
    "text (i.e.'x/10 games played') will not continue counting past 10, as "\
    "the purpose of this tool is to assist in tracking the users progress in"\
    " completing the 10x10 challenge. Users may still log data after they "\
    "have played 10 games of a particular title, however this data will not "\
    "be utilised by any of this programs functions for viewing and comparing"\
    " logged plays.\n"


game_selection = int
result_type = ""
game_data_worksheets = ("game1", "game2", "game3", "game4", "game5", "game6",
                        "game7", "game8", "game9", "game10")
active_worksheet = ""
duration_data = ""
score_data = ""
description_data = ""
selected_title = ""
game_type = SHEET.worksheet("game_type")
first_duration = 0
last_duration = 0
number_of_plays = 0
percentage = 0


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome_menu():
    """
    Prints welcome menu and basic instructions
    """
    clear()
    print(welcome_message)
    while True:
        choice = input(start_menu)
        if choice == "1":
            overview_graph()
            break
        elif choice == "2":
            get_game_selection()
            game_data_input()
            break
        elif choice == "3":
            get_game_selection()
            print_logged_data()
            break
        elif choice == "4":
            show_guide()
        else:
            clear()
            print("Invalid selection, please choose from the options listed")


def validate_game_selection(selection):
    """
    Validates user input during game selection process
    """
    clear()
    try:
        selection = int(selection)
        if (selection >= 1 and selection <= 10):
            return True
        else:
            raise ValueError(
                "Please enter a value between 1 and 10")
    except ValueError as e:
        print(f"{selection} is not a valid input, please try again")
        return False


def validate_duration(duration):
    """
    Validates user-input value for the duration of a logged play
    """
    clear()
    try:
        duration = int(duration)
        if (duration >= 10 and duration <= 500):
            return True
        else:
            raise ValueError(
                "Please enter a value between 10 and 500")
    except ValueError as e:
        print(f"Invalid input: {duration}")
        return False


def validate_score(score):
    """
    Validates user-input value for the score of a logged play, if
    the game is score-based
    """
    clear()
    try:
        if type(int(score)) == int:
            return True
        else:
            raise ValueError(
                "Please enter an integer value")
    except ValueError as e:
        print(f"Invalid input: {score} is not an integer value")
        return False


def validate_description(description):
    """
    Validates user-input value for the description of a logged play
    ensuring it is between 10 and 60 characters long
    """
    clear()
    try:
        if len(description) >= 10 and len(description) <= 60:
            return True
        else:
            print(
                "Description must be 10-60 characters")
    except ValueError as e:
        print(f"Invalid input: {description}")
        return False


def get_game_selection():
    """
    Requests the user to input a number corresponding to the game
    they wish to select, and sets the active worksheet to correspond
    to this number
    """
    clear()
    while True:
        game_selection_instructions = "\nEnter the number that corresponds "\
                                    "to the game you wish to select\n"

        global game_selection
        global result_type
        global active_worksheet
        global selected_title

        print(game_selection_instructions)

        for ind in range(1, 11):
            title = game_type.cell(ind, 2).value
            print(f"{ind} {title}")

        game_selection = input("\nEnter your game selection here: ")
        if validate_game_selection(game_selection):
            selected_title = game_type.cell(game_selection, 2).value
            result_type = game_type.cell(game_selection, 3).value
            active_worksheet = game_data_worksheets[int(game_selection) - 1]
            print(f"You have selected {selected_title}")
            active_worksheet = SHEET.worksheet(active_worksheet)
            break


def get_duration():
    """
    Requests the user to input the duration of their game in minutes,
    and inserts this input into the appropriate cell of the active worksheet
    """
    global duration_data
    while True:
        duration_data = input("Enter game duration in minutes: ")
        if validate_duration(duration_data):
            break
    values_list = active_worksheet.col_values(1)
    row_location = len(values_list) + 1
    active_worksheet.update_cell(row_location, 1, duration_data)


def get_score():
    """
    Requests the user to input the score of their game, if applicable,
    and inserts this input into the appropriate cell of the active worksheet
    """
    global score_data
    while True:
        score_data = input("Enter winning player's score: ")
        if validate_score(score_data):
            break
    values_list = active_worksheet.col_values(2)
    row_location = len(values_list) + 1
    active_worksheet.update_cell(row_location, 2, score_data)


def get_result_description():
    """
    Requests the user to input a description of the result of their game,
    and inserts this input into the appropriate cell of the active worksheet
    """
    global description_data
    while True:
        description_data = input(f"{description_request}")
        if validate_description(description_data):
            break
    values_list = active_worksheet.col_values(3)
    row_location = len(values_list) + 1
    active_worksheet.update_cell(row_location, 3, description_data)


def game_data_input():
    """
    Calls the get_duration, get_score, and get_description functions in order
    """
    get_duration()
    if result_type == "score_based":
        get_score()
    get_result_description()
    clear()
    print(f"{selected_title} session summary\nLength:{duration_data} mins")
    if result_type == "score_based":
        print(f"Winning score: {score_data}")
    print(f"Description: {description_data}")
    print("")
    challenge_graph()
    menu_return()


def challenge_graph():
    """
    Prints a graph of challenge progress for the currently selected game
    based on the number of occupied rows in that games spreadsheet
    """
    games_played = len(active_worksheet.col_values(1)) - 1
    if games_played >= 10:
        completed = " - Game Completed!"
        games_played = 10
    else:
        completed = ""
    games_remaining = 10 - games_played
    print(f"{selected_title} - {games_played}/10 games played{completed}")
    graph = ""
    for i in range(games_played):
        graph += "█   "
    for i in range(games_remaining):
        graph += "░   "

    print(graph)
    return games_played


def overview_graph():
    """
    Call the challenge graph function once for each game in the challenge,
    and displays a numerical 'x/100' to display the users cumulative progress
    """
    global active_worksheet
    global selected_title
    games_tally = 0
    clear()
    for ind in range(1, 11):
        game_selection = int(ind)
        selected_title = game_type.cell(game_selection, 2).value
        active_worksheet = game_data_worksheets[int(game_selection) - 1]
        active_worksheet = SHEET.worksheet(active_worksheet)
        games_tally += challenge_graph()
    if games_tally >= 100:
        games_tally = 100
        congrats = " -- Congratualtions on completing your 10x10 challenge!"
    else:
        congrats = ""
    print(f"{games_tally}/100 games played{congrats}")
    menu_return()


def show_guide():
    """
    Prints a guide intended to instruct use of the 10x10 Challenge Tracker
    """
    clear()
    print(guide)
    menu_return()


def print_logged_data():
    """
    Prints the logged data for each play of a user-selected game
    """
    global first_duration
    global last_duration
    global number_of_plays
    number_of_plays = len(active_worksheet.col_values(1)) - 1
    if number_of_plays > 10:
        number_of_plays = 10
    for i in range(1, number_of_plays+1):
        duration = active_worksheet.cell((i+1), 1).value

        if i == 1:
            first_duration = int(duration)
        elif i == number_of_plays:
            last_duration = int(duration)

        if result_type == "score_based":
            score = active_worksheet.cell((i+1), 2).value
            score_string = f" Score: {score}"
        else:
            score_string = ""

        result_description = active_worksheet.cell((i+1), 3).value

        print(f"Session {i}. Duration: {duration} minutes.{score_string}")
        print(f"Result description: {result_description}")

    if number_of_plays == 0:
        print("There are no plays recorded for this game")
    comparison()


def comparison():
    """
    Compares the duration of the users first play of a given game to that of
    their most recent game
    """
    global percentage
    if number_of_plays > 1:
        if first_duration > last_duration:
            percentage = int((1 - (last_duration / first_duration)) * 100)
            print(recent_game + str(percentage) + duration_decrease)
        elif first_duration < last_duration:
            percentage = int(((last_duration / first_duration) - 1) * 100)
            print((recent_game + str(percentage) + duration_increase))
        else:
            print("")
    menu_return()


recent_game = "\nThe duration of your most recent game was "
duration_increase = "% longer than your first"
duration_decrease = "% shorter than your first"


def menu_return():
    """
    Prompts the user to press enter to return to the welcome menu
    """
    while True:
        input("Press enter to return to the start menu\n")
        if input:
            clear()
            welcome_menu()
            break


welcome_menu()

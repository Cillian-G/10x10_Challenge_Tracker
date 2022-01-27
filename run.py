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


welcome_message = "Welcome to 10x10_challenge_tracker, a handy tool for "\
                  "keeping track \nof your 10x10 challenge as you complete "\
                  "it"

game_selection = int
result_type = ""
game_data_worksheets = ("game1", "game2", "game3", "game4", "game5", "game6",
                        "game7", "game8", "game9", "game10")
active_worksheet = ""


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


def validate_game_selection(selection):
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
    try:
        duration = int(duration)
        if (duration >= 10 and duration <= 500):
            return True
        else: 
            raise ValueError(
                "Please enter a value between 10 and 500")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return False


def get_game_selection():
    """
    Requests the user to input a number corresponding to the game
    they wish to select
    """
    while True:
        game_selection_instructions = "\nEnter the number that corresponds "\
                                    "to the game you wish to enter data for\n"

        print(game_selection_instructions)

        game_type = SHEET.worksheet("game_type")
        # for ind in range(1, 11):
        #     title = game_type.cell(ind, 2).value
        #     print(f"{ind} {title}")

        global game_selection
        global result_type
        global active_worksheet
        game_selection = input("\nEnter your game selection here: ")
        if validate_game_selection(game_selection):
            selected_title = game_type.cell(game_selection, 2).value
            result_type = game_type.cell(game_selection, 3).value
            active_worksheet = game_data_worksheets[int(game_selection) - 1]
            print(f"You have selected {selected_title}")
            print(active_worksheet)
            active_worksheet = SHEET.worksheet(active_worksheet)
            break
    game_data_input()


def get_duration():
    while True:
        duration_data = input("Enter game duration in minutes: ")
        if validate_duration(duration_data):
            break
    values_list = active_worksheet.col_values(1)
    row_location = len(values_list) + 1
    active_worksheet.update_cell(row_location, 1, duration_data)


def get_score():
    while True:
        score_data = input("Enter winning players score: ")




def game_data_input():
    get_duration()
    if result_type == "score_based":
        get_score()
    # get_result_description()
    # current_game_overview()


welcome_menu()
get_game_selection()


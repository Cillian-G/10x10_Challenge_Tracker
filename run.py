import gspread
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


def welcome_menu():
    """
    Prints welcome menu and basic instructions
    """
    print(welcome_message)


def get_game_data():
    """
    Takes game details input by user and records them to 
    the google sheet for the game in question
    """
    game_selection_instructions = "Enter the number that corresponds to the "\
                                  "game you wish to enter data for"

    print(game_selection_instructions)

    game_title = SHEET.worksheet("game_type")
    for ind in range(1, 11):
        title = game_title.cell(ind, 2).value
        print(f"{ind} {title}")

    game_selection = input("Enter your game selection here: ")
    return game_selection


welcome_menu()
print(get_game_data())



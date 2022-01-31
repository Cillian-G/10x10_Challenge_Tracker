# 10x10 Challenge Tracker

The 10x10 Challenge Tracker is a tool designed to assist users in keeping track of their 10x10 challenge.
The 10x10 Challenge is a self imposed challenge undertaken by hobby board-game enthusiasts. The purpose of the challenge is to encourage players to explore the strategic depth of games in their collections, rather than swapping out old games for new ones after a handful of plays. The challenge consists of choosing 10 of lesser-played games from one’s collection, and playing these games 10 times each.
![am i responsive screenshot](/documentation/am_i_responsive.png)

## User Stories

 - I want to be able to log the games that I play while partaking in this challenge
 - I want to have access to an overview of my progress through the challenge
 - I want to be able to access the data I have entered.

## UX 

 - The Challenge tracker was designed so that after interacting with each “function” of the tool, the user would be directed back to the welcome menu where they would only be one input away from the next function they wished to use.
 - This design mean that once users had finished inputting data, or viewing the different types of overviews, the instructions as to how to return to the menu only took up one line of the terminal, rather than the 3 or 4 lines that would have been necessary to present the user with all of the available and relevant functions. This decision was made to avoid unnecessary clutter on the terminal, which was especially important on the challenge overview page, where it is important that the complete overview can be viewed in the terminal without scrolling.
![terminal filled with overview graphs](/documentation/overview_graphs.png)

### Flowchart

 flowchart PIC 
 
 
 
 ![](/documentation/am_i_responsive.png)

## Features

### sheets

![game type sheet](/documentation/game_type_sheet.png)

The foundation of the 10x10 Challenge Tracker is a google sheets spreadsheet, which is where the data logged by the user is stored. The game_type sheet stores the titles of each game, the titles of their corresponding worksheets, as well as an entry for their game type, which will determine whether or not they are treated as a score-based game by the program.

![game1 sheet](/documentation/game1_sheet.png)

Each game will have its own worksheet where details of logged plays will be recorded. These sheets can be edited by the user to allow them to replace the placeholder titles with the titles of the games they wish to undertake the challenge with.

### Welcome menu

![welcome menu](/documentation/welcome_menu.png)

Upon running the program the user will be presented with the ‘welcome menu’. The header of the menu contains a brief summary of the tool’s purpose. Below the header, there is a list of four options as to how the user may proceed, each with a corresponding number. The user is instructed to choose one of these options by entering its number.

![menu validation](/documentation/menu_validation.png)

 If the user inputs anything other than the listed numbers, the program will inform them of this error and request that they enter a valid input.

### Overview

![overview graphs](/documentation/overview_graphs.png)

If the user selects the first option in the welcome menu, which reads ‘To see an overview of your progress in the challenge, enter 1’, the program will generate a graph of their progress in the challenge. Each game of the ten they have chosen will have a progress graph printed beneath its name, as well as a numerical ‘counter’. The solid blocks on the graph represent logged plays of a given game, while the shaded blocks represent how many plays remain before the challenge is complete.

![game completed](/documentation/overview_game_completed.png)

When all 10 games have been played, the numerical counter will change from ‘9/10 games played’ to ‘10/10 games played - Game completed!’. If the user logs any further plays of this game, the progress graph and counter will not reflect these changes, as the tool is designed for tracking progress across this challenge specifically.

![overview hundreds counter](/documentation/overview_hundred_counter.png)

Below the 10th and final graph in this overview there is another numerical counter which tracks the user’s overall progress through the challenge.

### Logging a game

![game selection menu](/documentation/game_selection.png)

The second option in the welcome initiates the process for logging a ‘play’ or session of a given game in that games associated google sheet. The user will first be requested to select the game they wish to log a play of from a list of the 10 games chosen for the challenge.

![duration input request](/documentation/duration_input.png)

Users will first be requested to enter the duration of their game in minutes. This process will only accept integers that are greater than or equal to 10, and less than or equal to 500, as values outside of this range suggest that the game in question isn’t compatible with the purpose of the challenge.

![score input request](/documentation/score_input.png)

If the game is assigned the game type of score_based in the game_type sheet created by the user, then the user will be requested to enter a winning score when logging a play of this game. The validation for this input only requires the winning score to be an integer value, as many games feature very low scores, or even negative scoring.

![description input request with validation message](/documentation/description_validation.png)

The user will then be requested to enter a brief description of the result of the game they played. This is important as not all games have a score-based single-winner outcome. Allowing users to enter a description of their session allows them to capture the important details about the game. This input will only accept between 10 and 60 characters, as values below this range are unlikely to be usefully descriptive, and values above this range make the viewing of session logs more cluttered and difficult to read.

![input summary screen](/documentation/input_summary.png)

The details entered by the user are summarised once this process is complete. The user is then presented with an updated progress graph for the game in question, as well as a prompt to return to the welcome menu. It should be noted that players may log plays after completing 10 plays of a given game, however these plays will not be reflected in the graphs, counters, or statistics generated by the program

### Detailed Data

![detailed game data printout](/documentation/detailed_data.png)

The third option in the welcome menu allows the user to see detailed data about a their plays of a single game. They are first prompted to choose a game from their list, just as when inputting data. Upon choosing a game, the user is presented with a printout containing formatted data from the plays they have logged of that game, up to their 10th play. This printout will only list a “score” if the selected game is of the score_based ‘type’.

### Guide

![guide printout](/documentation/guide.png)

 The final option presented to the player in the welcome menu is the guide. This guide offers a simple summary of the functions of the 10x10 Challenge Tracker


## Technologies Used (explain various tech used, such as HTML, CSS, Balsamiq, TinyPNG, Gitpod, GitHub, Git, etc.)
## Testing
 - Make TESTING.md file

https://github.com/Cillian-G/10x10_Challenge_Tracker/commit/b71c9575af9c431a4f47f2c8efe861e9c64c35a3?diff=split 
 -  Aware of the commit

 - List bugs fixed with Tim
 - Entering strings for ints etc. change menu input if statements from if 1 to if "1" etc.
 - negative value for games_remaining
 -rate limi screenshot from Tim
### Code Validation
### Tested User Stories
 - paste user stories, use same screenshots from feautes to line up with features.
### Unfixed Bugs
- if you have any. if not "No unfixed bugs that i am aware of"
## Deployment
 - Creating credentials step-by-step as per the Code Institute instiructional video
 - how to get google sheets, APIs etc, how to Heroku, get Heroku to connect with Github.

### Local Deployment

In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/Cillian-G/10x10_Challenge_Tracker.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Cillian-G/10x10_Challenge_Tracker)

You'll need to install the required packages in order for this application to run. To do that, you can use this command:

- `pip3 install -r requirements.txt`

## Credits
 - code insitute love sandwiches for APIS, Creds.json etc
 - stack overflow stuff
 - slack community (find some links)

### Acknowledgements

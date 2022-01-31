# TESTING 
 
## Code Validation

![python validation](/documentation/testing/testing_python_validation.png)

Python code was validated at pep8online.com

## Fixed Bugs

![game selection error](/documentation/testing/testing_game_selection_error.png)
![menu error](/documentation/testing/testing_menu_error.png)

Most of the bugs encountered during this project emerged from code in the input validation functions. Specifically, the program was crashing whenever a non-numerical value was entered into an input which expected an integer. When this bug was initially fixed, another problem emerged which was that the error messages thrown in the terminal would have been unintelligible to most users. This secondary issue was resolved when appropriate, user-friendly error messages were substituted in their place These bugs were discovered during a mentor meeting and were promptly fixed.#

![testing rate limit ](/documentation/testing/testing_rate_limit.png)

Another bug was discovered during a mentor meeting but it was quickly determined that this was due to both myself and my mentor simultaneously editing the google sheet as well as using the deployed site

## Unfixed Bugs

Though there are no unfixed bugs that I am aware of, there was a commit message typo that was made. The commit message in questions merely consists of "Add", which was the result of accidentally pressing the enter key while still typing out the message. This commit is linked below.

https://github.com/Cillian-G/10x10_Challenge_Tracker/commit/b71c9575af9c431a4f47f2c8efe861e9c64c35a3?diff=split 



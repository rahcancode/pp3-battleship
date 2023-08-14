## Battleships

This is a simple Python terminal game, run in a mock terminal provided by Code Institute in Heroku
The aim of the game is to hit one of five ships that are positioned randomly in a 10x10 grid, using 25 bullets or less
You can find more information about the game of Battleships on its ![Wikipedia page - Battleship (game)](https://en.wikipedia.org/wiki/Battleship_(game))

![Here is a live version of my project on Heroku](https://pp3-battleship-august2023-9cb0d7252a27.herokuapp.com)

![Responsive Image](https://github.com/rahcancode/pp3-battleship/blob/main/media/responsive.PNG)

![GitHub contributors](https://img.shields.io/github/contributors-anon/rahcancode/pp3-battleship)![GitHub top language](https://img.shields.io/github/languages/top/rahcancode/pp3-battleship)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/rahcancode/pp3-battleship)
## How to play

Battleships Game Overview ¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>

Username: Enter a username to start the game
Grid Setup: A 10x10 grid holds 5 ships of varying lengths, placed randomly
Ammunition: Use 25 bullets to target and destroy ships on the grid
Shooting: Choose a grid location (e.g., C4) to fire a bullet
Outcome Display: Shots' outcomes (hit or miss) are shown on the grid
Ship Orientation: Ships don't place diagonally; a hit extends up, down, left or right
Victory Condition: Sink at least 1 of 5 ships before running out of bullets

    Legend:
    1. "." = water or empty space
    2. "O" = part of ship
    3. "X" = part of ship that was hit with bullet
    4. "#" = water that was shot with bullet, a miss because it hit no ship

## Features
# Existing Features

Upon starting the game, the user is prompted to enter a username. This is used in various print statements for win/lose

![Start or opening image](https://github.com/rahcancode/pp3-battleship/blob/main/media/open.PNG)

If a username or a single value is not entered, the terminal will continue to prompt the user until a value is input

![Username validation image](https://github.com/rahcancode/pp3-battleship/blob/main/media/usernamevalidation.PNG)

The terminal prompts you to enter values for a row (A-J) and column (0-9) such as "C4" and then will tell you if you have hit or missed

![You got a hit image](https://github.com/rahcancode/pp3-battleship/blob/main/media/hit.PNG)
![You missed image](https://github.com/rahcancode/pp3-battleship/blob/main/media/miss.PNG)

If you enter the same value again, the terminal will tell you have already shot a bullet there

![Bullet already shot image](https://github.com/rahcancode/pp3-battleship/blob/main/media/alreadyshot.PNG)

If the values entered are incorrect or invalid, an error will display prompting you to enter correct values for a row (A-J) and column (0-9)

![Invalid input image](https://github.com/rahcancode/pp3-battleship/blob/main/media/invalidinput.PNG)

When you have sunk at least one of five ships, a win message displays

![Win message image](https://github.com/rahcancode/pp3-battleship/blob/main/media/win.PNG)

If you run out of bullets without sinking a ship, a lose message displays

![Lose message image](https://github.com/rahcancode/pp3-battleship/blob/main/media/lose.PNG)

At the end of each game, win or lose, the ships positions are displayed
The terminal will also prompt you to play again yes/no and the game will restart
# Future Features

- A leaderboard would be a great addition, so that players can rank against friends or themselves
- Allow user to set a difficutly (smaller board, more or less ships, ship size, more or less bullets etc)
- Two player mode: Two boards, one for the user and one for the computer to play, like in the game of Battleships

## Testing

I have manually tested this project by completing the following:

The code was run through the ![CI Python Linter using PEP8](https://pep8ci.herokuapp.com/#) and no errors were found at the time of the last commit

- User testing:
- I have tried to start the game by pressing return instead of entering a value for a username, and the username prompt repeats (see image above)
- I have tried entering invalid values outside of the requested "row (A-J) and column (0-9)" and the correct error message appears (see images above)

## Bugs
# Solved Bugs

- During testing the grid automatically displayed the location of the boats from the beginning, which negated the purpose of the game. 
- I added print_grid(game_over) function to hide the positions of the boats until the game is won or lost.

- During testing I discovered that the terminal wasn't correctly printing the location of the boats when hit. 
- The bullet counter would decrease, and the "bullet already shot" error would print if the same input was used again, but the terminal would not change a "." to a "X" to show a boat was hit
- I discovered the code was not correctly displaying the ship ("O") when it was hit in the print_grid() function because the value was incorrect and it was defaulting to ".".
# Remaining Bugs

- The game should end when one boat has been hit two or more times, and a win message displays.
- Currently, the code will end the game once one boat is completely sunk. The number of hits is determined by the size of the boat (3 hits for a boat sized 3, 5 hits for a boat sized 5 etc)
# Validator Testing

![PEP8](https://pep8ci.herokuapp.com/#)
-  No errors were found at the time of the last commit
## Deployment

This project was deployed using the mock terminal in Heroku, created by Code Institute

To deploy:
- Fork/clone the repository
- Create a new Heroku app
- In Settings: Config Vars should be Port with a value of 8000
- In Settings: Buildpacks should be Python then NodeJS (in that order only)
- In Deploy: Link Github repo to Heroku
- Press Deploy Branch

## Credits
# Tools/Media

![ASCII Art](https://asciiart.website/index.php?art=transportation/nautical) for ascii image of submarine and fish at the start of the game
![patorjk.com](https://patorjk.com/software/taag/#p=display&f=Digital&t=Battleships) for ascii text Battleships under the ascii image at the start of the game
![PEP8 validator](https://pep8ci.herokuapp.com/#)

# Humans

My husband: For making sure I had the time and space to create this project under a tight deadline (as always)
Loz: Two snake heads are better than one in the 11th hour with coffee and cake for breakfast

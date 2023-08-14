## Battleships

This is a simple Python terminal game, run in a mock terminal provided by Code Institute in Heroku.
The aim of the game is to hit one of five ships that are positioned randomly in a 10x10 grid, using 25 bullets or less.
You can find more information about the game of Battleships on its ![Wikipedia page - Battleship (game)](https://en.wikipedia.org/wiki/Battleship_(game)).

![Here is a live version of my project on Heroku](https://pp3-battleship-august2023-9cb0d7252a27.herokuapp.com)

![Responsive Image](https://github.com/rahcancode/pp3-battleship/blob/main/media/responsive.PNG)

![GitHub contributors](https://img.shields.io/github/contributors-anon/rahcancode/pp3-battleship)![GitHub top language](https://img.shields.io/github/languages/top/rahcancode/pp3-battleship)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/rahcancode/pp3-battleship)
## How to play

Battleships Game Overview ¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>

Username: Enter a username to start the game.
Grid Setup: A 10x10 grid holds 5 ships of varying lengths, placed randomly.
Ammunition: Use 25 bullets to target and destroy ships on the grid.
Shooting: Choose a grid location (e.g., C4) to fire a bullet.
Outcome Display: Shots' outcomes (hit or miss) are shown on the grid.
Ship Orientation: Ships don't place diagonally; a hit extends up, down, left or right.
Victory Condition: Sink at least 1 of 5 ships before running out of bullets.

    Legend:
    1. "." = water or empty space
    2. "O" = part of ship
    3. "X" = part of ship that was hit with bullet
    4. "#" = water that was shot with bullet, a miss because it hit no ship

## Features

Upon starting the game, the user is prompted to enter a username. This is used in various print statements for win/lose.

![Start or opening image](https://github.com/rahcancode/pp3-battleship/blob/main/media/open.PNG)

If a username or a single value is not entered, the terminal will continue to prompt the user until a value is input.

![Username validation image](https://github.com/rahcancode/pp3-battleship/blob/main/media/usernamevalidation.PNG)

The terminal prompts you to enter values for a row (A-J) and column (0-9) such as "C4" and then will tell you if you have hit or missed.

![You got a hit image](https://github.com/rahcancode/pp3-battleship/blob/main/media/hit.PNG)
![You missed image](https://github.com/rahcancode/pp3-battleship/blob/main/media/miss.PNG)

If you enter the same value again, the terminal will tell you have already shot a bullet there.

![Bullet already shot image](https://github.com/rahcancode/pp3-battleship/blob/main/media/alreadyshot.PNG)

If the values entered are incorrect or invalid, an error will display prompting you to enter correct values for a row (A-J) and column (0-9).

![Invalid input image](https://github.com/rahcancode/pp3-battleship/blob/main/media/invalidinput.PNG)

When you have sunk at least one of five ships, a win message displays.

![Win message image](https://github.com/rahcancode/pp3-battleship/blob/main/media/win.PNG)

If you run out of bullets without sinking a ship, a lose message displays.




# Existing Features

# Future Features

A leaderboard would be a great addition, so that players can rank against friends or themselves.

## Testing

PEP8
User testing (no boats)

# Bugs
# Solved Bugs
# Remaining Bugs

# Validator Testing

## Deployment

# Credits

https://asciiart.website/index.php?art=transportation/nautical for ascii image of submarine and fish
https://patorjk.com/software/taag/#p=display&f=Digital&t=Battleships for ascii text Battleships
https://pep8ci.herokuapp.com/# PEP8 validator


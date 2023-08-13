# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
    -------BATTLESHIP-------
    How it will work:
    1. A 10x10 grid will have 6 ships of variable length placed randomly
    2. You have 30 bullets to take down the ships that are placed
    3. Choose a row and column to shoot your shot
    4. Every shot will show up in the grid, hit or miss
    5. If all ships are sunk before using up all bullets, you win

    Legend:
    1. "~" = water or empty space
    2. "0" = part of ship
    3. "X" = part of ship that was hit with bullet
    4. "#" = water that was shot with bullet, a miss because it hit no ship
"""
# Text image of a battleship
f = open('battleship_art.txt', 'r')
import random
import time

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
    4. "#" = a miss, only water was shot
"""
GRID_SIZE = 10
NUM_OF_SHIPS = 6
MAX_BULLETS = 30
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def validate_grid_and_place_ship(grid, ship_positions, start_row, end_row, start_col, end_col):
    """Check if it's safe to place a ship on the grid and update the grid accordingly"""
    all_valid = all(grid[r][c] == "." for r in range(start_row, end_row) for c in range(start_col, end_col))
    if all_valid:
        ship_positions.append((start_row, end_row, start_col, end_col))
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid

# Text image of a battleship
f = open('battleship_art.txt', 'r')
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
import random
import time

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

# ... (functions)

# Global variable for grid
grid = [[]]
# Global variable for grid size
grid_size = 10
# Global variable for number of ships to place
num_of_ships = 6
# Global variable for bullets left
bullets_left = 30
# Global variable for game over
game_over = False
# Global variable for number of ships sunk
num_of_ships_sunk = 0
# Global variable for ship positions
ship_positions = [[]]
# Global variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """Safe to place ship check, based on row and column range"""
    global grid
    global ship_positions

    all_valid = all(grid[r][c] == "." for r in range(start_row, end_row) for c in range(start_col, end_col))
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid

def try_to_place_ship_on_grid(row, col, direction, length):
    """Attempt to place ship, based a specified direction and length"""
    global grid_size

    direction_to_coordinates = {
        "left": (0, -1),
        "right": (0, 1),
        "up": (-1, 0),
        "down": (1, 0)
    }

    row_change, col_change = direction_to_coordinates[direction]

    start_row = max(0, row - (length - 1) * row_change)
    end_row = min(grid_size, row + length * row_change)
    start_col = max(0, col - (length - 1) * col_change)
    end_col = min(grid_size, col + length * col_change)

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)

def create_grid():
    """Build grid, randomly place ships within it"""
    global grid
    global num_of_ships

    random.seed(time.time())

    grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    ship_positions = []

    while len(ship_positions) != num_of_ships:
        random_row = random.randint(0, GRID_SIZE - 1)
        random_col = random.randint(0, GRID_SIZE - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            ship_positions.append((random_row, random_row + 1, random_col, random_col + 1))


def main():
    """Opening the game"""
    print("-----Welcome to Battleship-----")
    print("You have {} bullets to take down {} ships. Sink my battleship!".format(MAX_BULLETS, NUM_OF_SHIPS))

    grid = create_grid()
    ship_positions = []

    while True:
        print_grid(grid)
        print("Ships remaining:", NUM_OF_SHIPS - num_of_ships_sunk)
        print("Bullets remaining:", MAX_BULLETS - bullets_left)
        
        if bullets_left <= 0:
            print("You ran out of bullets, you lose. Better luck next time!")
            break

        if num_of_ships_sunk == NUM_OF_SHIPS:
            print("Gratz, you won!")
            break

        shoot_bullet(grid, ship_positions)
        print("----------------------------")
        print("")

if __name__ == '__main__':
    main()

# Text image of a battleship
f = open('battleship_art.txt', 'r')
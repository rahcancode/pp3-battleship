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

def print_grid():
    """Print the grid with rows A-J and columns 0-9"""
    global grid
    global alphabet

    debug_mode = True

    print("   ", end="")
    for i in range(len(grid[0])):
        print(f"{i:<2}", end="")
    print("\n")

    for row_index, row in enumerate(grid):
        print(f"{alphabet[row_index]:<2}", end=") ")
        for cell in row:
            if cell == "O":
                print("O", end=" ") if debug_mode else print(".", end=" ")
            else:
                print(cell, end=" ")
        print("\n")

def accept_valid_bullet_placement():
    """Get valid row and column to place bullet shot"""
    global alphabet
    global grid

    while True:
        placement = input("Enter row (A-J) and column (0-9) such as C4: ")
        placement = placement.upper()

        if len(placement) != 2 or not placement[0].isalpha() or not placement[1].isdigit():
            print("Error: Please enter a valid row and column such as C4")
            continue

        row = alphabet.find(placement[0])
        col = int(placement[1])

        if row < 0 or row >= grid_size or col < 0 or col >= grid_size:
            print("Error: Please enter valid coordinates (A-J) for row and (0-9) for column")
            continue

        if grid[row][col] in {"#", "X"}:
            print("You have already shot a bullet here, please try again")
            continue

        if grid[row][col] in {".", "O"}:
            return row, col

def check_for_ship_sunk(row, col):
    """Check if a ship has been sunk"""
    global ship_positions
    global grid

    for start_row, end_row, start_col, end_col in ship_positions:
        if start_row <= row <= end_row and start_col <= col <= end_col:
            if all(grid[r][c] == "X" for r in range(start_row, end_row) for c in range(start_col, end_col)):
                return True
    return False

def shoot_bullet():
    """Update grid and ships based on where the bullet was shot"""
    global grid
    global num_of_ships_sunk
    global bullets_left

    row, col = accept_valid_bullet_placement()

    print("\n----------------------------")

    cell = grid[row][col]
    if cell == ".":
        print("You missed, no hit")
        grid[row][col] = "#"
    elif cell == "O":
        print("You hit!", end=" ")
        grid[row][col] = "X"
        if check_for_ship_sunk(row, col):
            print("You sunk a battleship!")
            num_of_ships_sunk += 1
        else:
            print("Shots fired!")

    bullets_left -= 1

def check_for_game_over():
    """Check if the game is over"""
    global num_of_ships_sunk
    global bullets_left
    global game_over

    if num_of_ships_sunk == num_of_ships:
        print("Gratz, you won!")
    elif bullets_left <= 0:
        print("Sorry, you lost! Try again next time?")

    game_over = num_of_ships_sunk == num_of_ships or bullets_left <= 0

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
import random
import time
# Global variable for the player's username
username = ""


"""
    Battleships Game Overview:

Grid Setup: A 10x10 grid is populated with 2 ships of varying lengths, placed randomly.
Ammunition: You have 15 bullets to target and destroy the ships on the grid.
Shooting: You can select a grid location using a row and column combination (e.g., C4) to fire a bullet.
Outcome Display: Each shot's outcome (hit or miss) is displayed on the grid.
Ship Orientation: Ships are not placed diagonally; if a shot hits, the ship extends in one of four directions: left, right, up, or down.
Victory Condition: You win by uncovering all ship positions before running out of bullets; otherwise, you lose.

    Legend:
    1. "~" = water or empty space
    2. "S" = part of ship
    3. "X" = part of ship that was hit with bullet
    4. "#" = water that was shot with bullet, a miss because it hit no ship
"""

# Global variable for grid
grid = [[]]
# Global variable for grid size
grid_size = 10
# Global variable for number of ships to place
num_of_ships = 2
# Global variable for bullets left
bullets_left = 15
# Global variable for game over
game_over = False
# Global variable for number of ships sunk
num_of_ships_sunk = 0
# Global variable for ship positions
ship_positions = [[]]
# Global variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """Will check the row or column to see if it is safe to place a ship there"""
    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid


def try_to_place_ship_on_grid(row, col, direction, length):
    """Based on direction will call helper method to try and place a ship on the grid"""
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                return False

    return True


def create_grid():
    """Will create a 10x10 grid and randomly place down ships
       of different sizes in different directions"""
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)

    num_of_ships_placed = 0

    ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1



def print_grid(game_over):
    """Will print the grid with rows A-J and columns 0-9, revealing hits, misses, and ships if the game is over"""
    global grid
    global alphabet

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if game_over or grid[row][col] == "X" or grid[row][col] == "#" or grid[row][col] == "O":
                print(grid[row][col], end=" ")
            else:
                print(".", end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")




def accept_valid_bullet_placement():
    """Will get valid row and column to place bullet shot"""
    global alphabet
    global grid

    is_valid_placement = False
    row = -1
    col = -1
    while not is_valid_placement:
        placement = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement = placement.upper()
        if len(placement) != 2 or placement[0] not in alphabet or not placement[1].isdigit():
            print("Error: Please enter a valid row (A-J) and column (0-9) such as C4")
            continue
        row = alphabet.index(placement[0])
        col = int(placement[1])
        if not (0 <= row < grid_size) or not (0 <= col < grid_size):
            print("Error: Row and column values must be between A-J and 0-9")
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if grid[row][col] == "." or grid[row][col] == "O":
            is_valid_placement = True

    return row, col



def check_for_ship_sunk(row, col):
    """If all parts of a ship have been shot it is sunk and we later increment ships sunk"""
    global ship_positions
    global grid

    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # Ship found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    return True


def shoot_bullet():
    """Updates grid and ships based on where the bullet was shot"""
    global grid
    global num_of_ships_sunk
    global bullets_left

    row, col = accept_valid_bullet_placement()
    print("")
    print("----------------------------")

    if grid[row][col] == ".":
        print("You missed, no ship was shot")
        grid[row][col] = "#"
    elif grid[row][col] == "O":
        print("You hit!", end=" ")
        grid[row][col] = "X"
        if check_for_ship_sunk(row, col):
            print("A ship was completely sunk!")
            num_of_ships_sunk += 1
        else:
            print("A ship was shot")

    bullets_left -= 1


def check_for_game_over():
    """If all ships have been sunk or we run out of bullets its game over"""
    global num_of_ships_sunk
    global num_of_ships
    global bullets_left
    global game_over

    if num_of_ships == num_of_ships_sunk:
        print("Congrats you won!")
        game_over = True
    elif bullets_left <= 0:
        print("Sorry, you lost! You ran out of bullets, try again next time!")
        game_over = True


def main():
    """Main entry point of application that runs the game loop"""
    global game_over
    global username

    print("-----Welcome to Battleships-----")
    username = input("Enter your username: ")  # Prompt for username
    print(f"Hello, {username}! You have 50 bullets to take down 8 ships. May the battle begin!")

    create_grid()

    while not game_over:
        print_grid(False)
        print("Number of ships remaining:", num_of_ships - num_of_ships_sunk)
        print("Number of bullets left:", bullets_left)
        shoot_bullet()
        print("----------------------------")
        print("")
        check_for_game_over()

    print(f"Game over, {username}!")
    print_grid(True)

if __name__ == '__main__':
    main()
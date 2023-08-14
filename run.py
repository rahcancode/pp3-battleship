import random
import time

# Global variable for the player's username
username = ""

"""
    Battleships Game Overview ¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>

Grid Setup: A 10x10 grid holds 5 ships of varying lengths, placed randomly.
Ammunition: Use 25 bullets to target and destroy ships on the grid.
Shooting: Choose a grid location (e.g., C4) to fire a bullet.
Outcome Display: Shots' outcomes (hit or miss) are shown on the grid.
Ship Orientation: Ships don't place diagonally; a hit extends in 4 directions.
Victory Condition: Uncover all ship positions before running out of bullets.

    Legend:
    1. "." = water or empty space
    2. "O" = part of ship
    3. "X" = part of ship that was hit with bullet
    4. "#" = water that was shot with bullet, a miss because it hit no ship
"""

# Global variables
grid = [[]]
grid_size = 10
num_of_ships = 5
bullets_left = 30
game_over = False
num_of_ships_sunk = 0
ship_positions = [[]]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Ship Placement and Validation


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """Checks if it is safe to place a ship in
    the specified range of rows and columns on the grid."""
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


def is_valid_ship_placement(row, col, direction, length):
    """Check if it's valid to place a ship on the grid
    in the given direction."""
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

# Game Setup and Initialization


def create_grid():
    """Create a 10x10 grid and randomly place ships
    of varying sizes and directions."""
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = [["." for _ in range(cols)] for _ in range(rows)]

    num_of_ships_placed = 0
    ship_positions = []  # Initialize ship_positions

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if is_valid_ship_placement(
            random_row, random_col, direction, ship_size
                ):
            num_of_ships_placed += 1

            # Calculate start and end positions
            start_row, end_row, start_col, end_col = \
                random_row, random_row + 1, random_col, random_col + 1
            if direction == "left":
                start_col = random_col - ship_size + 1
            elif direction == "right":
                end_col = random_col + ship_size
            elif direction == "up":
                start_row = random_row - ship_size + 1
            elif direction == "down":
                end_row = random_row + ship_size

            # Store ship positions
            ship_positions.append([start_row, end_row, start_col, end_col])

            # Mark ship on the grid
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    grid[r][c] = "O"


def print_grid(game_over):
    """Print the grid with rows labeled A-J and columns labeled 0-9,
    revealing game progress and ship positions if the game is over."""
    global grid
    global alphabet

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if game_over or grid[row][col] in ["X", "#"]:
                print(grid[row][col], end=" ")
            else:
                print(".", end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")


def get_valid_integer(prompt, min_value, max_value):
    """Get a valid integer input from the user within the specified range."""
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(
                    f"Please enter a value between {min_value} and {max_value}"
                    )
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def accept_valid_bullet_placement():
    """Get valid row and column coordinates for placing a bullet shot."""
    global alphabet
    global grid_size

    while True:
        placement = input("Enter row (A-J) and column (0-9) such as C4: ")
        placement = placement.upper()

        if len(placement)
        != 2 or placement[0] not in alphabet or not placement[1].isdigit():
            print(
                "Invalid input.Please enter a valid row (A-J) and column (0-9)"
                )
            continue

        row = alphabet.index(placement[0])
        col = int(placement[1])

        if not (0 <= row < grid_size) or not (0 <= col < grid_size):
            print(
                "Invalid input.Row & column values must be between A-J and 0-9"
                )
            continue

        if grid[row][col] == "#" or grid[row][col] == "X":
            print("You have already shot a bullet here. Choose again.")
            continue

        return row, col


def check_for_ship_sunk(row, col):
    """Check if a ship has been completely sunk
    based on the given coordinates."""
    global ship_positions
    global grid

    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]

        if start_row <= row <= end_row and start_col <= col <= end_col:
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
            return True

    return False


# Gameplay and Bullet Shooting

def shoot_bullet():
    """Simulate shooting a bullet at a specified location on the grid,
    and update the grid and ship status based on the shot's outcome."""
    global grid
    global num_of_ships_sunk
    global bullets_left
    global game_over

    bullets_left -= 1

    row, col = accept_valid_bullet_placement()
    print("")
    print("====================")

    if grid[row][col] == ".":
        print("You missed, no ship was shot")
        grid[row][col] = "#"
    elif grid[row][col] == "O":
        print("You got a hit!")
        grid[row][col] = "X"
        if check_for_ship_sunk(row, col):
            num_of_ships_sunk += 1
            print("A ship was completely sunk!")
            if num_of_ships_sunk == num_of_ships:
                print("Congratulations! You've sunk all the ships!")
                game_over = True
    elif grid[row][col] == "X":
        print("You hit the same spot again!")
    else:
        print("You have already shot a bullet here. Choose again.")


def check_for_game_over():
    """Check if the game is over based on the conditions:
        At least one ship has been hit two or more times."""
    global num_of_ships_sunk
    global game_over

    for position in ship_positions:
        if check_for_ship_sunk(position[0], position[2]):
            print("Yay, you won by sinking a ship!")
            game_over = True
            return

    if bullets_left <= 0:
        print("Sorry, you lose, try again next time!")
        game_over = True


# Text image of a battleship

f = open('battleship_art.txt', 'r')
print(f.read())
f.close()

# Main Game Loop and User Interaction


def main():
    """Main entry point of the application that runs the game loop."""
    global username

    print("-----Welcome to Battleships-----")
    username = input("Enter your username: ")

    while not username:
        username = input("Enter your username: ").strip()

    play_again = True

    while play_again:
        global grid
        global grid_size
        global num_of_ships
        global bullets_left
        global game_over
        global num_of_ships_sunk
        global ship_positions

        grid = [[]]
        bullets_left = 30
        game_over = False
        num_of_ships_sunk = 0
        ship_positions = [[]]

        print(
            f"Hello, {username}! You have {bullets_left} bullets" +
            f"to take down 1 of {num_of_ships} ships."
            )

        create_grid()

        while not game_over:
            print_grid(False)
            print("Number of bullets left:", bullets_left)

            shoot_bullet()

            print("====================")
            print("")

            check_for_game_over()

        print(f"Game over, {username}!")
        print_grid(True)

        play_again = input(
            "Do you want to play again? (yes/no): "
                ).strip().lower() == "yes"


if __name__ == '__main__':
    main()

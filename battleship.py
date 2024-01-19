import random

# Function to create an empty grid
def create_grid(rows, cols):
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(' ')
        grid.append(row)
    return grid

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(row)
    pass

# Function to place the ships on the grid
def place_ships(grid, ship_sizes):
    for size in ship_sizes:
        # Add code here to randomly place ships on the grid
        pass

# Function to check if a guess is a hit or a miss
def check_guess(grid, row, col):
    if grid[col][row] != ' ':
        print("Hit!!!")
    else:
        print("HAHAHAHA IMAGINE MISSING")
    pass

# Function to update the grid with the result of a guess
def update_grid(grid, row, col, result):
    if grid[col][row] == ' ':
        grid[col][row] = 'x'
    result = grid
    return result

# Function to check if all the ships are sunk
def check_game_over(grid):
    # Add code here to check if all the ships are sunk
    pass

# Main game loop
def play_battleships():
    # Set up the grid
    rows = 10
    cols = 10
    grid = create_grid(rows, cols)

    # Place the ships on the grid
    ship_sizes = [5, 4, 3, 3, 2]
    place_ships(grid, ship_sizes)

    # Game loop
    while True:
        # Print the grid
        print_grid(grid)

        # Get the player's guess
        guess = input("Enter your guess (e.g., 1,1): ")

        # Convert the guess to row and column indices
        # Add code here to convert the guess to row and column indices
        guess = guess.split(',')
        row = int(guess[0])
        col = int(guess[1])

        # Check the guess
        result = check_guess(grid, row, col)

        # Update the grid with the guess result
        update_grid(grid, row, col, result)

        # Check if the game is over
        if check_game_over(grid):
            print("Congratulations! You sank all the ships!")
            break

print_grid(create_grid(10,10))
# Start the game
play_battleships()
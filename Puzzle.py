# Initialize the 9x9 two-dimensional array
"""
puzzle = [
    [5, 3, 3, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
"""
puzzle = [ [ 7, 9, 9, 1, 1, 3, 4, 5, 6],
            [ 4, 5, 6, 7, 8, 9, 1, 2, 3],
            [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [ 2, 3, 4, 5, 6, 7, 8, 9, 1],
            [ 5, 6, 7, 8, 9, 1, 2, 3, 4],
            [ 8, 9, 1, 2, 3, 4, 5, 6, 7],
            [ 3, 4, 5, 6, 7, 8, 9, 1, 2],
            [ 6, 7, 8, 9, 1, 2, 3, 4, 5],
            [ 9, 1, 2, 3, 4, 5, 6, 7, 8] ]
# Function to check if a given row is valid
def is_valid_row(row):
    return set(row) == set(range(1, 10))

# Function to check if a given column is valid
def is_valid_column(puzzle, col):
    column = [puzzle[row][col] for row in range(9)]
    return set(column) == set(range(1, 10))

# Function to check if a given 3x3 section is valid
def is_valid_section(puzzle, row, col):
    section = []
    for i in range(3):
        for j in range(3):
            section.append(puzzle[row+i][col+j])
    return set(section) == set(range(1, 10))

# Display the puzzle in a readable format
for row in puzzle:
    print(row)

# Check each row and print the result
for i, row in enumerate(puzzle):
    if is_valid_row(row):
        print(f"Row {i+1}: Valid")
    else:
        print(f"Row {i+1}: Invalid")

# Check each column and print the result
for i in range(9):
    if is_valid_column(puzzle, i):
        print(f"Column {i+1}: Valid")
    else:
        print(f"Column {i+1}: Invalid")

# Check each section and print the result
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        if is_valid_section(puzzle, i, j):
            print(f"Section {i//3+1}-{j//3+1}: Valid")
        else:
            print(f"Section {i//3+1}-{j//3+1}: Invalid")
with open('input.txt', 'r') as file:
    maze = [list(line.strip()) for line in file.readlines()]

rows = len(maze)
cols = len(maze[0])

print(f"Word puzzle has {cols} columns and {rows} rows.")

count = 0

def check_right(row: int, col: int) -> bool:
    return cols - col > 3 and \
        maze[row][col + 1] == "M" and \
        maze[row][col + 2] == "A" and \
        maze[row][col + 3] == "S" \
        
def check_right_up(row: int, col: int) -> bool:
    return cols - col > 3 and row > 3 and \
        maze[row - 1][col + 1] == "M" and \
        maze[row - 2][col + 2] == "A" and \
        maze[row - 3][col + 3] == "S" \

def check_up(row: int, col: int) -> bool:
    return row > 3 and \
        maze[row - 1][col] == "M" and \
        maze[row - 2][col] == "A" and \
        maze[row - 3][col] == "S" \

def check_left_up(row: int, col: int) -> bool:
    return col > 3 and row > 3 and \
        maze[row - 1][col - 1] == "M" and \
        maze[row - 2][col - 2] == "A" and \
        maze[row - 3][col - 3] == "S" \
        
def check_left(row: int, col: int) -> bool:
    return col > 3 and \
        maze[row][col - 1] == "M" and \
        maze[row][col - 2] == "A" and \
        maze[row][col - 3] == "S" \

def check_left_down(row: int, col: int) -> bool:
    return col > 3 and rows - row > 3 and \
        maze[row + 1][col - 1] == "M" and \
        maze[row + 2][col - 2] == "A" and \
        maze[row + 3][col - 3] == "S" \
        
def check_down(row: int, col: int) -> bool:
    return rows - row > 3 and \
        maze[row + 1][col] == "M" and \
        maze[row + 2][col] == "A" and \
        maze[row + 3][col] == "S" \

def check_right_down(row: int, col: int) -> bool:
    return cols - col > 3 and rows - row > 3 and \
        maze[row + 1][col + 1] == "M" and \
        maze[row + 2][col + 2] == "A" and \
        maze[row + 3][col + 3] == "S" \

def check_position(row: int, col: int) -> int:
    found = 0
    
    found += 1 if check_right(row, col) else 0
    found += 1 if check_up(row, col) else 0
    found += 1 if check_left(row, col) else 0
    found += 1 if check_down(row, col) else 0

    found += 1 if check_right_up(row, col) else 0
    found += 1 if check_right_down(row, col) else 0
    found += 1 if check_left_up(row, col) else 0
    found += 1 if check_left_down(row, col) else 0

    return found

for row_index, row in enumerate(maze):
    for col_index, char in enumerate(row):
        if char == 'X':
            count += check_position(row_index, col_index)

print(f"'XMAS' was found {count} times.")

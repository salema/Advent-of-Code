WORD_LENGTH = len('XMAS') - 1 # Only the 'MAS' part of XMAS

def check_right(maze: list[list[str]], row: int, col: int) -> bool:
    return len(maze[0]) - col > WORD_LENGTH and \
        maze[row][col + 1] == "M" and \
        maze[row][col + 2] == "A" and \
        maze[row][col + 3] == "S" \
        
def check_right_up(maze: list[list[str]], row: int, col: int) -> bool:
    return len(maze[0]) - col > WORD_LENGTH and row >= WORD_LENGTH and \
        maze[row - 1][col + 1] == "M" and \
        maze[row - 2][col + 2] == "A" and \
        maze[row - 3][col + 3] == "S" \

def check_up(maze: list[list[str]], row: int, col: int) -> bool:
    return row >= WORD_LENGTH and \
        maze[row - 1][col] == "M" and \
        maze[row - 2][col] == "A" and \
        maze[row - 3][col] == "S" \

def check_left_up(maze: list[list[str]], row: int, col: int) -> bool:
    return col >= WORD_LENGTH and row >= WORD_LENGTH and \
        maze[row - 1][col - 1] == "M" and \
        maze[row - 2][col - 2] == "A" and \
        maze[row - 3][col - 3] == "S" \
        
def check_left(maze: list[list[str]], row: int, col: int) -> bool:
    return col >= WORD_LENGTH and \
        maze[row][col - 1] == "M" and \
        maze[row][col - 2] == "A" and \
        maze[row][col - 3] == "S" \

def check_left_down(maze: list[list[str]], row: int, col: int) -> bool:
    return col >= WORD_LENGTH and len(maze) - row > WORD_LENGTH and \
        maze[row + 1][col - 1] == "M" and \
        maze[row + 2][col - 2] == "A" and \
        maze[row + 3][col - 3] == "S" \
        
def check_down(maze: list[list[str]], row: int, col: int) -> bool:
    return len(maze) - row > WORD_LENGTH and \
        maze[row + 1][col] == "M" and \
        maze[row + 2][col] == "A" and \
        maze[row + 3][col] == "S" \

def check_right_down(maze: list[list[str]], row: int, col: int) -> bool:
    return len(maze[0]) - col > WORD_LENGTH and len(maze) - row > WORD_LENGTH and \
        maze[row + 1][col + 1] == "M" and \
        maze[row + 2][col + 2] == "A" and \
        maze[row + 3][col + 3] == "S" \

def check_position(maze: list[list[str]], row: int, col: int) -> int:
    found = 0
    
    found += 1 if check_right(maze, row, col) else 0
    found += 1 if check_up(maze, row, col) else 0
    found += 1 if check_left(maze, row, col) else 0
    found += 1 if check_down(maze, row, col) else 0
    
    found += 1 if check_right_up(maze, row, col) else 0
    found += 1 if check_right_down(maze, row, col) else 0
    found += 1 if check_left_up(maze, row, col) else 0
    found += 1 if check_left_down(maze, row, col) else 0
    
    return found

def count_xmas(filename: str) -> int:
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]

    rows = len(maze)
    cols = len(maze[0])

    print(f"Word puzzle in file {filename} has {rows} rows and {cols} columns.")

    count = 0

    for row_index, row in enumerate(maze):
        for col_index, char in enumerate(row):
            if char == 'X':
                print(f"At position {row_index+1},{col_index+1} is a 'X'.")
                result = check_position(maze, row_index, col_index)
                print(f"Found {result} occurrences of 'XMAS'!")
                count += result

    return count

assert(count_xmas('test_simple.txt') == 7)
assert(count_xmas('test_star.txt') == 8)
assert(count_xmas('sample.txt') == 18)

print(f"'XMAS' was found {count_xmas('input.txt')} times.")

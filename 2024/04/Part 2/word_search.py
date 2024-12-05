def check_forward(maze: list[list[str]], row: int, col: int) -> bool:
    return maze[row + 1][col - 1] == "M" and \
        maze[row - 1][col - 1] == "M" and \
        maze[row + 1][col + 1] == "S" and \
        maze[row - 1][col + 1] == "S"

def check_backward(maze: list[list[str]], row: int, col: int) -> bool:
    return maze[row + 1][col - 1] == "S" and \
        maze[row - 1][col - 1] == "S" and \
        maze[row + 1][col + 1] == "M" and \
        maze[row - 1][col + 1] == "M"

def check_up(maze: list[list[str]], row: int, col: int) -> bool:
    return maze[row + 1][col - 1] == "M" and \
        maze[row - 1][col - 1] == "S" and \
        maze[row + 1][col + 1] == "M" and \
        maze[row - 1][col + 1] == "S"

def check_down(maze: list[list[str]], row: int, col: int) -> bool:
    return maze[row + 1][col - 1] == "S" and \
        maze[row - 1][col - 1] == "M" and \
        maze[row + 1][col + 1] == "S" and \
        maze[row - 1][col + 1] == "M"
        
def check_position(maze: list[list[str]], row: int, col: int) -> bool:
    return check_forward(maze, row, col) or check_backward(maze, row, col) or \
        check_up(maze, row, col) or check_down(maze, row, col)

def count_xmas(filename: str) -> int:
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]

    rows = len(maze)
    cols = len(maze[0])

    print(f"Word puzzle in file {filename} has {rows} rows and {cols} columns.")

    count = 0

    for row_index, row in enumerate(maze):
        for col_index, char in enumerate(row):
            if char == 'A':
                if row_index == 0 or col_index == 0 or \
                    row_index == len(maze) - 1 or col_index == len(maze[0]) - 1:
                    continue
                print(f"At position {row_index+1},{col_index+1} is an 'A'.")
                result = 1 if check_position(maze, row_index, col_index) else 0
                print(f"Found {result} occurrences of 'X-MAS'!")
                count += result

    return count

assert(count_xmas('test_simple.txt') == 1)
assert(count_xmas('sample.txt') == 9)

print(f"'X-MAS' was found {count_xmas('input.txt')} times.")


def find_initial_position(maze: list[list[str]]) -> tuple[int, int]:
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == '^':
                return (row, col)

def move(maze: list[list[str]], position: tuple[int, int], direction: str) -> tuple[str, int, int]:
    # Leave current position
    maze[position[0]][position[1]] = '.'                
    
    # Move
    match(direction):
        case 'u':
            if maze[position[0] - 1][position[1]] != '#':
                return ('u', position[0] - 1, position[1])
            else:
                return ('r', position[0], position[1] + 1)
        case 'r':
            if maze[position[0]][position[1] + 1] != '#':
                return ('r', position[0], position[1] + 1)
            else:
                return ('d', position[0] + 1, position[1])
        case 'd':
            if maze[position[0] + 1][position[1]] != '#':
                return ('d', position[0] + 1, position[1])
            else:
                return ('l', position[0], position[1] - 1)
        case 'l':
            if maze[position[0]][position[1] - 1] != '#':
                return ('l', position[0], position[1] - 1)
            else:
                return ('u', position[0] - 1, position[1])
    
    return ('u', 0, 0)

def count_fields(filename: str) -> int:
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]

    rows = len(maze)
    cols = len(maze[0])

    print(f"The maze in file '{filename}' has {rows} rows and {cols} columns.")

    position = find_initial_position(maze)
    direction = 'u'
    print(f"Guard found at position {position}")
    fields_visited = set()
    fields_visited.add(position)

    while position[0] >= 0 and position[0] < rows - 1 and position[1] >= 0 and position[1] < cols - 1:
        movement = move(maze, position, direction)
        direction = movement[0]
        position = (movement[1], movement[2])

        print(f"Moved to field {position}")
        fields_visited.add(position)
        print(f"Field count: {len(fields_visited)}")
    
    return len(fields_visited)


assert(count_fields('sample.txt') == 41)
print(f"The guard visited {count_fields('input.txt')} of {rows * cols} possible fields before leaving the maze.")

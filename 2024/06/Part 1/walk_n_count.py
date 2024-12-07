OBSTACLE = '#'

def find_initial_position(maze: list[list[str]]) -> tuple[int, int]:
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == '^':
                return (row, col)

def move(maze: list[list[str]], position: tuple[int, int], direction: str) -> tuple[str, int, int]:
    match(direction):
        case 'north':
            if maze[position[0] - 1][position[1]] != OBSTACLE:
                return ('north', position[0] - 1, position[1])
            else:
                return ('east', position[0], position[1] + 1)
        case 'east':
            if maze[position[0]][position[1] + 1] != OBSTACLE:
                return ('east', position[0], position[1] + 1)
            else:
                return ('south', position[0] + 1, position[1])
        case 'south':
            if maze[position[0] + 1][position[1]] != OBSTACLE:
                return ('south', position[0] + 1, position[1])
            else:
                return ('west', position[0], position[1] - 1)
        case 'west':
            if maze[position[0]][position[1] - 1] != OBSTACLE:
                return ('west', position[0], position[1] - 1)
            else:
                return ('north', position[0] - 1, position[1])

def count_fields(filename: str) -> int:
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]

    rows = len(maze)
    cols = len(maze[0])

    print(f"The maze in file '{filename}' has {rows} rows and {cols} columns.")

    direction = 'north'
    position = find_initial_position(maze)
    print(f"Guard found at position {position} facing {direction}")

    fields_visited = set()
    fields_visited.add(position)

    while position[0] > 0 and position[0] < rows - 1 and position[1] > 0 and position[1] < cols - 1:
        movement = move(maze, position, direction)
        direction = movement[0]
        position = (movement[1], movement[2])

        fields_visited.add(position)
    
    return len(fields_visited)

assert(count_fields('sample.txt') == 41)
print(f"The guard visited {count_fields('input.txt')} different fields before leaving the maze.")

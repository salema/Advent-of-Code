EMPTY = '.'
OBSTACLE = '#'

def show_maze(maze: list[list[str]]):
    for row in range(len(maze)):
        print(maze[row])
    
    print("")
            
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
                return ('east', position[0], position[1])
        case 'east':
            if maze[position[0]][position[1] + 1] != OBSTACLE:
                return ('east', position[0], position[1] + 1)
            else:
                return ('south', position[0], position[1])
        case 'south':
            if maze[position[0] + 1][position[1]] != OBSTACLE:
                return ('south', position[0] + 1, position[1])
            else:
                return ('west', position[0], position[1])
        case 'west':
            if maze[position[0]][position[1] - 1] != OBSTACLE:
                return ('west', position[0], position[1] - 1)
            else:
                return ('north', position[0], position[1])

def detect_loop(maze: list[list[str]]) -> bool:
    direction = 'north'
    position = find_initial_position(maze)
    status = (direction, position[0], position[1])
    
    is_in_loop = False
    states_seen = set()
    states_seen.add(status)
   
    while position[0] > 0 and position[0] < len(maze) - 1 and \
          position[1] > 0 and position[1] < len(maze[0]) - 1 and not is_in_loop:
        status = move(maze, position, direction)
        direction = status[0]
        position = (status[1], status[2])

        is_in_loop = status in states_seen
        states_seen.add(status)        
    
    return is_in_loop

def count_loop_options(filename: str):
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]
    
    option_count = 0
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == EMPTY:
                maze[row][col] = OBSTACLE
                if detect_loop(maze):
                    print(f"Loop detected with obstacle at row {row + 1}, col {col + 1}.")
                    # show_maze(maze)
                    option_count += 1

                maze[row][col] = EMPTY # Restore original input
    
    return option_count    

assert(count_loop_options('sample.txt') == 6)
print(f"There are {count_loop_options('input.txt')} options to place an extra obstacle.")

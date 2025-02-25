from queue import Queue, PriorityQueue
import time

def load_map_from_file(filename):
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f.readlines() if len(line.strip()) > 0]

def find_start(map_grid):
    for row in range(len(map_grid)):
        for col in range(len(map_grid[row])):
            if map_grid[row][col] == 's':
                return row, col
    return None

def find_goal(map_grid):
    for row in range(len(map_grid)):
        for col in range(len(map_grid[row])):
            if map_grid[row][col] == 'D':
                return row, col
    return None

def get_neighbors(map_grid, position):
    row, col = position
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(map_grid) and 0 <= nc < len(map_grid[0]) and map_grid[nr][nc] != '*':
            neighbors.append((nr, nc))
    return neighbors

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

def bfs(map_grid, start, goal):
    start_time = time.time()
    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}
    iterations = 0

    while not frontier.empty():
        current = frontier.get()
        iterations += 1
        if current == goal:
            return reconstruct_path(came_from, start, goal), iterations, time.time() - start_time

        for neighbor in get_neighbors(map_grid, current):
            if neighbor not in came_from:
                frontier.put(neighbor)
                came_from[neighbor] = current

    return None, iterations, time.time() - start_time

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_search(map_grid, start, goal):
    start_time = time.time()
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    iterations = 0

    while not frontier.empty():
        _, current = frontier.get()
        iterations += 1
        if current == goal:
            return reconstruct_path(came_from, start, goal), iterations, time.time() - start_time

        for neighbor in get_neighbors(map_grid, current):
            if neighbor not in came_from:
                priority = heuristic(neighbor, goal)
                frontier.put((priority, neighbor))
                came_from[neighbor] = current

    return None, iterations, time.time() - start_time

def astar(map_grid, start, goal):
    start_time = time.time()
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    iterations = 0

    while not frontier.empty():
        _, current = frontier.get()
        iterations += 1
        if current == goal:
            return reconstruct_path(came_from, start, goal), iterations, time.time() - start_time

        for neighbor in get_neighbors(map_grid, current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                frontier.put((priority, neighbor))
                came_from[neighbor] = current

    return None, iterations, time.time() - start_time

# Load large maps
large_maps = [
    ("Cave Maps/cave300x300", (2, 2), (295, 257)),
    ("Cave Maps/cave600x600", (2, 2), (598, 595)),
    ("Cave Maps/cave900x900", (2, 2), (898, 895))
]

for filename, start, goal in large_maps:
    map_grid = load_map_from_file(filename)
    print(f"\nTesting {filename}")
    
    path, iterations, exec_time = bfs(map_grid, start, goal)
    print(f"BFS: Path Length: {len(path)}, Iterations: {iterations}, Time: {exec_time:.4f}s")
    
    path, iterations, exec_time = greedy_search(map_grid, start, goal)
    print(f"Greedy: Path Length: {len(path)}, Iterations: {iterations}, Time: {exec_time:.4f}s")
    
    path, iterations, exec_time = astar(map_grid, start, goal)
    print(f"A*: Path Length: {len(path)}, Iterations: {iterations}, Time: {exec_time:.4f}s")

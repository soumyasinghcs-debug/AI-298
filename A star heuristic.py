import heapq

def get_manhattan_distance(state, goal):
    """Calculates sum of Manhattan distances of tiles from their goal positions (ignoring 0)."""
    distance = 0
    
    goal_coords = {val: (i, j) for i, row in enumerate(goal) for j, val in enumerate(row)}
    
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0:
                gr, gc = goal_coords[val]
                distance += abs(r - gr) + abs(c - gc)
    return distance

def find_zero(state):
    """Finds the row and column index of the blank space (0)."""
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c

def get_neighbors(state):
    """Generates valid adjacent states by sliding a tile into the blank space."""
    neighbors = []
    r, c = find_zero(state)
    
   
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            
            new_state = [list(row) for row in state]
           
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def astar_8_puzzle(start, goal):
 
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
            
        for neighbor in get_neighbors(current):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + get_manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
                
    return None

def get_user_state(state_name):
    print(f"Enter the numbers for the {state_name} (0-8, where 0 is blank).")
    print("Provide them row by row, separated by spaces (e.g., '1 2 3' then Enter):")
    state = []
    for i in range(3):
        while True:
            try:
                row_input = input(f"Row {i+1}: ").split()
                row = tuple(int(x) for x in row_input)
                if len(row) == 3 and all(0 <= x <= 8 for x in row):
                    state.append(row)
                    break
                else:
                    print("Invalid input. Please enter exactly 3 numbers between 0 and 8 separated by spaces.")
            except ValueError:
                print("Invalid input. Please enter integers only.")
    return tuple(state)


start_state = get_user_state("Initial State")
goal_state = get_user_state("Goal State")

path = astar_8_puzzle(start_state, goal_state)

print("\nStart State:")
for row in start_state: print(row)
print("\nGoal State:")
for row in goal_state: print(row)

if path:
    print(f"\nSolution found in {len(path) - 1} steps!")
    for idx, state in enumerate(path):
        print(f"\nStep {idx}:")
        for row in state:
            print(row)
else:
    print("\nNo solution possible.")
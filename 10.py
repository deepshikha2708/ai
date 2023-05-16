def get_input():
    # Take input for the initial state
    initial_state = {}
    while True:
        block_name = input("Enter block name (or 'done' to finish): ")
        if block_name == 'done':
            break
        block_on_top = input("Enter name of block on top (or 'None' if none): ")
        initial_state[block_name] = block_on_top if block_on_top != 'None' else None
    
    # Take input for the goal state
    goal_state = {}
    while True:
        block_name = input("Enter block name (or 'done' to finish): ")
        if block_name == 'done':
            break
        block_on_top = input("Enter name of block on top (or 'None' if none): ")
        goal_state[block_name] = block_on_top if block_on_top != 'None' else None
    
    return initial_state, goal_state

# Define the actions that can be taken in the block world
actions = [
    ('move', 'A', 'B'),
    ('move', 'A', 'C'),
    ('move', 'B', 'A'),
    ('move', 'B', 'C'),
    ('move', 'C', 'A'),
    ('move', 'C', 'B')
]

# Define a function to apply an action to a state and return the new state
def apply_action(state, action):
    new_state = state.copy()
    if action[0] == 'move' and new_state[action[1]] is not None and new_state[action[2]] is None:
        new_state[action[2]] = new_state[action[1]]
        new_state[action[1]] = None
        return new_state
    else:
        return None

# Define a function to check if a state is the goal state
def is_goal_state(state, goal_state):
    return state == goal_state

# Define a function to perform a depth-first search to find a solution
def dfs_search(initial_state, goal_state):
    stack = [(initial_state, [])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if is_goal_state(state, goal_state):
            return path
        visited.add(str(state))
        for action in actions:
            new_state = apply_action(state, action)
            if new_state is not None and str(new_state) not in visited:
                stack.append((new_state, path + [action]))
    return None

# Get user input for the initial and goal states
initial_state, goal_state = get_input()

# Perform the depth-first search to find a solution and print the path
path = dfs_search(initial_state, goal_state)
if path is not None:
    for action in path:
        print(action)
else:
    print("No solution found.")

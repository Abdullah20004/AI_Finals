GRID_SIZE = 5
DISCOUNT_FACTOR = 0
actions = ["Up", "Down", "Right", "Left"]

def next_state(state, action):
    """Calculates the next state given the current state and action."""
    x, y = state
    if action == "Up" and x > 0:
        return (x - 1, y)
    elif action == "Down" and x < GRID_SIZE - 1:
        return (x + 1, y)
    elif action == "Right" and y < GRID_SIZE - 1:
        return (x, y + 1)
    elif action == "Left" and y > 0:
        return (x, y - 1)
    
    return state

def manhattan_distance(state, goal_state=(GRID_SIZE - 1, GRID_SIZE - 1)):
    """
    Calculates Manhattan distance from any state to the goal state.
    """
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

def reward_function(current_state, previous_state):
    """
    Calculates immediate reward dynamically.
    Reward = +1 if closer to the goal, -1 if moving away.
    """
    goal_state = (GRID_SIZE - 1, GRID_SIZE - 1)

    if current_state == goal_state:
        return 10

    prev_distance = manhattan_distance(previous_state, goal_state)
    current_distance = manhattan_distance(current_state, goal_state)

    if current_distance < prev_distance:
        reward = 1
    elif current_distance > prev_distance:
        reward = -1
    else:
        reward = 0

    return reward

def simulate_robot():
    """
    Simulate the robot by determining the best action to take and calcualte the required steps to reach the goal.
    """
    current_state = (0, 0)
    goal_state = (GRID_SIZE - 1, GRID_SIZE - 1)

    steps = 0
    while current_state != goal_state:
        best_action = None
        best_reward = float('-inf')

        for action in actions:
            next_s = next_state(current_state, action)
            reward = reward_function(next_s, current_state)
            expected_value = reward + DISCOUNT_FACTOR * manhattan_distance(next_s, goal_state)

            if expected_value > best_reward:
                best_reward = expected_value
                best_action = action

        print(f"Current State: {current_state}, Taking action: {best_action}, Reward: {best_reward}")
        current_state = next_state(current_state, best_action)
        steps += 1

    print(f"Agent reached the goal at state: {current_state} in {steps} steps")

simulate_robot()


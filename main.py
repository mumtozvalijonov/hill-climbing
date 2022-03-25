from numpy import random


objective_function = lambda x: 2 - x**2
INITIAL_STEP_SIZE = 0.5
LOWER_BOUNDARY = -5
UPPER_BOUNDARY = 5
STEP_DECAY_FACTOR = 0.9
MAX_STEPS_WITHOUT_IMPROVEMENT = 100


def main():
    x = random.uniform(LOWER_BOUNDARY, UPPER_BOUNDARY)
    state_value = objective_function(x)
    step_size = INITIAL_STEP_SIZE
    steps_without_improvement = 0

    while True:
        x_left = x - step_size
        x_right = x + step_size

        left_value = objective_function(x_left)
        right_value = objective_function(x_right)

        if left_value > state_value and left_value > right_value:
            x = x_left
            state_value = left_value
        elif right_value > state_value and right_value > left_value:
            x = x_right
            state_value = right_value
        else:
            steps_without_improvement += 1
            step_size *= STEP_DECAY_FACTOR
            if steps_without_improvement == MAX_STEPS_WITHOUT_IMPROVEMENT:
                break
        print(f"X: {x}. State: {state_value}")
    print()
    print(f"Result:\nXmax: {x}. Smax: {state_value}")
    

if __name__ == '__main__':
    main()

from collections import deque

BUCKET_ONE = 'one'
BUCKET_TWO = 'two'

def measure(bucket_one, bucket_two, goal, start_bucket):
    water_one, water_two = 0, 0
    for _ in range(1):
        if start_bucket == BUCKET_ONE:
            water_one, water_two = bucket_one, 0
            break
        if start_bucket == BUCKET_TWO:
            water_one, water_two = 0, bucket_two
            break
        raise ValueError('invalid start bucket')

    actions_count = 1

    if water_one == goal:
        return (actions_count, BUCKET_ONE, water_two)
    if water_two == goal:
        return (actions_count, BUCKET_TWO, water_one)

    queue = deque()
    queue.append((water_one, water_two, actions_count))
    visited = set()
    visited.add((water_one, water_two))

    while queue:
        water_one, water_two, actions_count = queue.popleft()

        next_states = []

        if water_one < bucket_one:
            next_states.append((bucket_one, water_two, actions_count + 1))
        if water_two < bucket_two:
            next_states.append((water_one, bucket_two, actions_count + 1))
        if water_one > 0:
            next_states.append((0, water_two, actions_count + 1))
        if water_two > 0:
            next_states.append((water_one, 0, actions_count + 1))
        if water_one > 0 and water_two < bucket_two:
            pour = min(water_one, bucket_two - water_two)
            next_states.append((water_one - pour, water_two + pour, actions_count + 1))
        if water_two > 0 and water_one < bucket_one:
            pour = min(water_two, bucket_one - water_one)
            next_states.append((water_one + pour, water_two - pour, actions_count + 1))

        for new_water_one, new_water_two, new_actions_count in next_states:
            if start_bucket == BUCKET_ONE:
                if new_water_one == 0 and new_water_two == bucket_two:
                    continue
            if start_bucket == BUCKET_TWO:
                if new_water_two == 0 and new_water_one == bucket_one:
                    continue

            if new_water_one == goal:
                return (new_actions_count, BUCKET_ONE, new_water_two)
            if new_water_two == goal:
                return (new_actions_count, BUCKET_TWO, new_water_one)

            if (new_water_one, new_water_two) not in visited:
                visited.add((new_water_one, new_water_two))
                queue.append((new_water_one, new_water_two, new_actions_count))

    raise ValueError('A meaningful error message here.')


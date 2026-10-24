
from collections import deque

initial = (1, 2, 3,
           4, 0, 6,
           7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row, col = blank // 3, blank % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            board = list(state)

            board[blank], board[new_pos] = (
                board[new_pos], board[blank]
            )

            neighbors.append(tuple(board))

    return neighbors


def solve(initial):
    queue = deque([initial])
    parent = {initial: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor in get_neighbors(current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    return None


def print_board(state):
    for i in range(0, 9, 3):
        print(*("_" if x == 0 else x for x in state[i:i+3]))
    print()


if __name__ == "__main__":
    solution = solve(initial)

    if solution:
        print("Solution found!")
        print("Number of moves:", len(solution) - 1)

        for step, state in enumerate(solution):
            print("Step", step)
            print_board(state)
    else:
        print("No solution exists.")

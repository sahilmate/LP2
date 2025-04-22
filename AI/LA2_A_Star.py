g = 0  # Move counter

def print_board(elements):
    for i in range(9):
        if i % 3 == 0:
            print()
        if elements[i] == -1:
            print("_", end=" ")
        else:
            print(elements[i], end=" ")
    print()

def solvable(start):
    inv = 0
    for i in range(9):
        if start[i] == -1:
            continue
        for j in range(i + 1, 9):
            if start[j] == -1:
                continue
            if start[i] > start[j]:
                inv += 1
    return inv % 2 == 0  # A puzzle is solvable if inversions are even

def heuristic(start, goal):
    global g
    h = 0
    for i in range(9):
        if start[i] != -1:
            j = goal.index(start[i])  # Find index of the current tile in the goal
            h += (abs(j - i) // 3) + (abs(j - i) % 3)  # Manhattan Distance
    return h + g

def moveleft(start, position):
    start[position], start[position - 1] = start[position - 1], start[position]

def moveright(start, position):
    start[position], start[position + 1] = start[position + 1], start[position]

def moveup(start, position):
    start[position], start[position - 3] = start[position - 3], start[position]

def movedown(start, position):
    start[position], start[position + 3] = start[position + 3], start[position]

def movetile(start, goal, visited):
    emptyat = start.index(-1)
    row, col = emptyat // 3, emptyat % 3
    t1, t2, t3, t4 = start[:], start[:], start[:], start[:]
    f1, f2, f3, f4 = float('inf'), float('inf'), float('inf'), float('inf')

    if col - 1 >= 0:  # Move left
        moveleft(t1, emptyat)
        if tuple(t1) not in visited:
            f1 = heuristic(t1, goal)

    if col + 1 < 3:  # Move right
        moveright(t2, emptyat)
        if tuple(t2) not in visited:
            f2 = heuristic(t2, goal)

    if row + 1 < 3:  # Move down
        movedown(t3, emptyat)
        if tuple(t3) not in visited:
            f3 = heuristic(t3, goal)

    if row - 1 >= 0:  # Move up
        moveup(t4, emptyat)
        if tuple(t4) not in visited:
            f4 = heuristic(t4, goal)

    # Select the best move
    min_heuristic = min(f1, f2, f3, f4)
    
    if min_heuristic == float('inf'):
        return False  # No valid move available (shouldn't happen)

    if f1 == min_heuristic:
        moveleft(start, emptyat)
    elif f2 == min_heuristic:
        moveright(start, emptyat)
    elif f3 == min_heuristic:
        movedown(start, emptyat)
    elif f4 == min_heuristic:
        moveup(start, emptyat)

    return True

def solveEight(start, goal, visited):
    global g
    g += 1
    visited.add(tuple(start))  # Store visited states

    print_board(start)
    f = heuristic(start, goal)
    
    if f == g:  # Solution reached
        print("Solved in {} moves".format(f))
        return True

    if not movetile(start, goal, visited):  # If no valid move
        return False
    
    return solveEight(start, goal, visited)  # Recursively solve

def main():
    global g
    g = 0  # Reset move counter
    start, goal = [], []

    print("Enter the start state (Enter -1 for empty):")
    for _ in range(9):
        start.append(int(input()))

    print("Enter the goal state (Enter -1 for empty):")
    for _ in range(9):
        goal.append(int(input()))

    print("\nInitial Board:")
    print_board(start)

    if solvable(start):
        visited = set()
        if solveEight(start, goal, visited):
            print("Solved in {} moves".format(g))
        else:
            print("Solution not found.")
    else:
        print("Not possible to solve")

if __name__ == "__main__":
    main()
    

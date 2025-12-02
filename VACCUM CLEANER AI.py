import math

grid = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

vacuum_pos = [0, 0]

def print_grid():
    for row in grid:
        print(row)
    print()

def find_dirty_cells():
    dirty = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 1:
                dirty.append((i, j))
    return dirty

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def clean():
    print("Initial grid:")
    print_grid()

    while True:
        dirty = find_dirty_cells()
        if not dirty:
            print("All cells cleaned!")
            break

        nearest = min(dirty, key=lambda c: distance(vacuum_pos, c))
        print(f"Moving from {vacuum_pos} to {nearest}")
        
        vacuum_pos[0], vacuum_pos[1] = nearest
        grid[nearest[0]][nearest[1]] = 0
        
        print("Cleaned cell:", nearest)
        print_grid()

clean()

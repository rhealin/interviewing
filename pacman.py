'''
Given a 2D grid with points in it, find the maximum points that the player can achieve.
Player can move only up, up-left, up-right in the grid. Player always starts
from bottom-most row and middle column


points_grid = [
    [9, 7, 10, 10],
    [2, 7, 9, 10],
    [0, 6, 2, 3],
    [1, 0, 2, 0],
]

start_x = 3 # m - 1
start_y = 2 # floor(n / 2)

2 -> 6 -> 2 -> 9 is one possible path with number of points gained 19
'''

def find_max_points(points_grid):
    m = len(points_grid)
    n = len(points_grid[0])
    
    for i in range(2, m+1):
        for j in range(n):
            if valid_point(i, j, n):
                points_grid[-i][j] += max_prev_value(i, j)
    
    max_value = 0
    for x in range(n):
        if valid_point(m+1, j):
            max_value = max(points_grid[-(m+1)][j], max_value)

    return max_value
            
def valid_point(i, j, n):
    if j < 0 or j > n - 1:
        return False
    return abs(j-floor(n/2)) < i

def max_prev_value(i, j):
    max_value = 0
    prev_row = i - 1
    if valid_point(prev_row, j-1):
        max_value = max(points_grid[-(prev_row)][j-1], max_value)
    if valid_point(prev_row, j):
        max_value = max(points_grid[-(prev_row)][j], max_value)
    if valid_point(prev_row, j+1):
        max_value = max(points_grid[-(prev_row)][j+1], max_value)
    return max_value



        
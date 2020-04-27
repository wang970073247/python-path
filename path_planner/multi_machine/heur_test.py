import numpy as np

def get_heuristic(x_dim, y_dim, point):
    heuristic = np.zeros((x_dim, y_dim))
    for row in range(x_dim):
        for col in range(y_dim):
            heuristic[row][col] = abs(point[0] - row) + abs(point[1] - col)

    return heuristic

def get_heuristic2(start, goal):
    x_dim = goal[0] - start[0]
    y_dim = goal[1] - start[1]

    heuristic = np.zeros((x_dim, y_dim))
    for row in range(x_dim):
        for col in range(y_dim):
            heuristic[row][col] = abs(goal[0] - row) + abs(goal[1] - col)

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
point1 = [9, 9]
heur1 = get_heuristic(10, 10, point1)

for row in heur1:
    print(row)

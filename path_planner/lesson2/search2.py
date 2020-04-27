#!/usr/bin/env python

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
delta = [[-1, 0],
         [0, -1],
         [1, 0],
         [0, 1]]

delta_name = ['^', '<', 'v', '>'] 
cost = 1

def search(grid, init, goal, cost):
    closed = [[0] * len(grid[0]) for i in grid]
    closed[init[0]][init[1]] = 1
    action = [[-1] * len(grid[0]) for i in grid]
    x = init[0]
    y = init[1]
    g = 0
    open = [[g, x, y]]
    found = False
    resign = False
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            next = open.pop(0)
            g = next[0]
            x = next[1]
            y = next[2]
            if x == goal[0] and y == goal[1]:
                found = True 
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
    
    policy = [[' '] * len(grid[0]) for i in grid]
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'
    while x != init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        policy[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2
    for row in policy:
        print (row)

    print('-----------------')
    for row in action:
        print (row)

    print('-----------------')
    for row in closed:
        print (row)

    return policy

search(grid, init, goal, cost)
#print(search())

#!/usr/bin/env python
import numpy as np
'''
grid = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        ]

heuristic = [[18, 17, 16, 15, 14, 13, 12, 11, 10, 9],
             [17, 16, 15, 14, 13, 12, 11, 10, 9,  8],
             [16, 15, 14, 13, 12, 11, 10, 9,  8,  7],
             [15, 14, 13, 12, 11, 10, 9,  8,  7,  6],
             [14, 13, 12, 11, 10, 9,  8,  7,  6,  5],
             [13, 12, 11, 10, 9,  8,  7,  6,  5,  4],
             [12, 11, 10, 9,  8,  7,  6,  5,  4,  3],
             [11, 10, 9,  8,  7,  6,  5,  4,  3,  2],
             [10, 9,  8,  7,  6,  5,  4,  3,  2,  1],
             [9,  8,  7,  6,  5,  4,  3,  2,  1,  0],
            ]
'''

def show(m):
    for row in m:
        for i in row:
#            if(i == 0):
#                i = ' '
            print('%3s' % str(i), end=',')
        print('', end='\r\n')
    print('----'*len(m[0]))

def color_show(m):
    for row in m:
        for i in row:
            if (type(i) == str):
                print('\033[0;35m%3s\033[0m'% i, end=',')
            elif i == 1:
                print('\033[0;33m%3s\033[0m'% i, end=',')
            else:
                print('%3s' % str(i), end=',')
        print('', end='\r\n')
    print('----'*len(m[0]))    

def get_heuristic(x_dim, y_dim, point):
    heuristic = np.zeros((x_dim, y_dim))
    for row in range(x_dim):
        for col in range(y_dim):
            heuristic[row][col] = abs(point[0] - row) + abs(point[1] - col)

    return heuristic

x_dim = y_dim = 30

#grid = np.zeros((x_dim, y_dim))
grid =  [[0 for col in range(x_dim)] for row in range(y_dim)]
'''
grid = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
'''
init1 = [6, 8]
goal1 = [len(grid)-1, len(grid[0])-1]
init2 = [0, 0]
goal2 = [20, 20]
delta = [[-1, 0], # up
         [0, -1], # left
         [1, 0],  # down
         [0, 1]]  # right

delta_name = ['^', '<', 'v', '>'] 
cost = 1


heuristic1 = get_heuristic(x_dim, y_dim, goal1)
heuristic2 = get_heuristic(x_dim, y_dim, goal2)
#print(heuristic)
def search(grid, init, goal, cost, heuristic):
    closed = [[0] * len(grid[0]) for i in grid]
    closed[init[0]][init[1]] = 1
    action = [[-1] * len(grid[0]) for i in grid]
    expand = [[-1] * len(grid[0]) for i in grid]

    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h
    orientation = 'v'
    open = [[f, h, g, x, y, orientation]]

    found = False
    resign = False
    count = 0
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            next = open.pop(0)
            g = next[2]
            x = next[3]
            y = next[4]
            orientation = next[5]
            expand[x][y] = count
            count += 1

            if x == goal[0] and y == goal[1]:
                found = True 
            else:
                for i in range(len(delta)):
                    next_orientation = delta_name[i]
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            if orientation == next_orientation:
                                cost = 1
                            else:
                                cost = 2
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            open.append([f2, h2, g2,  x2, y2, next_orientation])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
    
    #policy = [[' '] * len(grid[0]) for i in grid]
    policy = grid
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'
    while x != init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        policy[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2
#    return policy    
    color_show(policy)    
    show(expand)

    '''
    for row in policy:
        print (row)
        #print("{:^10d}".format(row))
    
    
    
    print('-----------------')
    for row in action:
        print (row)
    
    print('-----------------')
    for row in expand:
        print (row)
    '''
    #return policy

search(grid, init1, goal1, cost, heuristic1)
search(grid, init2, goal2, cost, heuristic2)
#print(search())

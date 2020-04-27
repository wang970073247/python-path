# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 0, 1], # go down [1,0]
         [ 1, 0]] # go right [0,1]

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1
    
    x = init[0]
    y = init[1]
    g = 0
    
    open = [[g, x, y]]

    found = False
    resign = False
    '''
    print('initial open list')
    for i in range(len(open)):
        print('    {}'.format(open[i]))
    print('--------------')
    '''

    #while found is False and resign is False:
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            '''
            open.sort()
            open.reverse()
            next = open.pop()
            '''
            open.sort()
            next = open.pop(0)
            '''
            next = min(open)
            open.remove(next)
            '''
            #print ('take list item)
            #print next
            g = next[0]
            x = next[1]
            y = next[2]

            if x == goal[0] and y == goal[1]:
                found = True
                print (next)
                print('Search Successful')
                return next

            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1


#search(grid, init, goal, cost)

def search1(grid, init, goal, cost):
    closed = [[0] * len(grid[0]) for i in grid]
    closed[init[0]][init[1]] = 1
    expand = [[-1] * len(grid[0]) for i in grid]
    x = init[0]
    y = init[1]
    g = 0
    open = [[g, x, y]]
    expand[x][y] = g
    count = 0
    found = False
    resign = False
    while not found and not resign:
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            next = open.pop(0)
            g = next[0]
            x = next[1]
            y = next[2]
            #expand[x][y] = count
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            count += 1
                            expand[x2][y2] = count
    
    return expand

print(search1(grid, init, goal, cost))




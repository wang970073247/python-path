import numpy as np

grid = [[0, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0]]

point = [4, 5]

def get_heuristic(x_dim, y_dim, point):
    heuristic = np.zeros((x_dim, y_dim))
    for row in range(x_dim):
        for col in range(y_dim):
            heuristic[row][col] = abs(point[0] - row) + abs(point[1] - col)

    return heuristic

grid = np.zeros((5,5))

a = [8, 18, 28, 38]
b = [9, 19, 29, 39]
c = [8, 18, 28, 40]
d = [8, 18, 29, 36]
e = [8, 17, 30, 35]

a = [[ 1,   1,  '>'],
     [ 1,  '>', '>'],
     ['>', '>', '>']]
def show(m):
    for row in m:
        for i in row:
            print('%3s' % str(i), end=',')
        print('', end='\r\n')

a = 10
b = 'v'
if(type(b) == str):

    print('\033[0;35m%3s\033[0m'% 'v')


print(type(a))
print(type(b))
print(type(a) == int)
print(type(b) == str)
'''
for row in a:
    for i in row:
        print('%3s' % str(i), end=',')
    print('', end='\r\n')

print("{:^10d}".format(3))
'''
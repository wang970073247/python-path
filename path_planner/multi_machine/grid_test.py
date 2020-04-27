import copy

grid = [[0, 0],
        [0, 0]]
m = 0

def fun_test(grid, m):
    b = copy.copy(grid)
    n = m

    b[0][0] += 1
    n += 1

    print(n)
    print(grid)
    print('---------')

fun_test(grid, m)
fun_test(grid, m)


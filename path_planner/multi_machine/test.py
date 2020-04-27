grid = [[0, 0],
        [0, 0]]
m = 0

'''
map = [[0]*2 for i in range(2)]
print(map)
map[0][0] = LandMark((0,0))
'''

def fun_test(grid, m):
    b = grid
    n = m

    b[0][0] += 1
    n += 1

class test_class:
    def __init__(self):
        self.front = 2
        self.back = 1
        self.total = self.front + self.back + 1


for i in range(5,10):
    if i > 10:
        print('fail1')
        break
    else:
        if i % 11 == 0:
            print('fail2')
            break

else:
    print('ok')
print('------1-------')

a = [1,2,3]
b = 3
print(a.index(b))
print('------2-------')

index = 3
print(index)

print('------3-------')
sum = 0
for i in range(4):
    if i > 5:
        for ii in range(i):
            sum += ii
        print(sum)
        break
else:
    print('no')

print('------4-------')
a = 3

if a > 5:
    i5 = 1
if a > 2:
    print(i5)


'''
from land_mark import information_map
a = []
for i in range(5):
    a.append(information_map[1][i])
print('a[0]:', a[0].is_locked)
print('info[1][0]', information_map[1][0].is_locked)

a[0].rewrite_locked_status('locked')

print('a[0]:', a[0].is_locked)
print('info[1][0]', information_map[1][0].is_locked)
'''


orientation_map2 = {'^':[(-1,0)], 'v':[(1,0)], '<':[(0,-1)], '>':[(0,1)], '<^>':[(0,-1),(-1,0),(0,1)],
                    '<v':[(0,-1),(1,0)], 'v^':[(1,0),(-1,0)],'v>':[(1,0),(0,1)], '<^':[(0,-1),(-1,0)], '^>':[(-1,0),(0,1)], '>v':[(1,0),(0,1)],'>^':[(-1,0),(0,1)],
                    'v^>':[(1,0),(-1,0),(0,1)], '<v^':[(0,-1),(1,0),(-1,0)], '<v>':[(0,-1),(1,0),(0,1)]}




#a = [[0] * col_dim] * row_dim



'''
            if car_position_in_route :#agv is now at route[0] 
                self.information_route[0].rewrite_locked_status('locked')
                self.information_route[0].update_passing_car(self.car_num)
                for i in range(1,self.front_locked_length+1):
                    if self.information_route[i].get_locked_status() == 'locked':
                        self.next_action.clear()
                        self.next_action.append('STOP')
                        self.information_route[i].add_waitting_car(self.car_num)
                        break
                    else:
                        self.information_route[i].rewrite_locked_status('locked')
                        self.information_route[i].update_passing_car(self.car_num)
                else:
                    self.next_action.clear()
                    for i in range(1, self.front_locked_length+1):
                        self.next_action.append(self.route_with_orie[i])

            elif p_x == self.route_with_orie[1][0] and p_y == self.route_with_orie[1][1]:#agv is now at route[1]
                if self.information_route[1+self.front_locked_length].get_locked_status() == 'locked':
                    self.next_action.clear()
                    self.next_action.append('STOP')
                else:
                    self.information_route[1+self.front_locked_length].rewrite_locked_status('locked')
                    self.information_route[1+self.front_locked_length].update_passing_car(self.car_num)
                    self.next_action.pop(0)
                    self.next_action.append(self.route_with_orie[1+self.front_locked_length])
'''
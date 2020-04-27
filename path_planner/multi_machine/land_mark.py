
from map import orie2 as orie_grid
from map import orientation_map

cost_value = 1
waitting_cost = 10
x_dim = len(orie_grid)
y_dim = len(orie_grid[0])

class LandMark:
    def __init__(self, coor, traffic_orientation):
        self.coor = coor
        self.traffic_orientation = traffic_orientation
        self.original_orientation = traffic_orientation

        self.is_locked = 'unlocked'
        self.cost_value = cost_value
        self.waitting_car = []
        self.passing_car = None
        self.traffic_status = True
        self.punish_cost = 1

    def get_coordinate(self):
        return self.coor

    def get_traffic_rule(self):
        return self.traffic_orientation

    def get_locked_status(self):
        return self.is_locked

    def get_passing_car_num(self):
        return self.passing_car

    def rewrite_locked_status(self, lock_status):
        '''if landmark is nearby in two need be locked, when car
        is gone need to be unlocked'''
        self.is_locked = lock_status

    def increase_cost(self):
        self.cost_value += self.punish_cost

    def reduce_cost(self):
        self.cost_value -= self.punish_cost

    def get_waitting_car(self):
        return self.waitting_car

    def add_waitting_car(self, car_num):
        self.waitting_car.append(car_num)

    def pop_waitting_car(self):
        self.waitting_car.pop(0)

    def update_passing_car(self, car_num):
        self.passing_car = car_num

    def cal_locked_cost(self, car_coor):
        locked_cost = 0
        distance = abs(car_coor[0]-self.coor[0]) + abs(car_coor[1]-self.coor[1])
        if distance > 10:
            locked_cost = 0
            return locked_cost
        else:
            locked_cost = 20 - (distance - 1) * 2
            return locked_cost

    def get_car_cost(self,car_coor):
        locked_cost = 0
        if self.is_locked == 'locked':
            locked_cost = self.cal_locked_cost(car_coor)

        final_cost = self.cost_value + locked_cost + len(self.waitting_car) * waitting_cost

        return final_cost

    def update_traffic_status(self, new_status):
        self.traffic_status = new_status
        if new_status == True:
            self.traffic_orientation = self.original_orientation
        else:
            self.traffic_orientation = 1


    def __str__(self):
        return '[LandMark: {0}, traffic_ori: {1}, cost: {2}]'.format(self.coor, self.traffic_orientation, self.cost_value)
'''
class Crossroads(LandMark):
    def __init__(self,)
'''

information_map = [[0] * y_dim for i in range(x_dim)]
for row in range(x_dim):
    for col in range(y_dim):
        information_map[row][col] = LandMark((row,col), orie_grid[row][col])

if __name__ == '__main__':
    mark_0_0 = LandMark((0,0),orie_grid[1][1])
    mark_0_0.increase_cost()
    mark_0_0.rewrite_locked_status('locked')
    mark_0_0.add_waitting_car('num1')
    cost_2_3 = mark_0_0.get_car_cost((2,3))

    orie_sign = information_map[1][1].get_traffic_rule()
    print(orie_sign)
    print(orientation_map[orie_sign])

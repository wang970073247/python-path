
from map import coor_to_ori
from map import orientation_map
from land_mark import information_map
x_dim = len(information_map)
y_dim = len(information_map[0])


class Agv_car:
    def __init__(self, car_num):
        self.car_num = car_num
        self.position = None #tuple
        self.simple_route_coor = []
        self.route_with_orie = []
        self.information_route = []
        self.start_point = (0, 0)
        self.destination = None
        self.transport_status = None # 0:idle 1:busy 2:error
        self.orientation = None
        self.front_locked_length = 2
        self.back_locked_length = 1
        self.locked_total_length = self.front_locked_length + self.back_locked_length + 1
        self.next_action = []
        self.is_long_route = False
        self.waitting_of_busy = False

        # 0:idle  1:in init process. 2:after init and before 3. 3:planner safely arrived goal  4:car safely arrived goal
        self.car_planner_stage = 0


    def __str__(self):
        return '[Car Num: {0}, Trans Status: {1}, Position: {2}, \n Route: {3}]'. \
                format(self.car_num, self.transport_status, self.position, self.route_with_orie)

    def set_car_position(self, car_position):
        self.position = car_position

    def set_start_point(self, start_point):
        self.start_point = start_point

    def set_destination(self, destination):
        self.destination = destination

    def set_orientation(self, current_orientation):
        self.orientation = current_orientation

    def path_search(self, destination):
        self.set_destination(destination)

        action = [[0] * y_dim for i in range(x_dim)]
        expand = [[-1] * y_dim for i in range(x_dim)]
        closed = [[0] * y_dim for i in range(x_dim)]
        x = self.start_point[0]
        y = self.start_point[1]
        closed[x][y] = 1
        g = 0
        orientation  = self.orientation
        search_tree = [[g, x, y, orientation]]
        found = False
        resign = False
        count = 0

        print('begin')
        while not found and not resign:
            if len(search_tree) == 0:
                resign = True
                print('fail')
                return 'fail'
            else:
                search_tree.sort()
                next = search_tree.pop(0)
                g = next[0]
                x = next[1]
                y = next[2]
                orientation = next[3]
                expand[x][y] = count
                count += 1

                if x == self.destination[0] and y == self.destination[1]:
                    found = True
                else:
                    orie_sign = information_map[x][y].get_traffic_rule()
                    orie_vector = orientation_map[orie_sign]
                    for i in orie_vector:
                        next_orientation = coor_to_ori[i]
                        x2 = x + i[0]
                        y2 = y + i[1]
                        traffic_rule = information_map[x2][y2].get_traffic_rule()
                        if closed[x2][y2] == 0 and traffic_rule != 1:
                            if next_orientation == orientation:
                                cost = information_map[x2][y2].get_car_cost(self.start_point)
                            else:
                                cost = information_map[x2][y2].get_car_cost(self.start_point) + 1

                            g2 = g + cost
                            search_tree.append([g2, x2, y2, next_orientation])
                            closed[x2][y2] = 1
                            action[x2][y2] = (x, y, next_orientation)


        x = destination[0]
        y = destination[1]
        self.simple_route_coor = [(x,y)]
        self.route_with_orie = [(x,y,'*')]
        self.information_route = [information_map[x][y]]
        while x != self.start_point[0] or y != self.start_point[1]:
            x2 = action[x][y][0]
            y2 = action[x][y][1]
            self.simple_route_coor.insert(0,(x2,y2))
            land_mark = (x2, y2, action[x][y][2])
            self.route_with_orie.insert(0, land_mark)
            information_mark = information_map[x2][y2]
            self.information_route.insert(0, information_mark)
            x = x2
            y = y2

        self.car_planner_stage = 1
        if len(self.simple_route_coor) > self.locked_total_length:
            self.is_long_route = True
        else:
            self.is_long_route = False

        print(self.route_with_orie)


    def update_landmark_cost(self):
        if len(self.route_with_orie) != 0:
            for landmark in self.route_with_orie:
                x = landmark[0]
                y = landmark[1]
                information_map[x][y].increase_cost()

    def release_landmark(self):
        self.information_route.pop(0)
        self.route_with_orie.pop(0)
        self.simple_route_coor.pop(0)

    def update_passed_landmark(self):
        if len(self.information_route[0].get_waitting_car()) == 0:
            self.information_route[0].rewrite_locked_status('unlocked')
            self.information_route[0].update_passing_car(None)
            self.release_landmark()
        else:
            self.information_route[0].update_passing_car(self.information_route[0].pop_waitting_car())
            self.release_landmark()

    def update_coming_landmark(self, car_position):
        index = car_position + self.front_locked_length
        if self.information_route[index] == 'locked':
            self.waitting_of_busy = True
            self.next_action = ['STOP']
            self.information_route[index].add_waitting_car(self.car_num)

        else:
            if self.simple_route_coor[index] == self.destination:
                self.car_planner_stage = 3
            self.information_route[index].rewrite_locked_status('locked')
            self.next_action.pop(0)
            self.next_action.append(self.route_with_orie[index])


    def deal_with_waitting(self):
        car_position_in_route = self.simple_route_coor.index(self.position)

        for i in range(car_position_in_route + 1, car_position_in_route + 1 + self.front_locked_length):
            if self.information_route[i].get_locked_status() == 'locked' and self.information_route[i].get_passing_car() != self.car_num:
                '''
                self.next_action.clear()
                self.next_action.append('STOP')
                '''
                if self.car_num not in self.information_route[i].get_waitting_car():
                    self.information_route[i].add_waitting_car(self.car_num)
                break

            elif self.simple_route_coor[i] == self.destination:
                if self.information_route[i].get_locked_status() == 'unlocked':
                    self.information_route[i].rewrite_locked_status('locked')
                    self.information_route[i].update_passing_car(self.car_num)
                self.waitting_of_busy = False
                self.car_planner_stage = 3

                self.next_action.clear()
                for ii in range(car_position_in_route + 1, i + 1):
                    self.next_action.append(self.route_with_orie[ii])
                break

            elif self.information_route[i].get_locked_status() == 'unlocked':
                self.information_route[i].rewrite_locked_status('locked')
                self.information_route[i].update_passing_car(self.car_num)

        else:
            self.waitting_of_busy = False
            self.next_action.clear()
            for i in range(car_position_in_route + 1, car_position_in_route + 1 + self.front_locked_length):
                self.next_action.append(self.route_with_orie[i])


    def normal_update_route(self):
        if len(self.simple_route_coor) == 0 or len(self.simple_route_coor) == 1:
            print('Error: No land mark!')
            return
        else:
            car_position_in_route = self.simple_route_coor.index(self.position)

        if self.is_long_route == False:
            if self.car_planner_stage == 1: # in initialized process
                self.information_route[0].rewrite_locked_status('locked')
                self.information_route[0].update_passing_car(self.car_num)
                i = 1
                while(i < 1 + self.front_locked_length):
                    if self.information_route[i].get_locked_status() == 'locked':
                        self.information_route[i].add_waitting_car(self.car_num)
                        self.waitting_of_busy = True
                        break
                    elif self.simple_route_coor[i] == self.destination:
                        self.car_planner_stage = 3
                        self.information_route[i].rewrite_locked_status('locked')
                        self.next_action.clear()
                        for ii in range(i+1):
                            self.next_action.append(self.route_with_orie[ii])
                        break
                    else:
                        self.information_route[i].rewrite_locked_status('locked')
                        self.information_route[i].update_passing_car(self.car_num)
                else:
                    self.car_planner_stage = 2
                    self.next_action.clear()
                    for i in range(1 + self.front_locked_length):
                        self.next_action.append(self.route_with_orie[i])

            elif self.car_planner_stage == 2:
                self.update_coming_landmark(car_position_in_route)

            elif self.car_planner_stage == 3:
                if car_position_in_route == self.back_locked_length + 1:
                    self.update_passed_landmark()

            elif self.car_planner_stage == 4:
                for i in range(car_position_in_route):
                    self.update_passed_landmark()
                self.car_planner_stage = 5

        if self.is_long_route == True:
            if self.car_planner_stage == 1:
                self.information_route[0].rewrite_locked_status('locked')
                self.information_route[0].update_passing_car(self.car_num)
                i = 1
                while(i < 1 + self.front_locked_length):
                    if self.information_route[i].get_locked_status() == 'locked':
                        self.information_route[i].add_waitting_car(self.car_num)
                        self.waitting_of_busy = True
                        break
                    else:
                        self.information_route[i].rewrite_locked_status('locked')
                        self.information_route[i].update_passing_car(self.car_num)
                else:
                    self.car_planner_stage = 2
                    self.next_action.clear()
                    for i in range(1 + self.front_locked_length):
                        self.next_action.append(self.route_with_orie[i])

            elif self.car_planner_stage == 2:
                if car_position_in_route  < self.back_locked_length:
                    self.update_coming_landmark(car_position_in_route)
                else:
                    self.update_passed_landmark()
                    self.update_coming_landmark(car_position_in_route)

            elif self.car_planner_stage == 3:
                self.update_passed_landmark()
                if self.position == self.destination:
                    self.car_planner_stage = 4

            elif self.car_planner_stage == 4:
                for i in range(car_position_in_route):
                    self.update_passed_landmark()
                self.car_planner_stage = 5



if __name__ == '__main__':
    car1 = Agv_car(1)
    car1.set_start_point((1,1))
    car1.set_destination((16,12))
    car1.path_search((16,12))

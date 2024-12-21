import heapq
import time

class AStarAlgorithm:
    def __init__(self, initial_state, method="Manhattan"):
        self.initial_state = initial_state
        self.method = method
        self.goal_state = "012345678"
        self.frontier = [] # priority queue / min heap
        self.expanded = [] # ordered list of expanded
        self.frontier_dict = {}   # node : fn
        self.depth_per_node = {}  # node : depth
        self.parent = {}    # child : parent
        self.start_time = 0
        self.end_time = 0
        self.max_depth = 0

    def search(self, initial_state):
        if not self.is_solvable():
            return -1
        
        self.start_time = time.time()
        self.frontier.append((0 + self.heuristic_calc(initial_state), initial_state))
        self.frontier_dict[initial_state] = 0 + self.heuristic_calc(initial_state)
        self.parent[initial_state] = -1
        self.depth_per_node[initial_state] = 0
        heapq.heapify(self.frontier)
        
        while len(self.frontier) != 0:
            current_state_tuple = heapq.heappop(self.frontier)
            self.expanded.append(current_state_tuple[1])
            current_state = current_state_tuple[1]
            current_state = str(current_state)
            if current_state_tuple[1] != initial_state:
                self.depth_per_node[current_state_tuple[1]] = self.depth_per_node[self.parent[current_state_tuple[1]]] + 1
            self.max_depth = max(self.max_depth, self.depth_per_node[current_state_tuple[1]])

            zero_position = -1
            if len(current_state) == 8:
                zero_position = 0
                current_state = "0" + current_state
            else:
                zero_position = int(self.zero_position(current_state))
            if self.is_goal(current_state):
                break
            
            neighbours = self.get_neighbours(current_state, zero_position)
            gn = self.depth_per_node[current_state_tuple[1]] + 1
            for i in range(len(neighbours)):
                if neighbours[i] == -1:
                    continue
                if neighbours[i] in self.expanded:
                    continue
                hn = self.heuristic_calc(neighbours[i])
                fn = hn + gn

                if neighbours[i] not in self.frontier_dict:
                    heapq.heappush(self.frontier, (fn, neighbours[i]))
                    self.frontier_dict[current_state_tuple[1]] = fn
                    self.parent[neighbours[i]] = current_state_tuple[1]
                else:
                    if fn < self.frontier_dict[neighbours[i]]:
                        self.frontier_dict[neighbours[i]] = fn
                        heapq.heappush(self.frontier, (fn, neighbours[i]))
                        heapq.heapify(self.frontier)
                        self.parent[neighbours[i]] = current_state_tuple[1]
        self.end_time = time.time()
        return self.expanded
    
    # 0 1 2
    # 3 4 5
    # 6 7 8    
    def heuristic_calc(self, state):
        h = 0
        str_state = str(state)
        if len(str_state) == 8:
            str_state = "0" + str_state
        for i in range(len(str_state)):
            if str_state[i] == "0":
                continue
            if str_state[i] != self.goal_state[i]:
                x_current = (i%3)
                y_current = int(i//3)
                x_goal = (int(str_state[i])%3)
                y_goal = int(str_state[i]) // 3
                if self.method == "Manhattan":
                    h += abs(x_current - x_goal) + abs(y_current - y_goal)
                elif self.method == "Euclidean":
                    h += ((x_current - x_goal)**2 + (y_current - y_goal)**2)**0.5
        return h

    def zero_position(self, state):
        return str(state).find("0")

    def move_up(self, state, zero):
        if(int(zero) < 3):
            return -1
        str_state = str(state)
        new_state = list(str_state)
        new_state[zero], new_state[zero-3] = new_state[zero-3], new_state[zero]
        return int("".join(new_state))
    
    def move_down(self, state, zero):
        if(zero > 5):
            return -1
        str_state = str(state)
        new_state = list(str_state)
        new_state[zero], new_state[zero+3] = new_state[zero+3], new_state[zero]
        return int("".join(new_state))
    
    def move_right(self, state, zero):
        if(zero%3 == 2):
            return -1
        str_state = str(state)
        new_state = list(str_state)
        new_state[zero], new_state[zero+1] = new_state[zero+1], new_state[zero]
        return int("".join(new_state))
    
    def move_left(self, state, zero):
        if(zero%3 == 0):
            return -1
        str_state = str(state)
        new_state = list(str_state)
        new_state[zero], new_state[zero-1] = new_state[zero-1], new_state[zero]
        return int("".join(new_state))

    def path_finder(self):
        path = []
        current_state = self.expanded[-1]
        path.insert(0, str(current_state))
        while self.parent[current_state] != -1:
            current_state = self.parent[current_state]
            path.insert(0, str(current_state))
        return path
    
    def is_solvable(self):
        inversions = 0
        initial = str(self.initial_state)
        if len(str(self.initial_state)) == 8:
            initial = "0" + initial
        for i in range (len(initial)):
            if initial[i] == "0":
                continue
            for j in range(i+1, len(initial)):
                if initial[j] == "0":
                    continue
                if int(initial[i]) > int(initial[j]):
                    inversions += 1  
        return inversions % 2 == 0
    
    def get_neighbours(self, current_state, zero_position):
        neighbours = []
        neighbours.append(self.move_up(current_state, zero_position))
        neighbours.append(self.move_down(current_state, zero_position))
        neighbours.append(self.move_right(current_state, zero_position))
        neighbours.append(self.move_left(current_state, zero_position))
        return neighbours

    def is_goal(self, state):
        return str(state) == self.goal_state 

    def path_cost(self):
        # level of goal node   
        return self.depth_per_node[self.expanded[-1]]
    
    def nodes_expanded(self):
        return len(self.expanded)
    
    def search_depth(self):
        # max depth of the search tree
        return self.max_depth
    
    def running_time(self):
        return self.end_time - self.start_time
    
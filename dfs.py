import time

class dfs_solver:
    def __init__(self, initial_state, goal_state="012345678"):
        #running time = end - start
        #nodes expanded = number of nodes in explored only
        #search depth = max depth of the search tree reached
        #path = path from initial state to goal state
        #path cost = level of goal node
        
        self.initial_state = str(initial_state)
        self.goal_state = goal_state
        self.frontier = []           # frontier stack
        self.explored = set()     # visited set
        self.frontier_set = set()   # frontier set
        self.nodes_expanded = 0
        self.depth_so_far = 0       #search depth
        self.cost = dict()
        self.cost[initial_state] = 0
        self.start_time = 0
        self.end_time = 0
        self.path = []
        self.parent = {}
        
    def is_goal(self, state):
        return state == self.goal_state

    def exchange(self, state, i, j):
        state = list(state)
        state[i], state[j] = state[j], state[i]
        return "".join(state)

    def get_neighbors(self, state):
        # find index of empty cell
        for i in range(9):
            if state[i] == "0":
                empty_cell = i
                break
            
            # all possible neighbors
            #assumption: tie breaking is done by the order (up, down, left, right)
            # so we append to the stack in the order(right, left, down, up)
        neighbors = []      # stack
        if empty_cell % 3 != 2:                         # right
            neighbors.append(self.exchange(state, empty_cell, empty_cell + 1))
        if empty_cell % 3 != 0:                         # left
            neighbors.append(self.exchange(state, empty_cell, empty_cell - 1))
        if empty_cell // 3 != 2:                         # down
            neighbors.append(self.exchange(state, empty_cell, empty_cell + 3))
        if empty_cell // 3 != 0:                         # up
            neighbors.append(self.exchange(state, empty_cell, empty_cell - 3))
        return neighbors


    def reconstruct_path(self, state):
        path = [state]
        while state in self.parent:
            state = self.parent[state]
            path.append(state)
        return path[::-1]
    
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
        print(inversions)
        return inversions % 2 == 0
    
    def search(self):
        if not self.is_solvable():
            return -1
        self.start_time = time.time()
        self.frontier.append(self.initial_state) # state
        self.frontier_set.add(self.initial_state) # state
        
        while self.frontier:
            curr_state = self.frontier.pop()
            self.frontier_set.remove(curr_state)
            self.nodes_expanded += 1
            
            # print(curr_state)
            
            if curr_state in self.explored:  # skip already explored states
                continue
            
            self.explored.add(curr_state)
            
            if self.is_goal(curr_state):
                self.end_time = time.time()
                self.path += self.reconstruct_path(curr_state)
                return {
                    "path": self.path,
                    "nodes_expanded": self.nodes_expanded,
                    "search_depth": self.depth_so_far,
                    "running_time": self.end_time - self.start_time,
                    "path_cost": self.cost[curr_state]
                }
            neighbors = self.get_neighbors(curr_state)
            for neighbor in neighbors:
                if neighbor not in self.explored and neighbor not in self.frontier_set:
                    self.frontier.append(neighbor)
                    self.frontier_set.add(neighbor)
                    self.cost[neighbor] = self.cost[curr_state] + 1
                    self.parent[neighbor] = curr_state  # track the parent to reconstruct path
                    self.depth_so_far = max(self.depth_so_far, self.cost[neighbor])

                    
                    
        return "No solution found"


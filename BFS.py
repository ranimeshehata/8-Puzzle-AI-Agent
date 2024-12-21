import queue
import time


class BfsAlgorithm:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = "012345678"
        self.frontier = queue.Queue()
        self.added_nodes = set()
        self.expanded = []
        self.parent = {}
        self.start_time = 0
        self.end_time = 0
        self.depth = {self.initial_state: 0}
        self.path = []

    def is_goal(self, cur_state):
        return cur_state == self.goal_state

    def exchange(self, state, i, j):
        state = list(state)
        state[i], state[j] = state[j], state[i]
        return "".join(state)

    def get_path(self, state):
        path = [state]
        while state in self.parent:
            state = self.parent[state]
            path.append(state)
        return path[::-1]

    def get_neighbors(self, cur_state):
        neighbors = []
        # if "0" not in cur_state:
        #     cur_state = "0" + cur_state
        empty_cell = cur_state.index('0')

        if empty_cell // 3 != 0:  # up
            neighbors.append(self.exchange(cur_state, empty_cell, empty_cell - 3))
        if empty_cell // 3 != 2:  # down
            neighbors.append(self.exchange(cur_state, empty_cell, empty_cell + 3))
        if empty_cell % 3 != 0:  # left
            neighbors.append(self.exchange(cur_state, empty_cell, empty_cell - 1))
        if empty_cell % 3 != 2:  # right
            neighbors.append(self.exchange(cur_state, empty_cell, empty_cell + 1))
        return neighbors
    
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

    def bfs_search(self):
        if not self.is_solvable():
            return -1
        self.start_time = time.time()
        self.frontier.put(self.initial_state)
        self.added_nodes.add(self.initial_state)
        while not self.frontier.empty():
            cur_state = self.frontier.get()
            self.expanded.append(cur_state)

            if self.is_goal(cur_state):
                self.end_time = time.time()
                self.path += self.get_path(cur_state)
                return {

                    "path": self.path,
                    "nodes_expanded": len(self.expanded),
                    "search_depth": self.depth[cur_state],
                    "running_time": self.running_time(),
                    "path_cost": self.depth[cur_state]
                }

            neighbors = self.get_neighbors(cur_state)
            for neighbor in neighbors:
                if neighbor not in self.added_nodes:
                    self.frontier.put(neighbor)
                    self.added_nodes.add(neighbor)
                    self.parent[neighbor] = cur_state
                    self.depth[neighbor] = self.depth[cur_state] + 1
        return "No solution found"

    def running_time(self):
        return self.end_time - self.start_time

    def nodes_expanded(self):
        return self.expanded

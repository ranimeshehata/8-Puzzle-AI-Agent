import time

class iterative_dfs_solver:
    def __init__(self, initial_state, goal_state="012345678"):
        self.initial_state = str(initial_state)
        self.goal_state = goal_state
        self.frontier = []
        self.nodes_expanded = 0
        self.start_time = 0
        self.end_time = 0

    def is_goal(self, state):
        return state == self.goal_state

    def exchange(self, state, i, j):
        state = list(state)
        state[i], state[j] = state[j], state[i]
        return "".join(state)

    def get_neighbors(self, state):
        empty_cell = state.index("0")
        neighbors = []

        if empty_cell % 3 != 2:  # Right
            neighbors.append(self.exchange(state, empty_cell, empty_cell + 1))
        if empty_cell % 3 != 0:  # Left
            neighbors.append(self.exchange(state, empty_cell, empty_cell - 1))
        if empty_cell // 3 != 2:  # Down
            neighbors.append(self.exchange(state, empty_cell, empty_cell + 3))
        if empty_cell // 3 != 0:  # Up
            neighbors.append(self.exchange(state, empty_cell, empty_cell - 3))

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

    def depth_limited_search(self, state, depth_limit, depth_so_far, frontier, explored):
        explored.add(state)
        frontier.append(state)

        if self.is_goal(state):
            return True

        if depth_so_far < depth_limit:
            for neighbor in self.get_neighbors(state):
                if neighbor not in explored:
                    self.nodes_expanded += 1
                    if self.depth_limited_search(neighbor, depth_limit, depth_so_far + 1, frontier, explored):
                        return True

        frontier.pop()
        explored.remove(state)
        return False

    def iterative_dfs(self):
        if not self.is_solvable():
            return -1
        self.start_time = time.time()
        depth_limit = 0

        while True:
            frontier = []
            explored = set()
            self.nodes_expanded = 0  # Reset for each depth level

            if self.depth_limited_search(self.initial_state, depth_limit, 0, frontier, explored):
                self.end_time = time.time()
                return {
                    "path": frontier,
                    "nodes_expanded": self.nodes_expanded,
                    "search_depth": depth_limit,
                    "running_time": self.end_time - self.start_time,
                    "path_cost": len(frontier) - 1  # Depth of the solution
                }

            depth_limit += 1
class SearchAlgorithm:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = 12345678
        # change data structures to fit the algorithm
        self.frontier = []
        self.expanded = []
        self.parent = []
        self.start_time = 0
        self.end_time = 0
        self.depth_so_far = 0

    def search(self):
        
        return self.explored

    def path_finder():

        return path
    
    def is_goal(self, state):
        return state == self.goal_state 

    def path_cost(self):
        # level of goal node   
        return 0
    
    def nodes_expanded(self):
        return self.expanded
    
    def search_depth(self):
        # max depth of the search tree
        return self.depth_so_far
    
    def running_time(self):
        return self.end_time - self.start_time
    
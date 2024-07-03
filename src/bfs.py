import queue

class BreadthFirst():
    def __init__(self, start_node_x, start_node_y, end_node_x, end_node_y, wall_pos):
        self.start_node_x = start_node_x
        self.start_node_y = start_node_y
        self.end_node_x = end_node_x
        self.end_node_y = end_node_y
        self.wall_pos = wall_pos
        self.visited = []
        self.route = None
        #print('hello')

# check if a certain path is valid
    def check_valid(self, moves):
        i = self.start_node_x
        j = self.start_node_y
        for move in moves:
            if move == 'L':
                i -= 1
            elif move == 'R':
                i += 1
            elif move == 'U':
                j -= 1
            elif move == 'D':
                j += 1
            if (i, j) in self.wall_pos:
                return False
        if (i, j) in self.visited:
            return False
        else:
            self.visited.append((i, j))
            return True

    def findEnd(self, moves):
        i = self.start_node_x
        j = self.start_node_y
        for move in moves:
            if move == 'L':
                i -= 1
            elif move == 'R':
                i += 1
            elif move == 'U':
                j -= 1
            elif move == 'D':
                j += 1
            print(i, j)
        if (i, j) == (self.end_node_x, self.end_node_y):
            return True
        return False

    def bfs_execute(self):
        #print('execute')
        nums = queue.Queue()
        nums.put("")
        first_out = ""

        while not self.findEnd(first_out):
            first_out = nums.get()
            #print(add)
            for j in ["L", "R", "U", "D"]:
                latest_moves = first_out + j
                if self.check_valid(latest_moves):
                    nums.put(latest_moves)
        self.route = first_out
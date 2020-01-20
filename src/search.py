import copy
from node import Node

class Search(object):

    """Algorithm to find path to goal cell"""

    def __init__(self, board, init_pos=(0, 0), goal_pos=(0,0)):
        self.board = board
        self.init_pos = init_pos
        self.curr_node = None
        self.goal_pos = goal_pos
        self.closed = [] # list of Node obj
        self.fringe = [] # list of Node obj

    def get_path_length(self):
        """Finds a shortest path between init_pos and goal_pos by traversing 
        the board
        :returns: int

        """
        self.fringe.append(Node(pos=self.init_pos,
                                h=self._heuristic(self.init_pos)))
        
        while True:
            if len(self.fringe) == 0:
                return -1, []
            self.curr_node = self._remove_front_from_fringe()
            #print(self.curr_node)
            if self._goal_test():
                visits = self.closed

                route = []
                target = visits.__getitem__(visits.__len__()-1)
                parent = target.parent.pos
                route.append(target.pos)
                route.append(parent)
                for val in range (visits.__len__()-1, 0 , -1):
                    curr = visits.__getitem__(val)
                    if curr.pos != parent: continue
                    parent = curr.parent.pos
                    route.append(parent)
                return self.curr_node.g , route
            self.closed.append(self.curr_node)
            neighbours = self.board.get_neighbours(*self.curr_node.pos)
            neighbour_nodes = [Node(pos=neighbour,
                                    parent=self.curr_node,
                                    g=self.curr_node.g+1, h=self._heuristic(neighbour))
                               for neighbour in neighbours]
            for n in neighbour_nodes:

                temp = copy.deepcopy(self.closed)
                temp.extend(self.fringe)
                repeating = False
                for m in temp:
                    if m.pos == n.pos and m.f <= n.f:
                        repeating = True

                if repeating:
                    continue
                else:
                    self.fringe.append(n)
            #print('Here')



    def _heuristic(self, pos):
        """Calculates heuristic value from pos to goal_pos

        :pos: tuple of 2 int
        :returns: int

        """
        x1, y1 = pos
        x2, y2 = self.goal_pos
        return max(abs(x2-x1), abs(y2-y1))

    def _goal_test(self):
        """Check if self.curr_node is at goal_pos
        :returns: bool

        """
        return self.goal_pos == self.curr_node.pos

    def _remove_front_from_fringe(self):
        """Returns the member with least cost
        :returns: Node obj

        """
        node = min(self.fringe, key=lambda x: x.f)
        self.fringe.remove(node)
        return node

    def __str__(self):
        string = ""
        string += "="*20 + "\n"
        string += str(self.board) + "\n"
        string += "goal: " + str(self.goal_pos) + "\n"
        string += "init: " + str(self.init_pos) + "\n"
        string += "curr: " + str(self.curr_node) + "\n"
        string += "closed: " + str(self.closed) + "\n"
        string += "fringe: " + str(self.fringe) + "\n"
        string += "="*20 + "\n"
        return string
        

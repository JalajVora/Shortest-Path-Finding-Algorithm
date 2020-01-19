class Node(object):

    """Object representing the node in search algorithm"""

    def __init__(self, pos, parent=None, g=0, h=0):
        self.pos = pos
        self.parent = parent
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __repr__(self):
        string = "<"
        string += str(self.pos) + ", "
        if self.parent is None:
            string += "p=None, "
        else:
            string += "p=" + str(self.parent.pos) + ", "
        string += "f=" + str(self.f) + ", "
        string += "g=" + str(self.g) + ", " 
        string += "h=" + str(self.h)
        string += ">"
        return string

    def __str__(self):
        return self.__repr__()

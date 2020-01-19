class Board(object):

    """Board object for simulating the 2 dimentional sqaure grid space"""

    def __init__(self, occupied_grid):
        self.occupied_grid = occupied_grid
        
    def get_neighbours(self, row, col):
        """Get all possible neighbours of a cell

        :row: int
        :col: int
        :returns: list of tuple

        """
        combinations = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                combinations.append((row+i, col+j))
        neighbours = []
        n = self.occupied_grid.shape[0]
        for combination in combinations:
            i, j = combination
            if (i < 0 or i > n-1)\
               or (j < 0 or j > n-1)\
               or (i, j) == (row, col)\
               or self.occupied_grid[i, j] == 1:
                continue
            neighbours.append(combination)
        return neighbours

    def __str__(self):
        return str(self.occupied_grid)

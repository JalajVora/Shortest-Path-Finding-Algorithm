#! usr/bin/env python3
import random
import sys

import numpy as np
from board import Board
from search import Search


def getRand(max, arr):
    if(max > 62):
        sys.exit(-1)
    cells = []
    random_cells = random.sample(range(1, 63), max)
    for random_cell in random_cells:
        cell = (random_cell // 8, random_cell % 8)
        cells.append(cell)
    for cell in cells:
        arr[cell] = 1
    return arr

INPUT = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]])
INPUT = getRand(15, INPUT)
#print(INPUT)

def main():
    """Entry point for the code
    :returns: None

    """
    board = Board(INPUT)
    n = board.occupied_grid.shape[0]
    search_obj = Search(board, init_pos=(0, 0), goal_pos=(n-1, n-1))
    path_length, path_route = search_obj.get_path_length()
    if path_route != []:
        print("Found path with length", path_length)
        path_route += [(-1, -1)]
    else:
        print("No path found")
    for path in path_route:
        INPUT[path] = 2
    print(INPUT)


if __name__ == "__main__":
    main()



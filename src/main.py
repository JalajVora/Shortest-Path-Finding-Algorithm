#! usr/bin/env python3

import numpy as np
from board import Board
from search import Search

INPUT = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]])

def main():
    """Entry point for the code
    :returns: None

    """
    board = Board(INPUT)

    n = board.occupied_grid.shape[0]
    search_obj = Search(board, init_pos=(0, 0), goal_pos=(n-1, n-1))
    path_length = search_obj.get_path_length()
    print("Found path with length", path_length)

if __name__ == "__main__":
    main()

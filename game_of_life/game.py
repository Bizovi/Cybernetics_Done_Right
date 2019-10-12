# The credit goes to Joseph Moukarzel and Michel Haber
# https://towardsdatascience.com/from-scratch-the-game-of-life-161430453ee3

from typing import List, Dict, Tuple


class State():
    """
    Class to represent the state of the game at a given iteration
    """
    def __init__(self, state: Dict[None, Tuple[int, int]] = {}) -> None:
        self.state = state

    def get_neighbors(self, cell: Tuple[int, int], max_size: int) -> List[Tuple[int, int]]:
        """Get Moore neighbors (including diagonal) for a cell in the grid"""
        i_pos = cell[0]
        j_pos = cell[1]

        def _check_boundaries(x, max_size):
            if (x >= 0) and (x <= max_size):
                return True
            else:
                return False

        # should be > zero and <= than max_size
        i_range = [position for position in [i_pos-1, i_pos, i_pos+1]
                    if _check_boundaries(position, max_size)]
        j_range = [position for position in [j_pos-1, j_pos, j_pos+1]
                    if _check_boundaries(position, max_size)]

        neighbors = [] # initialize neighbors as an empty list
        for i in i_range:
            for j in j_range:
                if (i != i_pos or j != j_pos):
                    neighbors.append((i, j))

        neighbors.sort()
        return neighbors


class Rules():
    """Class with a method which applies a rule on a grid of cells"""
    def apply_rules(self, grid, max_size, get_neighbors):
        pass

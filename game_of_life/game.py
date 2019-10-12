# The credit goes to Joseph Moukarzel and Michel Haber
# https://towardsdatascience.com/from-scratch-the-game-of-life-161430453ee3

from typing import List, Dict, Tuple
from copy import copy
import numpy as np
from PIL import Image

# for the blaster example
board_blaster = {(50,180), (51,180), (50,181), (51,181), (60,180), (60,179), (60,181), (61,178),
         (62,177), (63,177), (61,182), (62,183), (63,183), (65,182), (66,181), (66,180),
         (66,179), (65,178), (64,180), (67,180), (70,181), (70,182), (70,183), (71,181),
         (71,182), (71,183), (72,180), (72,184), (74,180), (74,179), (74,184), (74,185),
         (84,182), (84,183), (85,182), (85,183)}


class State:
    """
    Class to represent the state of the game at a given iteration
    """
    def __init__(self, state: Dict[None, Tuple[int, int]] = {}) -> None:
        self.state = state

    def copy(self):
        """Method to copy the object"""
        return State(copy(self.state))

    def equals(self, other) -> bool:
        """Check if current state equalt other state"""
        if other is None:
            return False
        return np.array_equal(self.state, other.state)

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

    def apply_rules(self, rules, max_size: int):
        """Apply rule on a current state and return a new state
        Arguments:
        ---------
        rules: Rules object
        """
        self.state = rules.apply_rules(self.state, max_size, self.get_neighbors)
        return self


class Rules:
    """
    Class with a method which applies a rule on a grid of cells
    Really, shouldn't be a class
    """
    def apply_rules(self, grid: Dict[None, Tuple[int, int]],
            max_size: int, get_neighbors) -> Dict[None, Tuple[int, int]]:
        """Apply rules on the current grid configuration
        # if the currently not active cell has:
        # no/one/two/four or more neighbors - it dies
        # if it has 3 - survives or is added

        Arguments:
        ---------
        grid: the grid from State - self.state
        max_size: max size of the game
        get_neighbors: method from State.get_neighbors()
        """

        counter = {}

        for element in grid:
            if element not in counter:
                counter[element] = 0
            neighbors = get_neighbors(element, max_size)
            for neighbor in neighbors:
                if neighbor not in counter:
                    counter[neighbor] = 1
                else:
                    counter[neighbor] += 1

        # counter serves as a mask for grid cells which die or become alive
        for candidate in counter:
            if counter[candidate] < 2 or counter[candidate] > 3:
                grid.discard(candidate)
            if counter[candidate] == 3:
                grid.add(candidate)

        return grid


class Game:
    """A game class that iteratively applies rules to the initial state"""
    def __init__(self, initial_state: State, rules: Rules, max_size: int) -> None:
        self.initial_state = initial_state
        self.rules = rules
        self.max_size = max_size

    def run_game(self, n_iter):
        """Iteratively apply rules over the state object"""
        state = self.initial_state
        previous_state = None
        progression = []
        i = 0

        # not state.equals(previous_state) and
        while (not state.equals(previous_state) and i < n_iter):
            i += 1
            previous_state = state.copy()
            progression.append(previous_state.state)
            state = state.apply_rules(self.rules, self.max_size)

        progression.append(state.state)
        return progression


def save_gif(array: np.array, file_name: str, figsize: Tuple = (300, 300)) -> None:
    """Transform array to a gif and save to a file"""
    from PIL import Image
    array = np.uint8(np.clip(array,0,1)*255.0)
    frames = []
    for frame in range(array.shape[0]):
        img = Image.fromarray(array[frame])
        img = img.resize(figsize)
        frames.append(img)
    img.save(file_name, save_all=True, duration=33.33, append_images=frames, loop=0,size=(500,500))


def results_to_array(rw: List[Dict[int, int]], max_size: int) -> np.array:
    """Transform sparse representation to array for plotting"""
    res = np.zeros((len(rw), max_size + 1, max_size + 1), dtype=bool)
    for n in range(0,len(rw)):
        for key in rw[n]:
            res[n, key[0], key[1]] = True
    return res

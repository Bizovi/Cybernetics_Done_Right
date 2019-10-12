import pytest
import game


def test_state_initialization():
    """Test the state initialization of the game"""
    # Setup
    initial_state = {(5, 5), (5, 6), (5, 7)}

    # Exercise
    state_result = game.State(initial_state)

    # Verify
    assert state_result.state == initial_state

    # Cleanup - none necessary


def test_default_state_initialization():
    """Test the default state initialization of the game"""
    # Setup - none necessary

    # Exercise
    state_result = game.State()

    # Verify
    assert state_result.state == {}

    # Cleanup - none necessary



def test_getting_neighbors_of_cell():
    """Test if neighbors of the cell are correct"""
    # Setup
    cell = (5, 5)
    max_size = 10
    state = game.State()

    # Exercise
    neighbors = state.get_neighbors(cell=cell, max_size=max_size)

    # Verify
    true_neighbors = [
        (4, 6), (5, 6), (6, 6),
        (4, 5),         (6, 5),
        (4, 4), (5, 4), (6, 4)
    ]
    true_neighbors.sort()
    assert neighbors == true_neighbors

    # Cleanup - none necessary


def test_if_neighbors_of_cell_in_boundaries():
    """Test if neighbors of the cell are within game boundaries"""
    # Setup
    cell = (5, 4)
    max_size = 5
    state = game.State()

    # Exercise
    neighbors = state.get_neighbors(cell=cell, max_size=max_size)

    # Verify
    true_neighbors = [
        (4, 5), (5, 5),
        (4, 4), # (5, 4)
        (4, 3), (5, 3)
    ]
    true_neighbors.sort()
    assert neighbors == true_neighbors

    # Cleanup - none necessary


def test_if_neighbors_of_cell_positive():
    """Test if neighbors of the cell are within game boundaries"""
    # Setup
    cell = (0, 0)
    max_size = 5
    state = game.State()

    # Exercise
    neighbors = state.get_neighbors(cell=cell, max_size=max_size)

    # Verify
    true_neighbors = [
        (0, 1), (1, 1),
                (1, 0)
    ]
    true_neighbors.sort()
    assert neighbors == true_neighbors

    # Cleanup - none necessary


def test_rule_application_on_glider():
    """Test if we apply a method on gliders, it will return the correct state"""
    # Setup
    grid = {(4, 5), (5, 5), (6, 5)}
    max_size = 10

    rules = game.Rules()
    state = game.State(grid)

    # Exercise
    grid_result = rules.apply_rules(grid, max_size, state.get_neighbors)
    grid_expected = {(5, 4), (5, 5), (5, 6)}

    # Verify
    assert grid_result == grid_expected

    # Cleanup - none needed

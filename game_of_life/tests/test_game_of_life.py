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


def test_rule_application_on_glider_reverse():
    """Test if we apply a method on gliders, it will return the correct state"""
    # Setup
    grid = {(5, 4), (5, 5), (5, 6)}
    max_size = 10

    rules = game.Rules()
    state = game.State(grid)

    # Exercise
    grid_result = rules.apply_rules(grid, max_size, state.get_neighbors)
    grid_expected = {(4, 5), (5, 5), (6, 5)}

    # Verify
    assert grid_result == grid_expected

    # Cleanup - none needed


def test_game_initialization():
    # Setup
    max_size = 5
    initial_grid = {(2, 3), (3, 3), (4, 3)}
    initial_state = game.State(initial_grid)
    rules = game.Rules()

    # Exercise
    game_glider = game.Game(initial_state, rules.apply_rules, max_size)

    # Verify
    assert game_glider.initial_state == initial_state
    assert game_glider.max_size == max_size

    # Cleanup - none needed


def test_state_copying():
    # Setup
    initial_grid = {(2, 3), (3, 3), (4, 3)}

    # Exercise
    initial_state = game.State(initial_grid)

    # Verify
    copied_state = initial_state.copy()
    assert initial_state.state == copied_state.state

    # Cleanup - none needed


def test_running_glider_five_iterations():
    """Test if glider returns to initial position after 4 iterations"""
    # Setup
    max_size = 5
    max_iter = 5
    initial_grid = {(2, 3), (3, 3), (4, 3)}
    initial_state = game.State(initial_grid)
    rules = game.Rules()

    # Exercise
    game_glider = game.Game(initial_state, rules, max_size)
    res = game_glider.run_game(max_iter)

    # Verify
    desired_state = {(3, 2), (3, 3), (3, 4)}
    assert len(res) == max_iter + 1 # four iterations plus the initial
    assert res[-1] == desired_state

    # Cleanup - none needed


def test_equality_of_states():
    """Test that the equality checking method identifies two identical
    states for two objects"""
    # Setup
    first_grid  = {(5, 5), (5, 6), (5, 7)}
    second_grid = {(5, 5), (5, 6), (5, 7)}

    # Exercise
    first_state  = game.State(first_grid)
    second_state = game.State(second_grid)

    # Verify
    assert first_state.equals(second_state)

    # Cleanup - none needed


def test_shape_of_transforming_results_to_array():
    """Test that the list of dictionaries can be transformed
    to a 3d numpy array"""
    # Setup
    max_size = 5
    max_iter = 5
    initial_grid = {(2, 3), (3, 3), (4, 3)}
    initial_state = game.State(initial_grid)
    rules = game.Rules()
    game_glider = game.Game(initial_state, rules, max_size)
    game_states = game_glider.run_game(max_iter)

    # Exercise
    res = game.results_to_array(game_states, max_size)

    # Verify
    assert res.shape == (6, max_size + 1, max_size + 1)

    # Cleanup - none needed


def test_counting_logic_of_alive_neighbors():
    """Test if the counting of neighbors is correct"""
    # Setup
    rules = game.Rules()
    max_size = 5
    grid = {(3, 3), (3, 4), (3, 5)}
    state = game.State(grid)

    # Exercise
    result_counter = game.Rules.count_neighbors(grid, max_size, state.get_neighbors)

    # Verify
    true_counter = {
        (2, 2): 1, (3, 2): 1, (4, 2): 1,
        (4, 3): 2, (4, 4): 3, (4, 5): 2,
        (2, 3): 2, (2, 4): 3, (2, 5): 2,
        (3, 3): 1, (3, 4): 2, (3, 5): 1
    }
    assert result_counter == true_counter

    # Cleanup - none necessary


## Implementing HighLife replicator dynamic
def test_high_life_rules_inheritance_counting():
    # Setup
    rules = game.HighlifeRules()
    max_size = 5
    grid = {(3, 3), (3, 4), (3, 5)}
    state = game.State(grid)

    # Exercise
    result_counter = game.HighlifeRules.count_neighbors(grid, max_size, state.get_neighbors)

    # Verify
    true_counter = {
        (2, 2): 1, (3, 2): 1, (4, 2): 1,
        (4, 3): 2, (4, 4): 3, (4, 5): 2,
        (2, 3): 2, (2, 4): 3, (2, 5): 2,
        (3, 3): 1, (3, 4): 2, (3, 5): 1
    }
    assert result_counter == true_counter

    # Cleanup - none necessary


def test_high_life_rule_application_on_a_block():
    """Test one iteration of high life rule on a square"""
    # Setup
    grid = {(4, 5), (5, 5), (4, 6), (5, 6)}
    max_size = 10

    rules = game.HighlifeRules()
    state = game.State(grid)

    # Exercise
    grid_result = rules.apply_rules(grid, max_size, state.get_neighbors)
    grid_expected = {(4, 5), (5, 5), (4, 6), (5, 6)}

    # Verify
    assert grid_result == grid_expected

    # Cleanup - none needed

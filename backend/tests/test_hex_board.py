import sys
sys.path.append("backend")
from hex_board import HexBoard

board = HexBoard(radius=4)

# Test 1: cube coordinate invariant
for coords in board.grid:
    assert sum(coords) == 0

# Test 2: center has 6 neighbors
assert len(board.get_neighbors(0, 0, 0)) == 6

# Test 3: true corner tile has 3 neighbors
assert len(board.get_neighbors(4, -4, 0)) == 3

# Test 4: outer edge (non-corner) tile has 4 neighbors
assert len(board.get_neighbors(4, -3, -1)) == 4

# Test 5: all neighbors are valid tiles inside the grid
for neighbor in board.get_neighbors(0, 0, 0):
    assert (neighbor.q, neighbor.r, neighbor.s) in board.grid

# Test 6: total tile count for radius 4 should be 61
assert len(board.grid) == 61

print("All tests passed!")
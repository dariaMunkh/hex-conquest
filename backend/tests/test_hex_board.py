import sys
sys.path.append("backend")
from hex_board import HexBoard

board = HexBoard(radius=4)

# Test 1: cube coordinate invariant
for coords in board.grid:
    assert sum(coords) == 0

# Test 2: center tile has 6 neighbors
neighbors = board.get_neighbors(0, 0, 0)
assert len(neighbors) == 6

print("All tests passed!")
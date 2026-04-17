from dataclasses import dataclass, field
from typing import Optional

CUBE_DIRECTIONS = [
    (1, -1, 0), (1, 0, -1), (0, 1, -1),
    (-1, 1, 0), (-1, 0, 1), (0, -1, 1)
]

@dataclass
class HexTile:
    q: int
    r: int
    s: int
    owner: int = 0        # 0=empty, 1=player, 2=AI
    is_border: bool = False

class HexBoard:
    def __init__(self, radius: int = 4):
        self.radius = radius
        self.grid: dict[tuple, HexTile] = {}
        self._generate_grid()

    def _generate_grid(self):
        for q in range(-self.radius, self.radius + 1):
            for r in range(-self.radius, self.radius + 1):
                s = -q - r
                if abs(s) <= self.radius:
                    self.grid[(q, r, s)] = HexTile(q, r, s)

    def get_neighbors(self, q, r, s) -> list[HexTile]:
        return [
            self.grid[(q+dq, r+dr, s+ds)]
            for dq, dr, ds in CUBE_DIRECTIONS
            if (q+dq, r+dr, s+ds) in self.grid
        ]

    def hex_distance(self, a: tuple, b: tuple) -> int:
        return max(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))

    def get_territory(self, player: int) -> int:
        return sum(1 for tile in self.grid.values() if tile.owner == player)


if __name__ == "__main__":
    board = HexBoard(radius=4)
    print(f"Board created with {len(board.grid)} tiles")
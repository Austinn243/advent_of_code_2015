"""
Advent of Code 2015: Day 3
Perfectly Spherical Houses in a Vacuum
https://adventofcode.com/2015/day/3
"""

from enum import Enum
from os import path

INPUT_FILE = "input.txt"


class Direction(Enum):
    """Directions in which Santa can move."""

    UP = "^"
    DOWN = "v"
    RIGHT = ">"
    LEFT = "<"


class GiftGrid:
    """A grid of houses that received gifts."""

    def __init__(self) -> None:
        """Initialize the grid with the starting house."""

        self.visited = {(0, 0)}

    def count_houses(self) -> int:
        """Count the number of houses that received at least one gift."""

        return len(self.visited)

    def perform_deliveries(
        self,
        directions: list[Direction],
        agent_count: int = 1,
    ) -> None:
        """Deliver gifts to the houses according to the given directions."""

        routes = []

        for i in range(agent_count):
            routes.append(directions[i::agent_count])

        for route in routes:
            x, y = (0, 0)

            for direction in route:
                x, y = self._move(x, y, direction)
                self.visited.add((x, y))

    def _move(self, x: int, y: int, direction: Direction) -> tuple[int, int]:
        """Move Santa according to the given direction."""

        match direction:
            case Direction.UP:
                return x, y + 1
            case Direction.DOWN:
                return x, y - 1
            case Direction.RIGHT:
                return x + 1, y
            case Direction.LEFT:
                return x - 1, y
            case _:
                raise ValueError(f"Invalid direction: {direction}")


def read_directions(file_path: str) -> list[Direction]:
    """Read directions from the input file."""

    with open(file_path, encoding="UTF-8") as file:
        return [Direction(char) for char in file.read().strip()]


def main() -> None:
    """Execute the program."""

    file_path = path.join(path.dirname(__file__), INPUT_FILE)

    directions = read_directions(file_path)

    for agent_count in range(1, 3):
        gift_grid = GiftGrid()
        gift_grid.perform_deliveries(directions, agent_count=agent_count)

        house_count = gift_grid.count_houses()
        print(f"{agent_count} Santa(s) delivered gifts to {house_count} houses.")


if __name__ == "__main__":
    main()

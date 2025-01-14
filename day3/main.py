"""
Advent of Code 2015: Day 3
Perfectly Spherical Houses in a Vacuum
https://adventofcode.com/2015/day/3
"""

INPUT_FILE = "./input.txt"


class GiftGrid:
    """A grid of houses that received gifts."""

    def __init__(self) -> None:
        """Initialize the grid with the starting house."""

        self.visited = {(0, 0)}

    def count_houses(self) -> int:
        """Count the number of houses that received at least one gift."""

        return len(self.visited)

    def perform_deliveries(self, directions: str, agent_count: int = 1) -> None:
        """Deliver gifts to the houses according to the given directions."""

        routes = []

        for i in range(agent_count):
            routes.append(directions[i::agent_count])

        for route in routes:
            x, y = (0, 0)

            for direction in route:
                x, y = self._move(x, y, direction)
                self.visited.add((x, y))

    def _move(self, x: int, y: int, direction: str) -> tuple[int, int]:
        """Move Santa according to the given direction."""

        match direction:
            case "^":
                return x, y + 1
            case "v":
                return x, y - 1
            case ">":
                return x + 1, y
            case "<":
                return x - 1, y
            case _:
                raise ValueError(f"Invalid direction: {direction}")


def read_input() -> str:
    """Read directions from the input file."""

    with open(INPUT_FILE, encoding="UTF-8") as file:
        return file.read().strip()


def main() -> None:
    """Execute the program."""

    directions = read_input()

    for agent_count in range(1, 3):
        gift_grid = GiftGrid()
        gift_grid.perform_deliveries(directions, agent_count=agent_count)

        house_count = gift_grid.count_houses()
        print(f"{agent_count} Santa(s) delivered gifts to {house_count} houses.")


if __name__ == "__main__":
    main()

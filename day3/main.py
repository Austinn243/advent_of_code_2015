"""
Advent of Code 2015: Day 3
Perfectly Spherical Houses in a Vacuum
https://adventofcode.com/2015/day/3
"""

from enum import Enum
from os import path
from typing import NamedTuple

INPUT_FILE = "input.txt"


class Position(NamedTuple):
    """A position on the grid."""

    x: int
    y: int


class Direction(Enum):
    """Directions in which Santa can move."""

    UP = "^"
    DOWN = "v"
    RIGHT = ">"
    LEFT = "<"


def read_directions(file_path: str) -> list[Direction]:
    """Read directions from the input file."""

    with open(file_path, encoding="UTF-8") as file:
        return [Direction(char) for char in file.read().strip()]


def split_directions(
    directions: list[Direction],
    agent_count: int,
) -> list[list[Direction]]:
    """Split the directions into separate routes for each agent."""

    return [directions[i::agent_count] for i in range(agent_count)]


def advance_position(position: Position, direction: Direction) -> Position:
    """Advance the position in the given direction."""

    match direction:
        case Direction.UP:
            return Position(position.x, position.y + 1)
        case Direction.DOWN:
            return Position(position.x, position.y - 1)
        case Direction.RIGHT:
            return Position(position.x + 1, position.y)
        case Direction.LEFT:
            return Position(position.x - 1, position.y)


def deliver_gifts(directions: list[Direction], agent_count: int = 1) -> int:
    """Deliver gifts to the houses according to the given directions.

    Returns the number of houses visited.
    """

    routes = split_directions(directions, agent_count)
    visited = {Position(0, 0)}

    for route in routes:
        position = Position(0, 0)

        for direction in route:
            position = advance_position(position, direction)
            visited.add(position)

    return len(visited)


def main() -> None:
    """Execute the program."""

    file_path = path.join(path.dirname(__file__), INPUT_FILE)

    directions = read_directions(file_path)

    house_count_alone = deliver_gifts(directions, 1)
    print(f"On his own, Santa delivered gifts to {house_count_alone} houses.")

    house_count_with_help = deliver_gifts(directions, 2)
    print(f"With help, Santa delivered gifts to {house_count_with_help} houses.")


if __name__ == "__main__":
    main()

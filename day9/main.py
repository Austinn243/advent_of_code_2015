"""
Advent of Code 2015, Day 9
All in a Single Night
https://adventofcode.com/2015/day/9
"""

import re
from os import path
from typing import NamedTuple

INPUT_FILE = "input.txt"
TEST_FILE = "test.txt"

ROUTE_REGEX = re.compile(r"(\w+) to (\w+) = (\d+)")


class Route(NamedTuple):
    """An undirected route between two cities."""

    city1: str
    city2: str
    distance: int


def read_routes(file_path: str) -> list[Route]:
    """Read routes between cities from a file."""

    with open(file_path, encoding="utf-8") as file:
        return [parse_route(line.strip()) for line in file]


def parse_route(line: str) -> Route:
    """Parse a route from a line of text."""

    pattern_match = re.match(ROUTE_REGEX, line)
    if not pattern_match:
        raise ValueError(f"Invalid route: {line}")
    
    city1, city2, distance = pattern_match.groups()

    return Route(city1, city2, int(distance))


def get_shortest_distance_to_visit_all_cities(routes: list[Route]) -> int:
    """Determine the shortest distance required to visit all cities.
    
    Calculations can start and end at any city so long as each city is only visited once.
    """

    pass


def main() -> None:
    """Read route data from a file and process it."""

    input_file = TEST_FILE
    file_path = path.join(path.dirname(__file__), input_file)

    routes = read_routes(file_path)
    print(routes)

    shortest_distance = get_shortest_distance_to_visit_all_cities(routes)
    print(f"Shortest distance to visit all cities: {shortest_distance}")


if __name__ == "__main__":
    main()
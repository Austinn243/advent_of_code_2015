"""
Advent of Code 2015, Day 14
Reindeer Olympics
https://adventofcode.com/2015/day/14
"""

import re
from dataclasses import dataclass
from os import path

INPUT_FILE = "input.txt"
TEST_FILE = "test.txt"

REINDEER_REGEX = re.compile(
    r"(\w+) can fly (\d+) km/s for (\d+) seconds, "
    r"but then must rest for (\d+) seconds.",
)

TARGET_TIME = 2503


@dataclass
class Reindeer:
    name: str
    speed: int
    fly_time: int
    rest_time: int

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Reindeer) and self.name == other.name


def read_reindeer_data(file_path: str) -> list[Reindeer]:
    """Read information about each reindeer from a file."""

    with open(file_path, encoding="utf-8") as file:
        return [parse_reindeer(line.strip()) for line in file]


def parse_reindeer(line: str) -> Reindeer:
    """Parse a reindeer's data from a line of text."""

    pattern_match = re.match(REINDEER_REGEX, line)
    if not pattern_match:
        raise ValueError(f"Invalid reindeer data: {line}")

    name = pattern_match.group(1)
    speed = int(pattern_match.group(2))
    fly_time = int(pattern_match.group(3))
    rest_time = int(pattern_match.group(4))

    return Reindeer(name, speed, fly_time, rest_time)


def find_distance_after_time(reindeer: Reindeer, time: int) -> int:
    """Determine how far a reindeer will have traveled after a given time."""

    distance = 0

    while time > 0:
        fly_time = min(reindeer.fly_time, time)
        distance += fly_time * reindeer.speed
        time -= fly_time

        rest_time = min(reindeer.rest_time, time)
        time -= rest_time

    return distance


def find_winning_reindeer_by_distance(
    reindeer: list[Reindeer],
    race_time: int,
) -> tuple[Reindeer, int]:
    """Determine the winning reindeer based on the distance covered in a given time.

    Returns the winning reindeer and the distance they traveled.
    """

    finish_distances = {}

    for deer in reindeer:
        finish_distance = find_distance_after_time(deer, race_time)
        finish_distances[deer] = finish_distance

    winner = None
    winning_distance = 0
    for deer, finish_distance in finish_distances.items():
        if finish_distance > winning_distance:
            winner = deer
            winning_distance = finish_distance

    return winner, winning_distance


def find_winning_reindeer_by_points(
    reindeer: list[Reindeer],
    race_time: int,
) -> tuple[Reindeer, int]:
    """Determine which reindeer is the winner based on their points after a given time.

    Returns the winning reindeer and the points they have.

    Reindeer gain a point for each second they are in the lead for distance traveled.
    Therefore, the winning reindeer is the one that maintains the lead the longest.
    """

    points = {deer: 0 for deer in reindeer}
    distance = {deer: 0 for deer in reindeer}

    for time in range(1, race_time + 1):
        for deer in reindeer:
            distance[deer] = find_distance_after_time(deer, time)

        leading_reindeer = []
        leading_distance = 0

        for deer, deer_distance in distance.items():
            if deer_distance > leading_distance:
                leading_reindeer = [deer]
                leading_distance = deer_distance
            elif deer_distance == leading_distance:
                leading_reindeer.append(deer)

        for deer in leading_reindeer:
            points[deer] += 1

    winner = None
    winning_points = 0

    for deer, deer_points in points.items():
        if deer_points > winning_points:
            winner = deer
            winning_points = deer_points

    return winner, winning_points


def main() -> None:
    """Read information about each reindeer from a file and process it."""

    input_file = INPUT_FILE
    file_path = path.join(path.dirname(__file__), input_file)

    reindeer = read_reindeer_data(file_path)
    print(reindeer)

    race_time = TARGET_TIME

    distance_winner, winning_distance = find_winning_reindeer_by_distance(
        reindeer,
        race_time,
    )
    print(f"After a time of {race_time} seconds and judging by distance traveled:")
    print(f"{distance_winner.name} wins with a distance of {winning_distance} km.")

    points_winner, winning_points = find_winning_reindeer_by_points(reindeer, race_time)
    print(f"After a time of {race_time} seconds and judging by points:")
    print(f"{points_winner.name} wins with {winning_points} points.")


if __name__ == "__main__":
    main()

"""
Advent of Code 2015, Day 6
Probably a Fire Hazard
https://adventofcode.com/2015/day/6
"""

from enum import Enum
from itertools import chain
from os import path
from typing import Callable

import numpy as np

INPUT_FILE = "input.txt"

HEIGHT = 1000
WIDTH = 1000

LightState = int
LightGrid = np.ndarray[LightState]
Coordinate = tuple[int, int]


class CommandType(Enum):
    """Describes the type of command that can be executed on a light grid."""

    TURN_ON = "turn on"
    TURN_OFF = "turn off"
    TOGGLE = "toggle"


RawCommand = tuple[CommandType, Coordinate, Coordinate]
LightCommand = Callable[[LightState], LightState]

turn_on: LightCommand = np.vectorize(lambda _: 1)
turn_off: LightCommand = np.vectorize(lambda _: 0)
toggle: LightCommand = np.vectorize(lambda light: 1 - light)
increment_by_one: LightCommand = np.vectorize(lambda light: light + 1)
increment_by_two: LightCommand = np.vectorize(lambda light: light + 2)
decrement: LightCommand = np.vectorize(lambda light: max(0, light - 1))

COMMAND_MAP_V1 = {
    CommandType.TURN_ON: turn_on,
    CommandType.TURN_OFF: turn_off,
    CommandType.TOGGLE: toggle,
}

COMMAND_MAP_V2 = {
    CommandType.TURN_ON: increment_by_one,
    CommandType.TURN_OFF: decrement,
    CommandType.TOGGLE: increment_by_two,
}


def execute_command(
    grid: LightGrid,
    command: LightCommand,
    start: Coordinate,
    end: Coordinate,
) -> LightGrid:
    """Execute a command on a light grid."""

    start_x, start_y = start
    end_x, end_y = end

    segment = grid[start_x : end_x + 1, start_y : end_y + 1]
    transformed_segment = command(segment)
    grid[start_x : end_x + 1, start_y : end_y + 1] = transformed_segment

    return grid


def parse_raw_command(line: str) -> RawCommand:
    """Read a command from a line of text."""

    parts = line.split()

    command_type = None
    start_segment = None
    end_segment = None

    if parts[0] == "toggle":
        command_type = CommandType.TOGGLE
        start_segment = parts[1]
        end_segment = parts[3]
    else:
        start_segment = parts[2]
        end_segment = parts[4]

        command_type = CommandType.TURN_ON if parts[1] == "on" else CommandType.TURN_OFF

    start_coords = tuple(map(int, start_segment.split(",")))
    end_coords = tuple(map(int, end_segment.split(",")))

    return command_type, start_coords, end_coords


def read_raw_commands(file_path: str) -> list[RawCommand]:
    """Read raw commands from a file."""

    with open(file_path, encoding="utf-8") as file:
        return [parse_raw_command(line) for line in file]


def main() -> None:
    """Execute the program."""

    file_path = path.join(path.dirname(__file__), INPUT_FILE)

    raw_commands = read_raw_commands(file_path)

    for i, command_map in enumerate([COMMAND_MAP_V1, COMMAND_MAP_V2]):
        grid = np.full((HEIGHT, WIDTH), 0)

        for command_type, start, end in raw_commands:
            grid = execute_command(grid, command_map[command_type], start, end)

        total_brightness = sum(chain(*grid))
        print(f"Part {i + 1}: {total_brightness}")


if __name__ == "__main__":
    main()

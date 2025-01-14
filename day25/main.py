"""
Advent of Code 2015, Day 25
Let It Snow
https://adventofcode.com/2015/day/25
"""

import re
from os import path

INPUT_FILE = "input.txt"

# NOTE: The double space in the regex is an intentional part of the puzzle input.
CODE_REGEX = re.compile(
    r"To continue, please consult the code grid in the manual.  "
    r"Enter the code at row (\d+), column (\d+).",
)


def read_code_position(file_path: str) -> tuple[int, int]:
    """Read the target position of a code from a file."""

    with open(file_path, encoding="utf-8") as file:
        pattern_match = re.match(CODE_REGEX, file.read())
        if pattern_match:
            row, column = pattern_match.groups()
            return int(row), int(column)

    raise ValueError("Code position not found in file.")


def get_code_number(row: int, column: int) -> int:
    """Calculate the number in which the code is generated."""


def get_code_at_position(row: int, column: int) -> int:
    """Calculate the code at a given position in the grid."""

    pass


def main() -> None:
    """Read the target position of a code from a file and process it."""

    input_file = INPUT_FILE
    file_path = path.join(path.dirname(__file__), input_file)

    code_row, code_column = read_code_position(file_path)
    print(code_row, code_column)

    code = get_code_at_position(code_row, code_column)
    print(f"The code is {code}")


if __name__ == "__main__":
    main()

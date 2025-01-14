"""
Advent of Code 2015, Day 1
Not Quite Lisp
https://adventofcode.com/2015/day/1
"""

from os import path

INPUT_FILE = "input.txt"


def read_instructions(file_path: str) -> str:
    """Read instructions from an input file."""

    with open(file_path, encoding="utf-8") as file:
        return file.read()


def update_floor(current_floor: int, instruction: str) -> int:
    """Update the current floor based on the instruction."""

    if instruction == "(":
        return current_floor + 1
    elif instruction == ")":
        return current_floor - 1

    return current_floor


def is_basement_floor(floor: int) -> bool:
    """Check if Santa is in the basement."""

    return floor < 0


def find_final_floor(instructions: str) -> int:
    """Find the final floor Santa ends up on."""

    floor = 0

    for char in instructions:
        floor = update_floor(floor, char)

    return floor


def find_first_basement_instruction(instructions: str) -> int:
    """Find the position of the first instruction leads Santa into the basement."""

    floor = 0

    for position, instruction in enumerate(instructions):
        if is_basement_floor(floor):
            return position

        floor = update_floor(floor, instruction)

    raise ValueError("Santa never enters the basement.")


def main() -> None:
    """Execute the program."""

    file_path = path.join(path.dirname(__file__), INPUT_FILE)

    instructions = read_instructions(file_path)

    floor = find_final_floor(instructions)
    print(f"Santa is on floor {floor}.")

    basement_instruction_position = find_first_basement_instruction(instructions)
    print(f"Santa enters the basement at instruction {basement_instruction_position}.")


if __name__ == "__main__":
    main()

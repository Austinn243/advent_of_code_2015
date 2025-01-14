"""
Advent of Code 2015, Day 2
I Was Told There Would Be No Math
https://adventofcode.com/2015/day/2
"""

from os import path

INPUT_FILE = "input.txt"


class Present:
    """Represents a present with its dimensions."""

    def __init__(self, length: int, width: int, height: int) -> None:
        """Initialize the present with its dimensions."""

        self.length = length
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        """Represent the present as a string."""

        return (
            f"Present(length={self.length}, width={self.width}, height={self.height})"
        )

    def required_wrapping_paper(self) -> int:
        """Calculate the required wrapping paper for the present."""

        side_areas = (
            self.length * self.width,
            self.width * self.height,
            self.height * self.length,
        )

        surface_area = sum(2 * side_area for side_area in side_areas)
        slack = min(side_areas)

        return surface_area + slack

    def required_ribbon(self) -> int:
        """Calculate the required ribbon for the present."""

        dimensions = sorted((self.length, self.width, self.height))

        wrapper = 2 * (dimensions[0] + dimensions[1])
        bow = self.length * self.width * self.height

        return wrapper + bow


def parse_present(line: str) -> Present:
    """Read information about a present from a line of text."""

    raw_dimensions = line.strip().split("x")
    dimensions = tuple(map(int, raw_dimensions))

    return Present(*dimensions)


def read_presents(file_path: str) -> list[Present]:
    """Read the presents from an input file."""

    with open(file_path, encoding="utf-8") as file:
        return [parse_present(line) for line in file]


def get_total_wrapping_paper(presents: list[Present]) -> int:
    """Calculate the total wrapping paper required for all presents."""

    return sum(present.required_wrapping_paper() for present in presents)


def get_total_ribbon(presents: list[Present]) -> int:
    """Calculate the total ribbon required for all presents."""

    return sum(present.required_ribbon() for present in presents)


def main() -> None:
    """Execute the program."""

    file_path = path.join(path.dirname(__file__), INPUT_FILE)

    presents = read_presents(file_path)

    total_wrapping_paper = get_total_wrapping_paper(presents)
    print(f"Total wrapping paper required: {total_wrapping_paper}")

    total_ribbon = get_total_ribbon(presents)
    print(f"Total ribbon required: {total_ribbon}")


if __name__ == "__main__":
    main()

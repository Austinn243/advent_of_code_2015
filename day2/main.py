"""
Advent of Code 2015, Day 2
I Was Told There Would Be No Math
https://adventofcode.com/2015/day/2
"""

INPUT_FILE = "./input.txt"


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


def read_present(line: str) -> Present:
    """Read information about a present from a line of the input file."""

    raw_dimensions = line.strip().split("x")
    dimensions = tuple(map(int, raw_dimensions))

    return Present(*dimensions)


def read_input() -> list[Present]:
    """Read the presents from the input file."""

    presents = []

    with open(INPUT_FILE, encoding="utf-8") as file:
        for line in file:
            presents.append(read_present(line))

    return presents


def main() -> None:
    """Execute the program."""

    presents = read_input()
    total_wrapping_paper = sum(
        present.required_wrapping_paper() for present in presents
    )
    print(f"Total wrapping paper required: {total_wrapping_paper}")

    total_ribbon = sum(present.required_ribbon() for present in presents)
    print(f"Total ribbon required: {total_ribbon}")


if __name__ == "__main__":
    main()

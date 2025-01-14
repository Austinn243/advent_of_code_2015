"""
Advent of Code 2015, Day 10,
Elves Look, Elves Say
https://adventofcode.com/2015/day/10
"""

INPUT = "1321131112"


def look_and_say(sequence: str) -> str:
    """Transform the sequence using the look-and-say method."""

    # NOTE: We add a space to the end of the sequence to handle all digits
    # using the same logic. Otherwise, the final subsequence would need to
    # be handled separately.
    source = sequence + " "
    subsequences = []

    start = 0
    for end in range(1, len(source)):
        if source[start] != source[end]:
            subsequences.append((source[start], end - start))
            start = end

    return "".join(f"{count}{digit}" for digit, count in subsequences)


def main() -> None:
    """Execute the program."""

    sequence = INPUT

    for _ in range(40):
        sequence = look_and_say(sequence)

    print(f"Part 1: {len(sequence)}")

    for _ in range(10):
        sequence = look_and_say(sequence)

    print(f"Part 2: {len(sequence)}")


if __name__ == "__main__":
    main()

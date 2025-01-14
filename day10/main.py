"""
Advent of Code 2015, Day 10,
Elves Look, Elves Say
https://adventofcode.com/2015/day/10
"""

INPUT_SEQUENCE = "1321131112"


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


def look_and_say_n_times(sequence: str, n: int) -> str:
    """Apply the look-and-say method n times to the sequence."""

    for _ in range(n):
        sequence = look_and_say(sequence)

    return sequence


def main() -> None:
    """Execute the program."""

    initial_sequence = INPUT_SEQUENCE

    sequence_after_40 = look_and_say_n_times(initial_sequence, 40)
    print("After 40 iterations:")
    print(f"The length of the sequence is: {len(sequence_after_40)}")

    sequence_after_50 = look_and_say_n_times(sequence_after_40, 10)
    print("After 50 iterations:")
    print(f"The length of the sequence is: {len(sequence_after_50)}")


if __name__ == "__main__":
    main()

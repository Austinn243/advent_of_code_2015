"""
Advent of Code 2015, Day 5
Doesn't He Have Intern-Elves For This?
https://adventofcode.com/2015/day/5
"""

from collections import defaultdict
from itertools import pairwise
from os import path
from typing import Callable, Iterable

INPUT_FILE = "input.txt"

NAUGHTY_SUBSTRINGS = frozenset(["ab", "cd", "pq", "xy"])
VOWELS = frozenset("aeiou")


def read_input(file_path: str) -> list[str]:
    """Read the lines of text from an input file."""

    with open(file_path, encoding="utf-8") as file:
        return file.read().strip().split("\n")


def contains_three_vowels(candidate: str) -> bool:
    """Check if a string contains at least three vowels."""

    count = 0

    for char in candidate:
        if char in VOWELS:
            count += 1

        if count >= 3:
            return True

    return False


def contains_double_letter(candidate: str) -> bool:
    """Check if a string contains a letter that appears twice in a row."""

    return any(ch1 == ch2 for ch1, ch2 in pairwise(candidate))


def contains_naughty_substring(candidate: str) -> bool:
    """Check if a string contains any of the naughty substrings."""

    return any(substring in candidate for substring in NAUGHTY_SUBSTRINGS)


def is_nice_string(candidate: str) -> bool:
    """Determine if a string is nice according to the old rules."""

    return (
        contains_three_vowels(candidate)
        and contains_double_letter(candidate)
        and not contains_naughty_substring(candidate)
    )


def contains_non_overlapping_repeated_pair(candidate: str) -> bool:
    """Check if a string contains a non-overlapping repeated pair of letters."""

    pair_locations = defaultdict(list)

    for index, pair in enumerate(pairwise(candidate)):
        pair_locations[pair].append(index)

    for locations in pair_locations.values():
        if len(locations) < 2:
            continue

        contains_non_overlapping_pair = locations[-1] - locations[0] > 1
        if contains_non_overlapping_pair:
            return True

    return False


def triplewise[T](iterable: Iterable[T]) -> Iterable[tuple[T, T, T]]:
    """Iterate over an iterable in groups of three."""

    for (first, second), (_, third) in pairwise(pairwise(iterable)):
        yield first, second, third


def contains_double_letter_with_gap(candidate: str) -> bool:
    """Check if a string contains a letter that repeats with a gap of one letter."""

    return any(ch1 == ch3 for ch1, _, ch3 in triplewise(candidate))


def is_nice_string_v2(candidate: str) -> bool:
    """Determine if a string is nice according to the new rules."""

    validators = [
        contains_non_overlapping_repeated_pair,
        contains_double_letter_with_gap,
    ]

    return all(validator(candidate) for validator in validators)


def count_nice_strings(candidates: list[str], validator: Callable[[str], bool]) -> int:
    """Count the number of nice strings in the list of candidates."""

    return sum(validator(candidate) for candidate in candidates)


def main() -> None:
    """Execute the program."""

    file_path = path.join(path.dirname(__file__), INPUT_FILE)

    candidates = read_input(file_path)

    for validator in [is_nice_string, is_nice_string_v2]:
        nice_string_count = count_nice_strings(candidates, validator)
        print(f"Number of nice strings: {nice_string_count}")


if __name__ == "__main__":
    main()

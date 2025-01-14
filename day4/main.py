"""Advent of Code 2015, Day 4
The Ideal Stocking Stuffer
https://adventofcode.com/2015/day/4
"""

from hashlib import md5

SECRET_KEY = "bgvyzdsv"


def find_md5_hash(key: str, number: int) -> str:
    """Find the MD5 hash of the key and number."""

    hash_input = key + str(number)
    return md5(hash_input.encode()).hexdigest()


def find_lowest_number_with_hash_starting_with_n_zeroes(
    key: str, zero_count: int = 1,
) -> int:
    """Find the lowest number whose hash that starts with at least n zeroes."""

    prefix = "0" * zero_count

    number = 0

    while True:
        hash = find_md5_hash(key, number)
        if hash.startswith(prefix):
            return number

        number += 1


def main() -> None:
    """Execute the program."""

    for zero_count in [5, 6]:
        min_number = find_lowest_number_with_hash_starting_with_n_zeroes(
            SECRET_KEY, zero_count,
        )
        print(
            f"Lowest number with hash starting with {zero_count} zeroes: {min_number}",
        )


if __name__ == "__main__":
    main()

"""
Advent of Code 2015, Day 16
Aunt Sue
https://adventofcode.com/2015/day/16
"""

from collections.abc import Callable
import re
from dataclasses import dataclass
from operator import eq, gt, lt
from os import path
from typing import Optional


INPUT_FILE = "input.txt"

SUE_REGEX = re.compile(r"Sue (\d+): (.+)")

# NOTE: The use of optional values in the Sue class indicates that the property is not known,
# not that the value is zero. In these cases, the property should be ignored when comparing Sues.

@dataclass
class Sue:
    number: int
    children: Optional[int] = None
    cats: Optional[int] = None
    samoyeds: Optional[int] = None
    pomeranians: Optional[int] = None
    akitas: Optional[int] = None
    vizslas: Optional[int] = None
    goldfish: Optional[int] = None
    trees: Optional[int] = None
    cars: Optional[int] = None
    perfumes: Optional[int] = None

Comparator = Callable[[Optional[int], Optional[int]], bool]

@dataclass
class ComparisonRules:
    children: Comparator
    cats: Comparator
    samoyeds: Comparator
    pomeranians: Comparator
    akitas: Comparator
    vizslas: Comparator
    goldfish: Comparator
    trees: Comparator
    cars: Comparator
    perfumes: Comparator

COMPARE_BY_EQUIVALENCE = ComparisonRules(
    children=eq,
    cats=eq,
    samoyeds=eq,
    pomeranians=eq,
    akitas=eq,
    vizslas=eq,
    goldfish=eq,
    trees=eq,
    cars=eq,
    perfumes=eq
)
COMPARE_WITH_RANGES = ComparisonRules(
    children=eq,
    cats=gt,
    samoyeds=eq,
    pomeranians=lt,
    akitas=eq,
    vizslas=eq,
    goldfish=lt,
    trees=gt,
    cars=eq,
    perfumes=eq
)
TARGET_SUE = Sue(0, children=3, cats=7, samoyeds=2, pomeranians=3, akitas=0, vizslas=0, goldfish=5, trees=3, cars=2, perfumes=1)


def read_sues(file_path: str) -> list[Sue]:
    """Read information about each Sue from a file."""

    with open(file_path, encoding="utf-8") as file:
        return [parse_sue(line.strip()) for line in file]
    

def parse_sue(line: str) -> Sue:
    """Parse information about an Aunt Sue from a line of text."""

    pattern_match = re.match(SUE_REGEX, line)
    if not pattern_match:
        raise ValueError(f"Invalid Sue data: {line}")
    
    number = int(pattern_match.group(1))
    properties = pattern_match.group(2).split(", ")

    sue = Sue(number)
    for property in properties:
        key, value = property.split(": ")
        setattr(sue, key, int(value))

    return sue


def find_matching_sue(candidates: list[Sue], target: Sue, comparison_rules: ComparisonRules = COMPARE_BY_EQUIVALENCE) -> Optional[Sue]:
    """Find the Aunt Sue whose properties match the target's."""

    for candidate in candidates:
        if sue_matches_target(candidate, target, comparison_rules):
            return candidate

    return None


def sue_matches_target(candidate: Sue, target: Sue, comparison_rules: ComparisonRules = COMPARE_BY_EQUIVALENCE,) -> bool:
    """Determine if an Aunt Sue's properties match the target's."""

    properties = {key: value for key, value in candidate.__dict__.items() if key != "number"}

    for key, value in properties.items():
        if value is None:
            continue

        target_property_value = getattr(target, key)
        if target_property_value is None:
            continue

        comparator = getattr(comparison_rules, key)
        if comparator(value, target_property_value) is False:
            return False
        
    return True


def main() -> None:
    """Read information about each Aunt Sue and process it."""

    input_file = INPUT_FILE
    file_path = path.join(path.dirname(__file__), input_file)

    sues = read_sues(file_path)

    gift_sender_by_equivalence = find_matching_sue(sues, TARGET_SUE)
    print("When comparing properties exactly:")
    if gift_sender_by_equivalence:
        print(f"The gift sender is Sue {gift_sender_by_equivalence.number}.")
    else:
        print("No Aunt Sue matches the target properties.")
    print()

    gift_sender_by_ranges = find_matching_sue(sues, TARGET_SUE, comparison_rules=COMPARE_WITH_RANGES)
    print("When comparing properties with ranges:")
    if gift_sender_by_ranges:
        print(f"The gift sender is Sue {gift_sender_by_ranges.number}.")
    else:
        print("No Aunt Sue matches the target properties.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python

from time import perf_counter
from typing import List

import re

"""
--- Part 1 ---
The newly-improved calibration document consists of lines of text; each line originally contained a
specific calibration value that the Elves now need to recover. On each line, the calibration value
can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these
together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

--- Part 2 ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with
letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits". Equipped
with this new information, you now need to find the real first and last digit on each line.

For example:
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

digits = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
]


def import_puzzle_data() -> List[str]:
    """Import puzzle data in a format best suited for the code challenge"""
    with open("puzzle-data.txt") as f:
        return [datum.strip().replace("\n", "").lower() for datum in f.readlines()]


def match_and_replace_digits(target_str: str) -> None:
    """Match and replace digit strings with numbers"""
    for word, digit in digits:
        target_str = target_str.replace(word, digit)


def find_sum_of_first_and_last_digit_in_string(puzzle_input: List[str]) -> int:
    """Find first and last digit of a string in a list of strings with digits mixed with characters"""
    return sum(
        list(
            map(
                lambda num: int(num[0] + num[-1]),
                list(map(lambda data: re.sub("[a-zA-Z]", "", data), puzzle_input)),
            )
        )
    )


def find_sum_of_alphabetic_digits(puzzle_input: List[str]) -> int:
    """Find first and last digit in string in a list of strings with alphabetic digits"""
    check = map(
        lambda puzzle_string: match_and_replace_digits(puzzle_string),
        list(map(lambda data: re.sub("[0-9]", "", data), puzzle_input)),
    )

    for puzzle_string in puzzle_input:
        print(puzzle_string)
        match_and_replace_digits(puzzle_string)
        print(puzzle_string)

    return 0


def main():
    start_time = perf_counter()
    puzzle_data = import_puzzle_data()
    puzzle_load_time = perf_counter() - start_time

    part_one_start_time = perf_counter()
    part_one_result = find_sum_of_first_and_last_digit_in_string(puzzle_data)
    part_one_end_time = perf_counter() - part_one_start_time

    part_two_start_time = perf_counter()
    part_two_result = find_sum_of_alphabetic_digits(puzzle_data)
    part_two_end_time = perf_counter() - part_two_start_time

    elapsed_time = perf_counter() - start_time

    print(
        f"Part one result [{part_one_end_time:.3f} ms]: {part_one_result}"
        + f"\nPart two result [{part_two_end_time:.3f} ms]: {part_two_result}"
        + f"\n\nLoaded puzzle data: {puzzle_load_time:.3f} ms.\nTotal elapsed time: {elapsed_time:.3f} ms"
    )


if __name__ == "__main__":
    main()

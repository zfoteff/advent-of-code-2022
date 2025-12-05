#!/usr/bin/env python

from typing import List

import re

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
    check = list(
        map(
            lambda puzzle_string: match_and_replace_digits(puzzle_string),
            list(map(lambda data: re.sub("[0-9]", "", data), puzzle_input)),
        )
    )

    print(list(map(lambda data: re.sub("[0-9]", "", data), puzzle_input)))
    return 0

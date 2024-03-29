#!/usr/bin/env python3

from time import perf_counter

import re
from typing import List, Tuple

"""
two lists of numbers separated by a vertical bar (|): a list of winning numbers and then a list
of numbers you have. You organize the information into a table (your puzzle input).

each match after the first doubles the point value of that card.

For example:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers
you have (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17,
and 86) are winning numbers! That means card 1 is worth 8 points (1 for the first match, then
doubled three times for each of the three matches after the first).

    Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
    Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
    Card 4 has one winning number (84), so it is worth 1 point.
    Card 5 has no winning numbers, so it is worth no points.
    Card 6 has no winning numbers, so it is worth no points.
"""


def import_puzzle_data() -> List[Tuple[str, ...]]:
    with open("puzzle-data.txt") as f:
        lines = f.readlines()
        puzzle_data = [
            tuple(re.sub(r"\s+", " ", line[10:]).replace("\n", "").strip().split(" | "))
            for line in lines
        ]

        return puzzle_data


def count_matches(puzzle_data: List[Tuple[str, ...]]) -> int:
    return sum(
        map(
            lambda x: 2 ** (x - 1) if x > 0 else 0,
            [
                len(
                    set(map(int, winning_numbers.split(" "))).intersection(
                        set(map(int, provided_numbers.split(" ")))
                    )
                )
                for winning_numbers, provided_numbers in puzzle_data
            ],
        )
    )


def main():
    start_time = perf_counter()
    puzzle_data = import_puzzle_data()
    puzzle_load_time = perf_counter() - start_time

    part_one_start_time = perf_counter()
    part_one_result = count_matches(puzzle_data)
    part_one_end_time = perf_counter() - part_one_start_time

    part_two_start_time = perf_counter()
    part_two_result = 0
    part_two_end_time = perf_counter() - part_two_start_time

    elapsed_time = perf_counter() - start_time

    print(
        f"Part one result [{part_one_end_time:.3f} ms]: {part_one_result}"
        + f"\nPart two result [{part_two_end_time:.3f} ms]: {part_two_result}"
        + f"\n\nLoaded puzzle data: {puzzle_load_time:.3f} ms.\nTotal elapsed time: {elapsed_time:.3f} ms"
    )


if __name__ == "__main__":
    main()

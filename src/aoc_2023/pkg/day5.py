#!/usr/bin/env python3

from time import perf_counter

import re
from typing import List, Tuple

"""
"""


def import_puzzle_data() -> List[Tuple[str, ...]]:
    with open("puzzle-data.txt") as f:
        lines = f.readlines()
        puzzle_data = []

        return puzzle_data


def main():
    start_time = perf_counter()
    puzzle_data = import_puzzle_data()
    puzzle_load_time = perf_counter() - start_time

    part_one_start_time = perf_counter()
    part_one_result = 0
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

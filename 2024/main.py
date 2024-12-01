#!/usr/bin/python3

from utils.timed_runner import timed_advent_of_code_runner

from pkg.day1 import (
    calculate_distance_between_location_ids,
    calculate_similarity_score,
    import_day_1_puzzle_data,
)
from pkg.day2 import part_1, part_2, import_day_2_puzzle_data


def main():
    """Runner file for 2024 advent of code submissions. Returns all puzzles with timing and results"""

    # Day 1
    timed_advent_of_code_runner(
        "Day 1",
        "./data/day-1-puzzle-data.txt",
        calculate_distance_between_location_ids,
        calculate_similarity_score,
        import_day_1_puzzle_data,
    )

    # Day 2
    timed_advent_of_code_runner(
        "Day 2",
        "./data/day-2-puzzle-data.txt",
        part_1,
        part_2,
        import_day_2_puzzle_data,
    )


if __name__ == "__main__":
    main()

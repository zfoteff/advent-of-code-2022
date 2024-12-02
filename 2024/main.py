#!/usr/bin/python3
from time import perf_counter
from utils.timed_runner import timed_advent_of_code_runner

from pkg.day1 import (
    calculate_distance_between_location_ids,
    calculate_similarity_score,
    import_day_1_puzzle_data,
)
from pkg.day2 import (
    reduce_to_safe_and_unsafe,
    reduce_to_safe_and_unsafe_with_tolerence,
    import_day_2_puzzle_data,
)
from pkg.day3 import part_one, part_two, import_day_3_puzzle_data


def main():
    """Runner file for 2024 advent of code submissions. Returns all puzzles with timing and results"""
    start_time = perf_counter()

    # # Day 1
    # timed_advent_of_code_runner(
    #     "Day 1",
    #     "./data/day-1-puzzle-data.txt",
    #     calculate_distance_between_location_ids,
    #     calculate_similarity_score,
    #     import_day_1_puzzle_data,
    # )

    # Day 2
    timed_advent_of_code_runner(
        "Day 2",
        "./data/day-2-puzzle-data.txt",
        reduce_to_safe_and_unsafe,
        reduce_to_safe_and_unsafe_with_tolerence,
        import_day_2_puzzle_data,
    )

    # timed_advent_of_code_runner(
    #     "Day 3",
    #     "./data/day-2-puzzle-data.txt",
    #     part_one,
    #     part_two,
    #     import_day_3_puzzle_data,
    # )

    elapsed_time = perf_counter() - start_time
    print(f"Completed AoC 2024 Runner in {elapsed_time:.4f} s")


if __name__ == "__main__":
    main()

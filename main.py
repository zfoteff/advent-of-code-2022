import argparse
from time import perf_counter

from utils.advent_of_code_runner import timed_advent_of_code_runner

VALID_YEARS = [2022, 2023, 2024, 2025]


def run_2023_tests():
    from pkg.aoc_2023.pkg import day1, day2, day3, day4, day5

    start_time = perf_counter()

    timed_advent_of_code_runner(
        "Day 1",
        "data/day-1-puzzle-data.txt",
        day1.find_sum_of_first_and_last_digit_in_string,
        day1.find_sum_of_alphabetic_digits,
        day1.import_puzzle_data,
    )

    timed_advent_of_code_runner(
        "Day 2",
        "data/day-2-puzzle-data.txt",
        day2.determine_sum_of_game_ids_with_valid_games,
        day2.determine_minimum_amount_of_cubes_for_valid_game,
        day2.import_puzzle_data,
    )

    timed_advent_of_code_runner(
        "Day 3",
        "data/day-3-puzzle-data.txt",
        day3.get_adjacent_numbers_to_symbol,
        day3.get_gear_ratios,
        day3.import_puzzle_data,
    )

    elapsed_time = perf_counter() - start_time
    print(f"Completed AoC 2025 Runner in {elapsed_time*1000:.4f} ms")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Program to run Advent of Code suites from multiple or specific years"
    )
    parser.add_argument(
        "-y",
        "--year",
        help="Run suite from selected advent of code year",
        action="store_true",
    )
    parser.add_argument("")

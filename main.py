from time import perf_counter

from utils.advent_of_code_runner import timed_advent_of_code_runner


def run_2022_tests() -> None:
    from src.aoc_2022.pkg import day1, day2, day3

    start_time = perf_counter()

    timed_advent_of_code_runner(
        "Day 1",
        "src/aoc_2022/data/day-1-puzzle-data.txt",
        day1.find_max_calories_sum,
        day1.find_top_three_largest_amounts_of_calories_sum,
        day1.import_puzzle_data,
    )

    timed_advent_of_code_runner(
        "Day 2",
        "src/aoc_2022/data/day-2-puzzle-data.txt",
        day2.play_rock_paper_scissors,
        day2.play_cheater_rock_paper_scissors,
        day2.import_puzzle_data,
    )

    timed_advent_of_code_runner(
        "Day 3",
        "src/aoc_2022/data/day-3-puzzle-data.txt",
        day3.count_item_priority,
        day3.count_badge_priority,
        day3.import_puzzle_data,
    )

    elapsed_time = perf_counter() - start_time
    print(f"Completed AoC 2022 Runner in {elapsed_time*1000:.4f} ms")


def run_2023_tests() -> None:
    from src.aoc_2023.pkg import day1, day2, day3, day4

    start_time = perf_counter()

    timed_advent_of_code_runner(
        "Day 1",
        "src/aoc_2023/data/day-1-puzzle-data.txt",
        day1.find_sum_of_first_and_last_digit_in_string,
        day1.find_sum_of_alphabetic_digits,
        day1.import_puzzle_data,
    )

    timed_advent_of_code_runner(
        "Day 2",
        "src/aoc_2023/data/day-2-puzzle-data.txt",
        day2.determine_sum_of_game_ids_with_valid_games,
        day2.determine_minimum_amount_of_cubes_for_valid_game,
        day2.import_puzzle_data,
    )

    timed_advent_of_code_runner(
        "Day 3",
        "src/aoc_2023/data/day-3-puzzle-data.txt",
        day3.get_adjacent_numbers_to_symbol,
        day3.get_gear_ratios,
        day3.import_puzzle_data,
    )

    timed_advent_of_code_runner(
        "Day 4",
        "src/aoc_2023/data/day-4-puzzle-data.txt",
        day4.count_matches,
        day4.part_two,
        day4.import_puzzle_data,
    )

    elapsed_time = perf_counter() - start_time
    print(f"Completed AoC 2023 Runner in {elapsed_time*1000:.4f} ms")


def run_2024_tests():
    from src.aoc_2024.pkg import day1, day2, day3

    start_time = perf_counter()
    # Day 1
    timed_advent_of_code_runner(
        "Day 1",
        "src/aoc_2024/data/day-1-puzzle-data.txt",
        day1.calculate_distance_between_location_ids,
        day1.calculate_similarity_score,
        day1.import_puzzle_data,
    )

    # Day 2
    timed_advent_of_code_runner(
        "Day 2",
        "src/aoc_2024/data/day-2-puzzle-data.txt",
        day2.reduce_to_safe_and_unsafe,
        day2.reduce_to_safe_and_unsafe_with_tolerence,
        day2.import_puzzle_data,
    )

    # Day 3
    timed_advent_of_code_runner(
        "Day 3",
        "src/aoc_2024/data/day-3-puzzle-data.txt",
        day3.extract_mul_commands,
        day3.part_two,
        day3.import_puzzle_data,
    )

    elapsed_time = perf_counter() - start_time
    print(f"Completed AoC 2024 Runner in {elapsed_time*1000:.4f} ms")


def run_2025_tests():
    from src.aoc_2025.pkg import day1, day2, day3, day4

    start_time = perf_counter()

    timed_advent_of_code_runner(
        "Day 1",
        "src/aoc_2025/data/day-1-puzzle-data.txt",
        day1.adjust_dials_and_count_zeros,
        day1.adjust_dials_and_count_passes_over_zero,
        day1.import_puzzle_data,
    )

    timed_advent_of_code_runner(
        "Day 2",
        "src/aoc_2025/data/day-2-puzzle-data.txt",
        day2.part_one,
        day2.part_two,
        day2.import_puzzle_data,
    )

    timed_advent_of_code_runner(
        "Day 3",
        "src/aoc_2025/data/day-3-puzzle-data.txt",
        day3.part_one,
        day3.part_two,
        day3.import_puzzle_data,
    )

    timed_advent_of_code_runner(
        "Day 4",
        "src/aoc_2025/data/day-4-puzzle-data.txt",
        day4.part_one,
        day4.part_two,
        day4.import_puzzle_data,
    )

    elapsed_time = perf_counter() - start_time
    print(f"Completed AoC 2025 Runner in {elapsed_time*1000:.4f} ms")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="Program to run Advent of Code suites from multiple or specific years"
    )
    parser.add_argument(
        "-y",
        "--year",
        default=[],
        action="append",
        help="Run suite from selected range of advent of code years",
    )

    ADVENT_OF_CODE_FUNCTIONS = {
        "2022": run_2022_tests,
        "2023": run_2023_tests,
        "2024": run_2024_tests,
        "2025": run_2025_tests,
    }

    args = parser.parse_args()

    if args.year == []:
        for year in ADVENT_OF_CODE_FUNCTIONS.keys():
            ADVENT_OF_CODE_FUNCTIONS[year]()
    else:
        for year in args.year:
            ADVENT_OF_CODE_FUNCTIONS[year]()

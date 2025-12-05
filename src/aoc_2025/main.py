from time import perf_counter

from utils.advent_of_code_runner import timed_advent_of_code_runner
from pkg.day1 import (
    import_day_1_puzzle_data,
    adjust_dials_and_count_zeros,
    adjust_dials_and_count_passes_over_zero,
)


def main():
    start_time = perf_counter()

    # Day 1

    timed_advent_of_code_runner(
        "Day 1",
        "data/day-1-puzzle-data.txt",
        adjust_dials_and_count_zeros,
        adjust_dials_and_count_passes_over_zero,
        import_day_1_puzzle_data,
    )

    elapsed_time = perf_counter() - start_time
    print(f"Completed AoC 2025 Runner in {elapsed_time*1000:.4f} ms")


if __name__ == "__main__":
    main()

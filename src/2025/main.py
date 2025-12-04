from pkg.day1 import import_day_1_puzzle_data, part_one, part_two
from time import perf_counter
from ..utils.advent_of_code_runner import timed_advent_of_code_runner


def main():
    start_time = perf_counter()

    # Day 1
    timed_advent_of_code_runner(
        "Day 1",
        "./data/day-1-puzzle-data.txt",
        part_one,
        part_two,
        import_day_1_puzzle_data,
    )

    elapsed_time = perf_counter() - start_time
    print(f"Completed AoC 2025 Runner in {elapsed_time*1000:.4f} ms")


if __name__ == "__main__":
    main()

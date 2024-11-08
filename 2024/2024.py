from utils.timed_runner import timed_advent_of_code_runner

from pkg.day1 import part_one, part_two, import_puzzle_data


def main():
    # Day 1
    timed_advent_of_code_runner(
        "Day 1", 
        "data/day-1-puzzle-data.txt", 
        part_one, 
        part_two, 
        import_puzzle_data
    )

    # Day 2


if __name__ == "__main__":
    main()

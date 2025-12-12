from typing import List


def import_puzzle_data(data_path: str) -> List[List[str]]:
    with open(data_path) as f:
        return [line.strip() for line in f.readlines()]


def part_one(puzzle_input) -> int:
    print(puzzle_input)
    return 0


def part_two(puzzle_input) -> int:
    return 0

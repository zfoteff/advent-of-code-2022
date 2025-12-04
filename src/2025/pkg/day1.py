from typing import List, Tuple


def import_day_1_puzzle_data(data_path: str) -> Tuple[str, List[int]]:
    with open(data_path) as f:
        data = [datum.strip() for datum in f.readlines()]
        print(data)


def part_one(puzzle_input) -> int:
    pass


def part_two(puzzle_input) -> int:
    pass

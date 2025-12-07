from typing import List, Tuple


def import_puzzle_data(data_path) -> List[Tuple[int, int]]:
    with open(data_path) as f:
        return [tuple(map(int, datum.split("-"))) for datum in f.readlines()]


def part_one(puzzle_data: List[Tuple[int, int]]) -> int:
    counter = 0

    for start_range, end_range in puzzle_data:
        for num in list(map(str, range(start_range, end_range + 1))):
            num_dict = dict()

            for digit in num:
                num_dict.setdefault(digit, 0)
                num_dict[digit] += 1

            if sum(num_dict.values()) % len(num_dict) == 2:
                counter += 1

    return counter


def part_two(puzzle_data: List[Tuple[int, int]]) -> int:
    return 0

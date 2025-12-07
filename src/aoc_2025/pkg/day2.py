from typing import List, Tuple


def import_puzzle_data(data_path) -> List[Tuple[int, int]]:
    with open(data_path) as f:
        return [tuple(map(int, datum.split("-"))) for datum in f.readlines()]


def part_one(puzzle_data: List[Tuple[int, int]]) -> int:
    counter = 0

    for start_range, end_range in puzzle_data:
        for number in range(start_range, end_range + 1):
            num = str(number)
            if len(num) % 2 != 0:
                continue
            if num[: len(num) // 2] == num[len(num) // 2 :]:
                counter += number

    return counter


def part_two(puzzle_data: List[Tuple[int, int]]) -> int:
    return 0

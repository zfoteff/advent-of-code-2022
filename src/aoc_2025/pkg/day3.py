from typing import List


def import_puzzle_data(puzzle_data: str) -> List[str]:
    with open(puzzle_data) as f:
        return [data.strip() for data in f.readlines()]


def part_one(puzzle_data: List[str]) -> int:
    counter = 0
    for data in list(map(list, puzzle_data)):
        data.sort(reverse=True)
        counter += int(data[0] + data[1])

    return counter


def part_two(puzzle_data: List[str]) -> int:
    return 0

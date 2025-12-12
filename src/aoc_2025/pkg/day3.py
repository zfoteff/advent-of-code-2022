from typing import List


def import_puzzle_data(puzzle_data: str) -> List[str]:
    with open(puzzle_data) as f:
        return [data.strip() for data in f.readlines()]


def part_one(puzzle_data: List[str]) -> int:
    counter = 0

    for data in puzzle_data:
        first_battery = 0
        second_battery = 0

        for digit in range(len(data) - 1):
            if int(data[digit]) > first_battery:
                first_battery = int(data[digit])
                second_battery = int(data[digit + 1])
            if int(data[digit + 1]) > second_battery:
                second_battery = int(data[digit + 1])

        counter += int(f"{first_battery}{second_battery}")

    return counter


def part_two(puzzle_data: List[str]) -> int:
    return 0

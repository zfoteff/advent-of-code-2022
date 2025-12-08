from typing import List


def import_puzzle_data(puzzle_data: str) -> List[str]:
    with open(puzzle_data) as f:
        return [data.strip() for data in f.readlines()]


def part_one(puzzle_data: List[str]) -> int:
    counter = 0

    for data in puzzle_data:
        first_battery = 0
        second_battery = 0
        print(data)

        for digit in data:
            if int(digit) > first_battery and int(digit) > second_battery:
                first_battery = int(digit)
            elif int(digit) <= first_battery and int(digit) > second_battery:
                second_battery = int(digit)

        print(f"{first_battery}{second_battery}")
        counter += int(f"{first_battery}{second_battery}")

    return counter


def part_two(puzzle_data: List[str]) -> int:
    return 0

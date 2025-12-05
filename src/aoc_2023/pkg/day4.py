import re
from typing import List, Tuple


def import_puzzle_data() -> List[Tuple[str, ...]]:
    with open("puzzle-data.txt") as f:
        lines = f.readlines()
        puzzle_data = [
            tuple(re.sub(r"\s+", " ", line[10:]).replace("\n", "").strip().split(" | "))
            for line in lines
        ]

        return puzzle_data


def count_matches(puzzle_data: List[Tuple[str, ...]]) -> int:
    return sum(
        map(
            lambda x: 2 ** (x - 1) if x > 0 else 0,
            [
                len(
                    set(map(int, winning_numbers.split(" "))).intersection(
                        set(map(int, provided_numbers.split(" ")))
                    )
                )
                for winning_numbers, provided_numbers in puzzle_data
            ],
        )
    )


def part_two():
    return 0

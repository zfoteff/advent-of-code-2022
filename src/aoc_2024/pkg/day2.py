from typing import List


def import_puzzle_data(data_path: str) -> List[List[int]]:
    with open(data_path) as f:
        return [
            list(map(lambda x: int(x), datum.strip().replace("\n", "").split(" ")))
            for datum in f.readlines()
        ]


def _reduce(puzzle_data: List[int], tolerence: int = 0) -> int:
    is_increasing = False
    is_decreasing = False
    defer_roc = False
    i = 0

    while i < len(puzzle_data) - 1:
        change = puzzle_data[i] - puzzle_data[i + 1]
        if i == 0 or defer_roc:
            if change < 0:
                is_decreasing = True
                defer_roc = False
            elif change > 0:
                is_increasing = True
                defer_roc = False
            elif change == 0:
                if tolerence == 0:
                    return 0
                tolerence -= 1
                defer_roc = True

        if abs(change) > 3 or change == 0:
            if tolerence == 0:
                return 0
            tolerence -= 1
        if change < 0 and is_increasing:
            if tolerence == 0:
                return 0
            tolerence -= 1
        if change > 0 and is_decreasing:
            if tolerence == 0:
                return 0
            tolerence -= 1
        i += 1
    return 1


def reduce_to_safe_and_unsafe(puzzle_data: List[List[int]]):
    return sum([_reduce(data) for data in puzzle_data])


def reduce_to_safe_and_unsafe_with_tolerence(puzzle_data: List[List[int]]):
    return sum([_reduce(data, tolerence=1) for data in puzzle_data])

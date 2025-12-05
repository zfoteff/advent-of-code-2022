from typing import List


def import_puzzle_data(data_path: str) -> List[List[int]]:
    with open(data_path) as f:
        return [
            list(map(int, datum.split("\n")))
            for datum in f.read().strip().split("\n\n")
        ]


def find_max_calories_sum(puzzle_data: List[List[int]]) -> int:
    return max(map(sum, puzzle_data))


def find_top_three_largest_amounts_of_calories_sum(puzzle_data: List[List[int]]) -> int:
    puzzle_data_sums = [sum(item) for item in puzzle_data]

    top_calories = list()
    while len(top_calories) < 3:
        max_value = max(puzzle_data_sums)
        top_calories.append(max_value)
        puzzle_data_sums.pop(puzzle_data_sums.index(max_value))

    return sum(top_calories)

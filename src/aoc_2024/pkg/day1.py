from typing import List, Tuple


def import_puzzle_data(data_path: str) -> Tuple[List[int], List[int]]:
    with open(data_path) as f:
        data = [datum.strip().replace("\n", "").split("   ") for datum in f.readlines()]
        return sorted([int(value[0]) for value in data]), sorted(
            [int(value[1]) for value in data]
        )


def calculate_distance_between_location_ids(
    puzzle_input: Tuple[List[int], List[int]],
) -> int:
    return sum([abs(l - r) for l, r in zip(puzzle_input[0], puzzle_input[1])])


def calculate_similarity_score(puzzle_input: Tuple[List[int], List[int]]) -> int:
    left, right = puzzle_input
    return sum([value * right.count(value) for value in left])

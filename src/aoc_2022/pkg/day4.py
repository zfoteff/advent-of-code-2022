from typing import List, Tuple


def load_puzzle_data() -> List[Tuple[str, str]]:
    with open("data.txt") as f:
        puzzle_data = [
            tuple(map(str, datum.split(","))) for datum in f.read().splitlines()
        ]
        print(puzzle_data)
    return puzzle_data
